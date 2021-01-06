credentials = "~/.gcp/public-demos.json"

project_id = "prometheus-ai-public-demos"
region = "australia-southeast1"

function_name = "data-mining-demo-prod"
pubsub_topic_name = "data-mining-demo-prod-topic"
cronjob_name = "15MinuteScheduler-prod"

create_buckets = false

output_bucket = "prometheus-ai-public-demos-data"
output_prefix = "gcf-data-mining/dev"
source_bucket = "prometheus-ai-public-demos-source"

function_source_local = "src/function"
function_source_remote = "gcf-data-mining/prod/function.zip"