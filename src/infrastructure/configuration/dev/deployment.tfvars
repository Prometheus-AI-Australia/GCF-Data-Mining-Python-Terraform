credentials = "~/.gcp/public-demos.json"

project_id = "prometheus-ai-public-demos"
region = "australia-southeast1"

function_name = "data-mining-demo-dev"
pubsub_topic_name = "data-mining-demo-dev-topic"
cronjob_name = "15MinuteScheduler-dev"

create_buckets = false

output_bucket = "prometheus-ai-public-demos-data"
output_prefix = "gcf-data-mining/dev"
source_bucket = "prometheus-ai-public-demos-source"

function_source_local = "src/function"
function_source_remote = "gcf-data-mining/dev/function.zip"