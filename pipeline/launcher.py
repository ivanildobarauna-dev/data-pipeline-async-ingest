import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

from pipeline.config.common import (
    default_timestamp_formated,
    Constants,
    default_timestamp_str,
)


def set_key(element):
    key = eval(element)["created_at"]
    return str(key)[:8], element


def run():
    pipeline_options = PipelineOptions(
        job_name=f"data-consumer-pipeline-{default_timestamp_str()}"
    )

    with beam.Pipeline(options=pipeline_options) as p:
        messages = p | "ReadFromPubSub" >> beam.io.ReadFromPubSub(
            subscription=Constants.PUBSUB_SUBSCRIPTION
        )
        decoded_messages = messages | "Decode" >> beam.Map(lambda x: x.decode("utf-8"))
        keyed_messages = decoded_messages | "CreateKey" >> beam.Map(set_key)
        windowed_messages = keyed_messages | "Window" >> beam.WindowInto(
            beam.window.FixedWindows(5)
        )
        grouped_messages = windowed_messages | "GroupbyMessage" >> beam.GroupByKey()
        counted_messages = (
            grouped_messages | "CountPerWindow" >> beam.combiners.Count.PerElement()
        )
        counted_messages | "Print" >> beam.Map(print)
