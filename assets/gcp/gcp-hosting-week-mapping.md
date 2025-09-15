# GCP Model Hosting — Mapping to Your 20‑Week Plan

**Generated:** 2025-09-15  
**Tracks covered:** Vertex AI Predictions (online & batch), Vector Search, BigQuery ML, Cloud Run (GPU), GKE

---

## Weeks 9–12 (GCP / Vertex AI)
- **Week 9 — Fundamentals + Notebooks → Vertex AI Predictions (Online)**  
  *Deploy a scikit‑learn or AutoML model to a managed **Endpoint** for low‑latency inference.*  
  Tasks: create a Model, create Endpoint, deploy Model, call REST/gRPC.

- **Week 10 — Pipelines & MLOps → Pipelines + Model Registry**  
  *Track model versions in **Model Registry**, promote the best to **Endpoint**; automate with Pipelines.*

- **Week 11 — LLMs + Vector Search → GenAI + RAG**  
  *Use **Vertex AI Generative** APIs for serverless LLMs; add **Vector Search** for retrieval; evaluate prompts.*

- **Week 12 — BigQuery ML at Scale → SQL models + Hosting**  
  *Train with **BigQuery ML** and **register** models in **Model Registry**; invoke via **ML.PREDICT** or deploy for online predictions.*

## Weeks 17–20 (Capstone)
- **Week 17 — Design**: Choose hosting per component  
  - Tabular API → Vertex **Endpoint**  
  - LLM API → Vertex **Generative Models** or **Cloud Run (GPU)** (for OSS LLMs)  
  - RAG store → **Vertex AI Vector Search** (or BigQuery Vector Search)  
  - Batch scoring → **Batch Prediction Job** (Vertex) or scheduled **BQML**

- **Week 18 — Build/Observe**: Add **Cloud Logging/Monitoring**, request logs, latency SLIs, cost dashboards.  
- **Week 19 — Portfolio**: Diagram, ADRs, README with reproducible deploy steps.  
- **Week 20 — Interview**: Prepare trade‑off answers (Endpoint vs Cloud Run vs GKE, Vector Search vs RAG Engine, etc.).

---

## Quick choice guide
- **I need simplest hosting** → Vertex **Online Predictions** (Endpoint).  
- **I need serverless LLM API** → Vertex **Generative AI**.  
- **I need OSS runtime or libs (vLLM/Triton)** → **Cloud Run (GPU)**; heavy control → **GKE**.  
- **SQL‑first pipelines** → **BigQuery ML** (+ Model Registry if you want online serving).  
- **RAG** → **Vector Search** (+ Embeddings) next to your hosted model.
