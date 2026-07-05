# System Architecture

**Project Name:** Sentinel AI Platform

**Document Version:** 1.0

**Status:** Draft

**Author:** Rahul Teja B

**Last Updated:** July 2026

---

# Table of Contents

1. Purpose
2. Architecture Goals
3. Architectural Principles
4. High-Level Architecture
5. Platform Layers
6. Application Services
7. AI Agent Layer
8. Shared Tool Layer
9. Knowledge Layer
10. Data Layer
11. Infrastructure Layer
12. Request Flow
13. Technology Stack
14. Scalability
15. Security
16. Future Architecture

---

# 1. Purpose

The purpose of this document is to define the overall architecture of the Sentinel AI Platform.

This document describes:

- Overall system architecture
- Platform components
- Layered architecture
- Service boundaries
- AI agent architecture
- Data flow
- Communication between components
- Security considerations
- Scalability strategy

This architecture serves as the foundation for all future implementation.

---

# 2. Architecture Goals

The platform is designed to achieve the following goals.

- Modular Architecture
- Enterprise Scalability
- Easy Maintenance
- High Reusability
- AI Agent Collaboration
- Human-in-the-Loop Decision Support
- Open Source Deployment
- Local First Development

---

# 3. Architectural Principles

## 3.1 Layered Architecture

Each layer has a single responsibility.

Presentation

↓

API

↓

Application Services

↓

AI Agents

↓

Knowledge

↓

Data

↓

Infrastructure

---

## 3.2 Modular Design

Each component should be independently deployable and maintainable.

---

## 3.3 Single Responsibility

Every module owns one business capability.

Examples:

- Report Service
- Knowledge Service
- Evidence Service
- Policy Service

---

## 3.4 Loose Coupling

Services communicate through APIs instead of directly depending on each other.

---

## 3.5 Human Oversight

AI assists users.

AI never replaces operational decisions.

---

## 3.6 Security First

Every request must pass authentication and authorization before accessing protected resources.

---

# 4. High-Level Architecture

```text
┌────────────────────────────────────────────────────────────┐
│                         USERS                              │
├────────────────────────────────────────────────────────────┤
│ Officers │ Detectives │ Analysts │ Supervisors │ Admins    │
└────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────┐
│                 PRESENTATION LAYER                         │
├────────────────────────────────────────────────────────────┤
│ React │ Web │ Dashboard │ Mobile (Future) │ REST API      │
└────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────┐
│                    API GATEWAY                             │
├────────────────────────────────────────────────────────────┤
│ JWT │ Routing │ Logging │ Validation │ Rate Limiting       │
└────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────┐
│               APPLICATION SERVICES                         │
├────────────────────────────────────────────────────────────┤
│ User │ Reports │ Cases │ Search │ Analytics │ Policies     │
└────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────┐
│                AGENT ORCHESTRATOR                          │
├────────────────────────────────────────────────────────────┤
│ Planner │ Task Router │ Context │ Memory │ Workflow Engine │
└────────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼────────────────────┐
        ▼                  ▼                    ▼
 Knowledge Agent      Report Agent        Policy Agent
 Investigation Agent  Evidence Agent      Analytics Agent
                           │
                           ▼
┌────────────────────────────────────────────────────────────┐
│                  SHARED TOOL LAYER                         │
├────────────────────────────────────────────────────────────┤
│ OCR │ PDF │ Search │ SQL │ Embeddings │ Vector Search      │
└────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────┐
│                  KNOWLEDGE LAYER                           │
├────────────────────────────────────────────────────────────┤
│ Reports │ Policies │ Manuals │ Crime Data │ Evidence       │
└────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────┐
│                     DATA LAYER                             │
├────────────────────────────────────────────────────────────┤
│ PostgreSQL │ FAISS │ Local Storage │ Public Datasets       │
└────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────┐
│               INFRASTRUCTURE LAYER                         │
├────────────────────────────────────────────────────────────┤
│ Docker │ FastAPI │ LangGraph │ Ollama │ GitHub Actions     │
└────────────────────────────────────────────────────────────┘
```

---

# 5. Platform Layers

## 5.1 Presentation Layer

Provides the user interface.

Responsibilities

- Web Application
- Dashboard
- Authentication
- Search
- Report Viewer
- Administration Portal

Technology

- React
- Next.js

---

## 5.2 API Gateway

Acts as the single entry point.

Responsibilities

- Authentication
- Authorization
- Request Routing
- Validation
- Logging
- Rate Limiting

---

## 5.3 Application Services

Business logic lives here.

Services

- User Service
- Report Service
- Case Service
- Policy Service
- Search Service
- Analytics Service

These services coordinate requests before they reach AI agents.

---

## 5.4 AI Agent Layer

The intelligence layer of the platform.

Initial agents include:

- Knowledge Agent
- Report Writing Agent
- Investigation Agent
- Evidence Agent
- Policy Agent
- Analytics Agent

Future agents can be added without modifying existing agents.

---

## 5.5 Shared Tool Layer

Reusable utilities used by all agents.

Examples

- OCR Engine
- PDF Parser
- Embedding Generator
- Vector Search
- SQL Query Engine
- Metadata Service
- File Storage

---

## 5.6 Knowledge Layer

Stores enterprise knowledge.

Contents

- Policies
- Procedures
- Reports
- Public Crime Data
- Evidence Metadata
- Training Manuals

This layer powers Retrieval-Augmented Generation (RAG).

---

## 5.7 Data Layer

Responsible for persistent storage.

Databases

- PostgreSQL
- FAISS Vector Database
- Local File Storage

Future

- Elasticsearch
- Neo4j
- Redis

---

## 5.8 Infrastructure Layer

Provides runtime services.

Components

- Docker
- FastAPI
- LangGraph
- Ollama
- GitHub Actions
- PyTest

---

# 6. Request Flow

Example:

Officer requests

"Draft an incident report."

```
User

↓

Frontend

↓

API Gateway

↓

Report Service

↓

Agent Orchestrator

↓

Knowledge Agent

↓

Report Agent

↓

Policy Agent

↓

Response

↓

Frontend
```

---

# 7. Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | React + Next.js |
| Backend | FastAPI |
| AI Framework | LangGraph |
| LLM | Ollama |
| Models | Llama / Qwen |
| Embeddings | Sentence Transformers |
| Vector Database | FAISS |
| Database | PostgreSQL |
| OCR | Tesseract |
| Authentication | JWT |
| Containerization | Docker |
| Testing | PyTest |
| Version Control | Git |

---

# 8. Scalability Strategy

The architecture supports horizontal scaling.

Future improvements

- Microservices
- Kubernetes
- Redis Cache
- Message Queue
- Cloud Storage
- Distributed Vector Databases

---

# 9. Security Considerations

Authentication

JWT

Authorization

Role-Based Access Control (RBAC)

Audit

Every AI request should be logged.

Future

- Multi-Factor Authentication
- Encryption at Rest
- Encryption in Transit
- Secrets Management

---

# 10. Future Architecture

Future versions may include:

- Mobile Application
- Voice Interface
- GIS Integration
- External RMS Connectors
- CAD Integration
- Multi-Organization Deployment
- Cloud Deployment
- Multi-Tenant Architecture

---

# Summary

Sentinel AI Platform follows a layered enterprise architecture that separates presentation, business services, AI agents, knowledge retrieval, storage, and infrastructure.

This modular approach enables independent development, testing, deployment, and future expansion while maintaining a clean separation of responsibilities.
