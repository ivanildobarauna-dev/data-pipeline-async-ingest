## Using setup.py

#python main.py --project ivanildobarauna \
#               --region us-east4 \
#               --runner Dataflowrunner \
#--setup_file ./setup.py \
#--staging_location gs://gcp-streaming-pipeline-dataflow/staging \
#--temp_location gs://gcp-streaming-pipeline-dataflow/temp \
#--save_main_session

## Using container

python main.py --project ivanildobarauna \
               --region us-east4 \
               --runner DataflowRunner \
               --staging_location gs://gcp-streaming-pipeline-dataflow/staging \
               --temp_location gs://gcp-streaming-pipeline-dataflow/temp \
               --sdk_container_image=us-central1-docker.pkg.dev/ivanildobarauna/dataflow-ar/custom-beam/img:latest \
               --sdk_location=container \
               --worker_machine_type=n1-standard-1 \
               --num_workers=1 \
               --max_num_workers=1 \
               --autoscaling_algorithm=NONE

