FROM apache/beam_python3.10_sdk:2.57.0

COPY . .


ENV RUN_PYTHON_SDK_IN_DEFAULT_ENVIRONMENT=1

RUN pip install --upgrade pip

# Pre-install Python dependencies. For reproducibile builds,
# supply all of the dependencies and their versions in a requirements.txt file.
RUN pip install -r requirements.txt

# You can also install individual dependencies.
RUN pip install lxml
# Pre-install other dependencies.
RUN apt-get update \
  && apt-get dist-upgrade \
  && apt-get install -y --no-install-recommends ffmpeg

CMD ["python", "main.py", "--setup_file", "setup.py"]