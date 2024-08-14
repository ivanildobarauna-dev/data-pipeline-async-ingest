from datadog import initialize, statsd
from pipeline.utils.instance_validator import Singleton
from pipeline.config.gcp.constants import PROJECT_ID, DD_AGENT_SERVER_SECRET_ID
from google.cloud import secretmanager
import os


class DataDogClient:
    def __init__(self):
        options = {"statsd_host": self.get_server_address(), "statsd_port": 8125}
        initialize(**options)

    def get_server_address(self):
        secret_client = secretmanager.SecretManagerServiceClient()

        request = {
            "name": f"projects/{PROJECT_ID}/secrets/{DD_AGENT_SERVER_SECRET_ID}/versions/latest",
        }

        secret_request = secret_client.access_secret_version(request=request)

        return secret_request.payload.data.decode("UTF-8")


class MetricsClient(Singleton):
    def __init__(self) -> None:
        if not hasattr(self, "initialized"):
            DataDogClient()
            self.initialized = True

    def incr(self, metric_name: str, action: str, value: int):
        statsd.increment(
            metric=metric_name,
            value=value,
            tags=["action:" + action, "env:" + os.getenv("env")],
        )
