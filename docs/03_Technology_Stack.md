# Technology Stack

**Project Name:** Sentinel AI Platform

**Document Version:** 1.0

**Status:** Draft

**Author:** Rahul Teja B

**Last Updated:** July 2026

---

# Table of Contents

1. Purpose
2. Technology Selection Principles
3. Technology Stack Overview
4. Frontend
5. Backend
6. AI & LLM Stack
7. Data Layer
8. Search & Retrieval
9. Infrastructure
10. Development Tools
11. Future Technologies
12. Summary

---

# 1. Purpose

This document defines the official technology stack for the Sentinel AI Platform.

Each technology has been selected based on:

- Open-source availability
- Enterprise adoption
- Scalability
- Developer productivity
- Community support
- Local deployment capability

The stack may evolve over time as the project grows.

---

# 2. Technology Selection Principles

Every technology should satisfy the following criteria.

## Open Source First

Whenever possible, use open-source software.

---

## Local Development

The complete platform should run on a local machine.

---

## Enterprise Ready

Technologies should support production deployments.

---

## Modular

Every component should be replaceable.

---

## Community Support

Preference is given to technologies with strong documentation and active communities.

---

# 3. Technology Stack Overview

| Layer | Technology |
|--------|------------|
| Frontend | React + Next.js |
| Backend | FastAPI |
| Programming Language | Python |
| AI Framework | LangGraph |
| LLM Runtime | Ollama |
| Initial Models | Llama 3.x / Qwen |
| Embeddings | Sentence Transformers |
| Vector Database | FAISS |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT |
| OCR | Tesseract OCR |
| PDF Processing | PyMuPDF |
| Testing | PyTest |
| Package Manager | Poetry |
| Containerization | Docker |
| Version Control | Git |
| CI/CD | GitHub Actions |

---

# 4. Frontend

## Selected Technology

- React
- Next.js
- TypeScript

### Why?

- Component-based architecture
- Large ecosystem
- Excellent performance
- Enterprise adoption
- Server-side rendering support

### Alternatives Considered

- Angular
- Vue.js
- Svelte

### Decision

React provides the best balance between flexibility, community support, and enterprise adoption.

---

# 5. Backend

## Selected Technology

FastAPI

### Why?

- High performance
- Automatic OpenAPI documentation
- Native async support
- Type validation using Pydantic
- Excellent AI ecosystem compatibility

### Alternatives Considered

- Flask
- Django
- Express.js

### Decision

FastAPI is well suited for AI APIs and modern microservices.

---

# 6. AI Framework

## Selected Technology

LangGraph

### Why?

- Designed for multi-agent systems
- Supports long-running workflows
- Built-in state management
- Human-in-the-loop workflows
- Graph-based orchestration

### Alternatives Considered

- CrewAI
- AutoGen
- Semantic Kernel

### Decision

LangGraph provides greater flexibility for complex enterprise workflows.

---

# 7. Large Language Models

## Runtime

Ollama

### Why?

- Local execution
- Open-source
- Easy model management
- No cloud dependency

---

## Initial Models

- Llama 3.x
- Qwen
- Mistral

Future support

- GPT
- Claude
- Gemini

The architecture allows models to be replaced without changing application logic.

---

# 8. Embeddings

## Selected Technology

Sentence Transformers

### Why?

- Open-source
- Strong retrieval quality
- Fast inference
- Local execution

---

# 9. Vector Database

## Selected Technology

FAISS

### Why?

- Lightweight
- Open-source
- Excellent local performance
- Widely used for semantic search

### Alternatives Considered

- Pinecone
- Chroma
- Milvus
- Weaviate

### Decision

FAISS is ideal for local development and portfolio projects.

---

# 10. Relational Database

## Selected Technology

PostgreSQL

### Why?

- Enterprise reliability
- ACID compliance
- Excellent SQL support
- Strong indexing
- JSON support

### Alternatives Considered

- MySQL
- SQLite
- MongoDB

### Decision

PostgreSQL provides flexibility for structured enterprise data.

---

# 11. Object Relational Mapping

## Selected Technology

SQLAlchemy

### Why?

- Mature ecosystem
- Database abstraction
- Easy migrations
- Enterprise adoption

---

# 12. Authentication

## Selected Technology

JWT

Future

OAuth2

SSO

Microsoft Entra ID

---

# 13. OCR

## Selected Technology

Tesseract OCR

### Why?

- Open-source
- Local execution
- Mature project

---

# 14. Document Processing

## Selected Technology

PyMuPDF

Responsibilities

- PDF Parsing
- Text Extraction
- Metadata Extraction

---

# 15. Testing

## Selected Technology

PyTest

Future

- Integration Tests
- Performance Tests
- Agent Evaluation Framework

---

# 16. Infrastructure

## Containerization

Docker

---

## CI/CD

GitHub Actions

---

## Environment Management

Poetry

---

## Logging

Python Logging

Future

OpenTelemetry

---

# 17. Future Technologies

Possible future additions include:

- Kubernetes
- Redis
- Neo4j
- Elasticsearch
- RabbitMQ
- Kafka
- MLflow
- Prometheus
- Grafana

---

# 18. Technology Replacement Strategy

Every technology is selected behind an abstraction layer.

Example

AI Models

```

Application

↓

Model Adapter

↓

Llama

GPT

Claude

Gemini

```

The application should not depend directly on any specific model.

This strategy enables future migration without large-scale code changes.

---

# 19. Summary

Sentinel AI Platform is built using modern, open-source technologies that support enterprise software architecture while remaining fully deployable on local infrastructure.

The architecture emphasizes modularity, maintainability, and future scalability, allowing individual technologies to evolve independently without requiring major redesigns.
