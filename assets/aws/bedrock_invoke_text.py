# Invoke an LLM on Amazon Bedrock (text generation)
# pip install boto3
import json, boto3, os

region = os.environ.get("AWS_REGION", "us-east-1")
model_id = os.environ.get("BEDROCK_MODEL_ID", "anthropic.claude-3-5-sonnet-20240620-v1:0")  # example id; replace as needed

brt = boto3.client("bedrock-runtime", region_name=region)

prompt = "Write a 2-sentence summary about Retrieval-Augmented Generation."
body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 256,
    "messages": [{"role":"user","content":[{"type":"text","text": prompt}]}]
}

resp = brt.invoke_model(
    modelId=model_id,
    body=json.dumps(body),
    accept="application/json",
    contentType="application/json"
)

out = json.loads(resp["body"].read())
print(json.dumps(out, indent=2))
