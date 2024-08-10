import apache_beam as beam
from pipeline.config.common import Constants
from pipeline.config.bigquery.table_registry import STG
from pipeline.config.options import get_options
from pipeline.transform.generic_transforms import set_key, set_datetime


def run():
    with beam.Pipeline(options=get_options()) as p:
        (
            p
            | "ReadFromPubSub"
            >> beam.io.ReadFromPubSub(subscription=Constants.PUBSUB_SUBSCRIPTION)
            | "Decode" >> beam.Map(lambda x: x.decode("utf-8"))
            | "CreateKey" >> beam.Map(set_key, "created_at", 8)
            | "Window" >> beam.WindowInto(beam.window.FixedWindows(5))
            | "GroupbyMessage" >> beam.GroupByKey()
            | "ExtractMessage" >> beam.Map(lambda x: x[1])
            | "ParseToJson" >> beam.Map(set_datetime, "ARRIVAL_DATE", "data")
            | "Flatten" >> beam.FlatMap(lambda x: x)
            | "WriteToBigQuery"
            >> beam.io.WriteToBigQuery(
                table=STG.api_data.get_table_name(),
                schema=STG.api_data.schema(),
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                method="STREAMING_INSERTS",
            )
        )
