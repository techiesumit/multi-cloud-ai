# Vertex AI Online Predictions — create endpoint & deploy model
# Requires: pip install google-cloud-aiplatform
from google.cloud import aiplatform

PROJECT_ID = "YOUR_PROJECT_ID"
REGION = "us-central1"
MODEL_ID = "YOUR_MODEL_ID"  # in this region
ENDPOINT_NAME = "demo-endpoint"
DEPLOYED_MODEL_NAME = "demo-deployed"

aiplatform.init(project=PROJECT_ID, location=REGION)

# Create endpoint (idempotent find-or-create)
eps = aiplatform.Endpoint.list(filter=f'display_name="{ENDPOINT_NAME}"')
endpoint = eps[0] if eps else aiplatform.Endpoint.create(display_name=ENDPOINT_NAME)

# Deploy a model (simple: CPU, autoscaling 1-2)
endpoint.deploy(
    model=MODEL_ID,
    deployed_model_display_name=DEPLOYED_MODEL_NAME,
    traffic_percentage=100,
    min_replica_count=1,
    max_replica_count=2,
    # For GPU add:
    # machine_type="n1-standard-8",
    # accelerator_type="NVIDIA_TESLA_T4",
    # accelerator_count=1,
)

print("Endpoint resource:", endpoint.resource_name)
print("Predict URL region:", REGION)
