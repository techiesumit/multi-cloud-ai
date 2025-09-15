# Oracle Generative AI Quickstart (README snippet)

## Prereqs
- OCI account, tenancy/compartment, and region
- Auth: use OCI Request Signing or a token; install OCI CLI if preferred

## Minimal REST call (template)
```bash
export ORACLE_GENAI_ENDPOINT="https://generativeai.<region>.oci.oraclecloud.com/2024-xx-xx/actions/generateText"
export ORACLE_API_KEY="REPLACE_WITH_TOKEN_OR_USE_SIGNED_REQUESTS"

python assets/oracle/oracle_genai_invoke_template.py
```

## RAG & In‑DB ML
- Store data in Autonomous DB; use **Select AI** for vector/embedding queries
- Train/score via **Oracle Machine Learning** (OML) close to data
- Observe with **OCI Logging/Monitoring**
