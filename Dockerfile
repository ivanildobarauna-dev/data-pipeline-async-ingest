FROM apache/beam_python3.9_sdk:2.57.0

WORKDIR /app

# Update pip and install poetry
RUN pip install --upgrade pip \
    && pip install poetry

# Copy application for container
COPY pipeline ./pipeline
COPY pyproject.toml .
COPY poetry.lock .

# Instale as dependências usando Poetry
RUN poetry config virtualenvs.create false

RUN poetry install

# [DEBUG] Set the entrypoint to /bin/bash
#ENTRYPOINT ["/bin/bash"]
