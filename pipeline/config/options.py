from apache_beam.options.pipeline_options import PipelineOptions
from pipeline.config.common import default_timestamp_str


def get_options():
    pipeline_options = PipelineOptions(
        job_name=f"data-consumer-pipeline-{default_timestamp_str()}", streaming=True
    )
    return pipeline_options
