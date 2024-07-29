from pipeline.config.common import default_timestamp_str, EnvSetup


class BeamConfig:
    def __init__(self, env: EnvSetup):
        self.env = env

    def get_pipeline_options(self) -> dict:
        if self.env == EnvSetup.PROD:
            return {
                "runner": "DataflowRunner",
                "project": "ivanildobarauna",
                "region": "us-central1",
                "temp_location": "gs://gcp-streaming-pipeline-dataflow/dataflow/temp",
                "staging_location": "gs://gcp-streaming-pipeline-dataflow/temp",
                "min_workers": 1,
                "num_workers": 1,
                "max_num_workers": 2,
                "autoscaling_algorithm": "THROUGHPUT_BASED",
                "save_main_session": True,
                "machine_type": "n1-standard-1",
                "job_name": f"data-consumer-pipeline-prod",
                "disk_size_gb": "10",
                "streaming": True,
            }
        else:
            return {
                "runner": "DirectRunner",
                "save_main_session": True,
                "num_workers": 1,
                "job_name": f"data-consumer-pipeline-test",
                "disk_size_gb": "10",
                "streaming": True,
                "save_main_session": True,
            }
