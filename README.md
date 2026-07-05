# Sentinel AI 

> **An Open-Source Enterprise Multi-Agent AI Platform for Law Enforcement**

---

## Overview

Sentinel AI Platform is an enterprise-style, multi-agent artificial intelligence platform designed to demonstrate how modern AI systems can support law enforcement operations using open-source technologies.

The platform combines specialized AI agents, Retrieval-Augmented Generation (RAG), workflow orchestration, and a unified knowledge layer to assist with report drafting, information retrieval, investigation support, policy lookup, evidence organization, and operational analytics.

This project is built as a software engineering portfolio and research project using publicly available datasets and open-source tools.

---

## Vision

Law enforcement organizations often use multiple disconnected systems for:

* Incident Reports
* Policies and Procedures
* Evidence Management
* Investigations
* Crime Analytics
* Internal Knowledge
* Document Search

Sentinel AI brings these capabilities together into a single AI-powered workspace where specialized agents collaborate to assist officers, investigators, analysts, supervisors, and administrators.

The platform is designed to **assist personnel**, not replace human judgment or operational decision-making.

---

# High-Level Architecture

```text
                                      USERS
──────────────────────────────────────────────────────────────────────────────
 Patrol Officers | Detectives | Analysts | Supervisors | Administrators
──────────────────────────────────────────────────────────────────────────────
                                      │
                                      ▼

                           PRESENTATION LAYER
──────────────────────────────────────────────────────────────────────────────
 React / Next.js Web Application
 Mobile Application (Future)
 Desktop Dashboard (Future)
 REST API
──────────────────────────────────────────────────────────────────────────────
                                      │
                                      ▼

                           API GATEWAY
──────────────────────────────────────────────────────────────────────────────
Authentication
Authorization
Session Management
Rate Limiting
Logging
Routing
API Versioning
──────────────────────────────────────────────────────────────────────────────
                                      │
                                      ▼

                     AGENT ORCHESTRATION LAYER
──────────────────────────────────────────────────────────────────────────────
Planner

Workflow Engine

Task Manager

Context Manager

Memory Manager

Human Approval Manager

Result Aggregator
──────────────────────────────────────────────────────────────────────────────
             │
─────────────┼───────────────────────────────────────────────────────────────
             │
             ▼

                    SPECIALIZED AI AGENTS

Knowledge Agent

Report Writing Agent

Investigation Agent

Evidence Agent

Policy Agent

Analytics Agent

Dispatch Support Agent (Future)

Supervisor Review Agent (Future)
             │
─────────────┼───────────────────────────────────────────────────────────────
             │
             ▼

                         SHARED TOOL LAYER
──────────────────────────────────────────────────────────────────────────────
Vector Search

Document Parser

OCR

Policy Search

Crime Dataset Search

Evidence Search

Timeline Builder

Geospatial Search

SQL Query Engine

Metadata Service
──────────────────────────────────────────────────────────────────────────────
             │
             ▼

                     KNOWLEDGE & DATA LAYER
──────────────────────────────────────────────────────────────────────────────
Public Crime Datasets

Department Policies

Incident Reports

Evidence Metadata

Training Manuals

Knowledge Base

FAISS Vector Database

PostgreSQL

Document Store
──────────────────────────────────────────────────────────────────────────────
             │
             ▼

                    INFRASTRUCTURE LAYER
──────────────────────────────────────────────────────────────────────────────
FastAPI

LangGraph

Ollama

Llama / Qwen

Sentence Transformers

Docker

GitHub Actions

PyTest

Logging

Monitoring
──────────────────────────────────────────────────────────────────────────────
```

---

# Core AI Agents

### Knowledge Agent

Provides enterprise search across documents, policies, reports, manuals, and structured datasets.

---

### Report Writing Agent

Assists officers by drafting reports from structured inputs, notes, and retrieved context.

---

### Investigation Agent

Supports investigators by organizing case information, building timelines, identifying related incidents, and summarizing evidence.

---

### Evidence Agent

Indexes evidence metadata, organizes supporting materials, and enables efficient retrieval.

---

### Policy Agent

Retrieves and summarizes departmental policies, procedures, and relevant public regulations.

---

### Analytics Agent

Generates dashboards and analytical summaries using public crime and operational datasets.

---

# Technology Stack

| Layer            | Technology            |
| ---------------- | --------------------- |
| Frontend         | React + Next.js       |
| Backend          | FastAPI               |
| Agent Framework  | LangGraph             |
| Local LLM        | Ollama                |
| Models           | Llama, Qwen, Mistral  |
| Embeddings       | Sentence Transformers |
| Vector Database  | FAISS                 |
| Database         | PostgreSQL            |
| Authentication   | JWT                   |
| OCR              | Tesseract             |
| PDF Processing   | PyMuPDF               |
| Testing          | PyTest                |
| Containerization | Docker                |
| Version Control  | Git + GitHub          |

---

# Repository Structure

```text
sentinel-ai-platform/

backend/
frontend/
docs/
datasets/
tests/
scripts/
docker/
.github/

README.md
LICENSE
.gitignore
```

---

# Development Roadmap

## Phase 1 — Foundation

* Project Architecture
* Base Agent Framework
* Knowledge Layer
* Local Development Environment

## Phase 2 — Core Agents

* Knowledge Agent
* Report Writing Agent
* Investigation Agent
* Evidence Agent
* Policy Agent

## Phase 3 — Platform

* Agent Orchestrator
* Workflow Engine
* Shared Memory
* Evaluation Framework

## Phase 4 — User Experience

* Web Dashboard
* Authentication
* User Management
* Administrative Portal

## Phase 5 — Production Readiness

* Monitoring
* Audit Logs
* Docker Deployment
* CI/CD
* Documentation

---

# Documentation

Detailed technical documentation will be maintained in the `/docs` directory, including:

* Product Vision
* System Architecture
* Agent Framework
* Individual Agent Designs
* API Specifications
* Database Design
* Workflow Definitions
* Deployment Guide

---

# Project Status

🚧 **Currently in Active Development**

The project is being built incrementally following an enterprise software development lifecycle, beginning with architecture and documentation before implementation.

---

# Disclaimer

Sentinel AI Platform is an independent open-source engineering project created for educational, research, and portfolio purposes.

It uses publicly available datasets and open-source technologies. The project is **not affiliated with, endorsed by, or deployed by the Chicago Police Department or any other law enforcement agency**.

The platform is intended to demonstrate enterprise AI architecture and decision-support workflows. It is not designed to make autonomous law enforcement decisions.

---

# License

MIT License
