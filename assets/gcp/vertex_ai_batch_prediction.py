# Vertex AI Batch Prediction: read from GCS and write to GCS
# Requires: pip install google-cloud-aiplatform
from google.cloud import aiplatform

PROJECT_ID = "YOUR_PROJECT_ID"
REGION = "us-central1"
MODEL_ID = "YOUR_MODEL_ID"
GCS_INPUT = "gs://YOUR_BUCKET/inputs/*.jsonl"  # instances format depends on model
GCS_OUTPUT = "gs://YOUR_BUCKET/outputs/batchpred/"

aiplatform.init(project=PROJECT_ID, location=REGION)

job = aiplatform.BatchPredictionJob.create(
    job_display_name="demo-batchpred",
    model_name=MODEL_ID,
    gcs_source_uris=[GCS_INPUT],
    gcs_destination_prefix=GCS_OUTPUT,
    instances_format="jsonl",
    predictions_format="jsonl",
    # Optional resources:
    # machine_type="n1-standard-8",
    # accelerator_type="NVIDIA_TESLA_T4",
    # accelerator_count=1,
)

print("BatchPredictionJob:", job.resource_name)
