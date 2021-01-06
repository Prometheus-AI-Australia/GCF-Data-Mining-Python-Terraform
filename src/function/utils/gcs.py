from google.cloud import storage

from .base import LazyClient


class GCSBucket(LazyClient):
    """Wrapper around raw GCS client.
    
    This class exists primarily for two reasons: (1.) to simplify the API
    for this particular application; and (2.) to allow for the GCS client to be
    shimmed during testing.
    """

    def __init__(self, configuration=None):
        super().__init__()
        self.client = storage.Client

        if configuration is not None:
            self.configure(configuration)

    def configure(self, config):
        self.bucket = config.gcp.bucket

    def upload(self, key, data, content_type="text/plain"):
        bucket = self.client.bucket(bucket_name=self.bucket)
        blob = bucket.blob(blob_name=key)

        blob.upload_from_string(data=data, content_type=content_type)

        return self
