import logging
import json

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

from pipeline.config.common import (
    default_timestamp_formated,
    Constants,
    default_timestamp_str,
)

from datetime import datetime


def set_key(element):
    key = eval(element)["created_at"]
    return str(key)[:8], element


def log_fn(element):
    logging.info(element)
    return element


def transform_data(element):
    new_list = []
    for item in element:
        dic = {}
        dic["ARRIVAL_DATE"] = datetime.now()
        dic["data"] = item
        new_list.append(dic)

    return new_list


def bigquery_schema():
    table_schema = "ARRIVAL_DATE:DATETIME, data:STRING"
    return table_schema


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
            beam.window.FixedWindows(60)
        )
        grouped_messages = windowed_messages | "GroupbyMessage" >> beam.GroupByKey()
        extracted_messages = grouped_messages | "ExtractMessage" >> beam.Map(
            lambda x: x[1]
        )
        parse_json = extracted_messages | "ParseToJson" >> beam.Map(transform_data)
        # parse_json | "Print" >> beam.Map(log_fn)
        flatter = parse_json | "Flatten" >> beam.FlatMap(lambda x: x)
        flatter | "WriteToBigQuery" >> beam.io.WriteToBigQuery(
            table="STG.api_data",
            schema=bigquery_schema(),
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
            method="STREAMING_INSERTS",
        )
