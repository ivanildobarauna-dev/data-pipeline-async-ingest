python main.py --project ivanildobarauna \
               --region us-east4 \
               --runner Dataflowrunner \
--staging_location gs://gcp-streaming-pipeline-dataflow/staging \
--temp_location gs://gcp-streaming-pipeline-dataflow/temp \
--sdk_container_image=us-central1-docker.pkg.dev/ivanildobarauna/dataflow-ar/custom-beam/img:latest
--sdk_location=container &
