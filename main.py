import logging

from pipeline.launcher import run

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    run()
