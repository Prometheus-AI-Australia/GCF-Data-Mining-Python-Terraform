resource "google_storage_bucket" "output_bucket" {
  count = var.create_buckets ? 1 : 0
  name  = var.output_bucket
}

resource "google_storage_bucket" "source_bucket" {
  count = var.create_buckets ? 1 : 0
  name  = var.source_bucket
}
