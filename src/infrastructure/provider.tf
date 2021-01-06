terraform {
  backend "gcs" {}
}


provider "google" {
  project     = var.project_id
  credentials = var.credentials
  region      = var.region
}

