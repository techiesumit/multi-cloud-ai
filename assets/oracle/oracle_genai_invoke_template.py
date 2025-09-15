# Oracle Generative AI — REST call template (placeholder)
# Fill TENANCY/COMPARTMENT/ENDPOINT and auth headers (OCI Signature or token).
import requests, os

endpoint = os.environ.get("ORACLE_GENAI_ENDPOINT", "https://generativeai.<region>.oci.oraclecloud.com/2024-xx-xx/actions/generateText")
api_key = os.environ.get("ORACLE_API_KEY")  # placeholder if using token-based auth

headers = {
    "Content-Type": "application/json",
    # NOTE: For production use, sign requests with OCI Signature (or use official SDK when available).
    "Authorization": f"Bearer {api_key or 'REPLACE_WITH_VALID_TOKEN'}"
}

payload = {
  "input": "Write a 2-sentence summary about Retrieval-Augmented Generation."
}

resp = requests.post(endpoint, json=payload, headers=headers, timeout=60)
print(resp.status_code, resp.text[:500])
