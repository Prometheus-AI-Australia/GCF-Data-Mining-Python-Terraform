locals {
  build_path = ".build/function/archive.zip"
}

#####################
## GCF Source File ##
#####################

data "archive_file" "function_source" {
  type        = "zip"
  source_dir  = var.function_source_local
  output_path = local.build_path
}

resource "google_storage_bucket_object" "function_source" {
  bucket = var.source_bucket
  name   = var.function_source_remote
  source = local.build_path
}

####################
## Cloud Function ##
####################

resource "google_cloudfunctions_function" "collect_orderbook" {
  depends_on = [google_storage_bucket_object.function_source]

  name        = "${var.function_name}-collect-orderbook"
  description = "Mines publically available cryptocurrency data from Binance."
  runtime     = "python38"

  source_archive_bucket = var.source_bucket
  source_archive_object = var.function_source_remote

  available_memory_mb = 128
  entry_point         = "collect_orderbooks"

  event_trigger {
    event_type = "google.pubsub.topic.publish"
    resource   = google_pubsub_topic.cron.id
  }

  environment_variables = {
    "BUCKET_NAME" = var.output_bucket,
    "KEY_PREFIX"  = var.output_prefix,
    "TICKERS"     = "ETHBTC,LTCBTC",
  }
}


resource "google_cloudfunctions_function" "collect_candlesticks" {
  depends_on = [google_storage_bucket_object.function_source]

  name        = "${var.function_name}-collect-candlesticks"
  description = "Mines publically available cryptocurrency candlesticks data from Binance."
  runtime     = "python38"

  source_archive_bucket = var.source_bucket
  source_archive_object = var.function_source_remote

  available_memory_mb = 128
  entry_point         = "collect_candlesticks"

  event_trigger {
    event_type = "google.pubsub.topic.publish"
    resource   = google_pubsub_topic.cron.id
  }

  environment_variables = {
    "BUCKET_NAME" = var.output_bucket,
    "KEY_PREFIX"  = var.output_prefix,
    "TICKERS"     = "ETHBTC,LTCBTC",
  }
}

###################
## Pub/Sub Topic ##
###################

resource "google_pubsub_topic" "cron" {
  name = var.pubsub_topic_name
}

##############
## Cron Job ##
##############

resource "google_cloud_scheduler_job" "cron" {
  name        = var.cronjob_name
  description = "Publishes a message to Pub/Sub topic every 15 minutes."
  schedule    = "*/15 * * * *"

  pubsub_target {
    topic_name = google_pubsub_topic.cron.id
    data       = base64encode("...") # TODO: Figure out if I want to supply any data here.
  }
}
