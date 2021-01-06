from diagrams import Diagram, Cluster
from diagrams.gcp.compute import GCF
from diagrams.gcp.storage import GCS

from diagrams.onprem.iac import Terraform
from diagrams.programming.language import Python

Terraform._height = 0.9
Python._height = 0.9

diagram_kwargs = dict(direction="LR", filename="docs/diagram", show=False)


with Diagram("GCF Data Mining Example", **diagram_kwargs):

    with Cluster("DevOps & Source Code") as devops:
        source_code = GCS("Source Code Bucket")
        python = Python()

        state = GCS("Terraform State Bucket")
        terraform = Terraform()

    with Cluster("Application") as app:
        function = GCF("Data Mining Service")
        data = GCS("Data Bucket")

    source_code >> python >> function
    state >> terraform >> function
    function >> data
