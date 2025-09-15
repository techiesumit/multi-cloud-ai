# Vertex AI Vector Search quickstart (SDK)
# Requires: pip install google-cloud-aiplatform
from google.cloud import aiplatform

PROJECT_ID = "YOUR_PROJECT_ID"
REGION = "us-central1"
DISPLAY_NAME = "vs-demo-index"
DIMENSIONS = 768  # your embedding size

aiplatform.init(project=PROJECT_ID, location=REGION)

# Create index (Tree-AH example)
index = aiplatform.MatchingEngineIndex.create_tree_ah_index(
    display_name=DISPLAY_NAME,
    contents_delta_uri="gs://YOUR_BUCKET/embeddings/",  # vectors & metadata
    dimensions=DIMENSIONS,
)

# Create endpoint & deploy
endpoint = aiplatform.MatchingEngineIndexEndpoint.create(
    display_name=f"{DISPLAY_NAME}-endpoint",
    public_endpoint_enabled=True,
)
endpoint.deploy_index(index=index, deployed_index_id=f"{DISPLAY_NAME}-deployed")

print("Index:", index.resource_name)
print("IndexEndpoint:", endpoint.resource_name)
