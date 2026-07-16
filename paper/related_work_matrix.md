# Sentinel AI – Related Work Matrix

## Purpose

This document summarizes the major frameworks, runtimes, SDKs, and architectural approaches relevant to Sentinel AI.

Its purpose is to support the **Related Work** chapter of the *Sentinel AI Architecture Whitepaper* by identifying:

- The primary goal of each technology
- Architectural strengths
- Architectural scope
- Known limitations
- How Sentinel AI relates to each technology

> **Note:** This matrix is intended for research purposes only. It is not a product comparison or ranking.

---

# Technology Classification

| Category | Technologies |
|------------|--------------|
| Application Frameworks | LangChain |
| Workflow & Runtime Frameworks | LangGraph |
| Multi-Agent Frameworks | CrewAI, AutoGen |
| Enterprise AI SDKs | Semantic Kernel, OpenAI Agents SDK |
| Knowledge Architectures | Retrieval-Augmented Generation (RAG), Agentic RAG |
| Enterprise Platform Architecture | Sentinel AI |

---

# Comparison Matrix

| Technology | Category | Primary Purpose | Strengths | Scope | Limitations | Could Sentinel AI Use It? | Relationship to Sentinel AI |
|------------|----------|----------------|-----------|-------|-------------|---------------------------|-----------------------------|
| **LangChain** | Application Framework | Build LLM-powered applications | Large ecosystem, RAG support, document loaders, tool integrations, vector databases | Application development | Does not define enterprise architecture | ✅ Yes | Provides reusable application components used within the Knowledge and Intelligence Layers. |
| **LangGraph** | Workflow Runtime | Execute long-running stateful AI workflows | Durable execution, graph orchestration, persistence, human-in-the-loop | Workflow runtime | Does not define enterprise platform architecture | ✅ Yes | Can serve as the workflow execution engine inside the Intelligence Layer. |
| **CrewAI** | Multi-Agent Framework | Role-based collaboration between specialized AI agents | Simple role assignment, teamwork, task delegation | Agent collaboration | Limited enterprise infrastructure guidance | ✅ Yes | Can provide collaborative agent execution within the Intelligence Layer. |
| **AutoGen** | Multi-Agent Framework | Conversational collaboration among AI agents | Flexible conversations, code execution, tool use, human interaction | Agent communication | Does not define enterprise architecture | ✅ Yes | Can provide conversational agent coordination inside Sentinel AI. |
| **Semantic Kernel** | Enterprise AI SDK | Build enterprise AI applications using reusable AI plugins and planners | Strong Microsoft ecosystem integration, planners, memory, plugins | Enterprise application SDK | Not a complete enterprise platform architecture | 🟡 Potentially | Can provide SDK components for orchestration and enterprise integrations. |
| **OpenAI Agents SDK** | Enterprise AI SDK | Build AI agents using OpenAI tooling | Modern agent APIs, tool calling, tracing | Agent development | Limited to SDK scope | ✅ Yes | Can be used to implement agents within Sentinel AI. |
| **Agentic RAG** | Knowledge Architecture | Combine retrieval with autonomous reasoning | Grounded responses, planning, retrieval | Knowledge reasoning | Focused on knowledge workflows rather than enterprise architecture | ✅ Yes | Forms part of Sentinel AI's Knowledge Engine architecture. |
| **Sentinel AI** | Enterprise Platform Architecture | Provide a layered enterprise architecture for intelligent systems | Orchestration, Knowledge Engine, shared services, security, operations, governance | Complete enterprise platform | Under active development | — | Defines the overall architecture that can integrate multiple frameworks and technologies. |

---

# Key Observations

## Layer of Abstraction

The technologies reviewed operate at different architectural layers.

```
Foundation Models
        │
        ▼
OpenAI / Anthropic / Google
        │
        ▼
Application Frameworks
        │
        ▼
LangChain
        │
        ▼
Workflow Runtime
        │
        ▼
LangGraph
        │
        ▼
Multi-Agent Frameworks
        │
        ▼
CrewAI / AutoGen
        │
        ▼
Enterprise AI SDKs
        │
        ▼
Semantic Kernel / OpenAI Agents SDK
        │
        ▼
Enterprise Platform
        │
        ▼
Sentinel AI
```

---

## Research Position

Sentinel AI is **not proposed as a replacement** for LangChain, LangGraph, CrewAI, AutoGen, Semantic Kernel, or the OpenAI Agents SDK.

Instead, Sentinel AI defines a **higher-level enterprise platform architecture** capable of integrating these technologies as implementation components where appropriate.

The architectural contribution of Sentinel AI lies in organizing orchestration, knowledge management, shared platform services, infrastructure, security, governance, and operational capabilities into a unified enterprise architecture.

---

# Next Research Topics

- Semantic Kernel
- OpenAI Agents SDK
- Agentic RAG
- Enterprise AI Governance
- Multi-Agent System Surveys
- AI Platform Architecture Patterns

---

# Revision History

| Version | Date | Notes |
|----------|------|-------|
| 0.1 | July 2026 | Initial literature comparison matrix created. |
