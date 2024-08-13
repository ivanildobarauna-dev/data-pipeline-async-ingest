import os
import logging

from pipeline.launcher import run

if __name__ == "__main__":
    if not os.getenv("env"):
        os.environ["env"] = "test"
    logging.getLogger().setLevel(logging.INFO)
    run()
