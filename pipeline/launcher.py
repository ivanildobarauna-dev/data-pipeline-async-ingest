import apache_beam as beam
from pipeline.config.beam_config import get_options
from pipeline.config.gcp.constants import PUBSUB_SUBSCRIPTION
from pipeline.utils.send_metrics import MetricsClient
from pipeline.config.app.constants import APPLICATION_NAME
from pipeline.transform.generic_transforms import set_key, set_datetime
from pipeline.config.gcp.bigquery.table_registry import STG


metrics_client = MetricsClient()


def increment_metric(element, metric_name: str):
    metrics_client.incr(metric_name=f"{APPLICATION_NAME}.{metric_name}", value=1)
    return element


def run():
    with beam.Pipeline(options=get_options()) as p:
        (
            p
            | "ReadTopic" >> beam.io.ReadFromPubSub(subscription=PUBSUB_SUBSCRIPTION)
            | "ExtractMetric" >> beam.Map(lambda x: increment_metric(x, "extracted"))
            | "Decode" >> beam.Map(lambda x: x.decode("utf-8"))
            | "CreateKey" >> beam.Map(set_key, "created_at", 8)
            | "Window" >> beam.WindowInto(beam.window.FixedWindows(5))
            | "GroupMessage" >> beam.GroupByKey()
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
