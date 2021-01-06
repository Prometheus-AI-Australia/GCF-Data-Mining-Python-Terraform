variable "credentials" {
  type = string
}

variable "project_id" {
  type = string
}

variable "region" {
  type    = string
  default = "us-central1"
}

variable "create_buckets" {
  type    = bool
  default = false
}

variable "output_bucket" {
  type = string
}

variable "output_prefix" {
  type = string
}

variable "source_bucket" {
  type    = string
  default = null
}

variable "function_name" {
  type = string
}

variable "pubsub_topic_name" {
  type = string
}

variable "cronjob_name" {
  type = string
}

variable "function_source_local" {
  type = string
}

variable "function_source_remote" {
  type = string
}
