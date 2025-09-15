# AWS Bedrock Quickstart (README snippet)

## Prereqs
- AWS account with Bedrock access in your region (enable model access in console).
- AWS CLI: `aws configure` (with region, keys)  
- Python 3.9+, `pip install boto3`

## Invoke a model
```bash
export AWS_REGION=us-east-1
export BEDROCK_MODEL_ID=anthropic.claude-3-5-sonnet-20240620-v1:0   # example, change if needed
python assets/aws/bedrock_invoke_text.py
```

## Call an Agent
```bash
export AWS_REGION=us-east-1
export BEDROCK_AGENT_ID=YOUR_AGENT_ID
export BEDROCK_AGENT_ALIAS_ID=YOUR_ALIAS_ID
python assets/aws/bedrock_agent_invoke.py
```

## Serverless API pattern
- API Gateway → Lambda → Bedrock Runtime
- Store docs in S3; use **Textract** → **Knowledge Bases** for RAG
- Observe with **CloudWatch** logs/metrics
