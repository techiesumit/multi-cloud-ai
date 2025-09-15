# Call an Amazon Bedrock Agent (skeleton)
# pip install boto3
import boto3, os, uuid, json

region = os.environ.get("AWS_REGION", "us-east-1")
agent_id = os.environ.get("BEDROCK_AGENT_ID", "YOUR_AGENT_ID")
alias_id = os.environ.get("BEDROCK_AGENT_ALIAS_ID", "TSTALIASID")  # e.g., "$LATEST" or an alias
session_id = str(uuid.uuid4())

client = boto3.client("bedrock-agent-runtime", region_name=region)

input_text = "What's our refund policy?"
resp = client.invoke_agent(
    agentId=agent_id,
    agentAliasId=alias_id,
    sessionId=session_id,
    inputText=input_text
)

# Streaming responses are delivered via event stream; this is a placeholder to show call params only.
print("Invoked agent session:", session_id)
