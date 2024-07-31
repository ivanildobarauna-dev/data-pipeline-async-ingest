python main.py --project ivanildobarauna \
               --region us-east4 \
               --runner Dataflowrunner \
--setup_file ./setup.py \
--staging_location gs://gcp-streaming-pipeline-dataflow/staging \
--temp_location gs://gcp-streaming-pipeline-dataflow/temp \
--save_main_session