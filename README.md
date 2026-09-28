# ReAct Agent Reasoning & Interleaved Tool Engine Skill

High-efficiency, zero-dependency Python implementation of the **ReAct (Reasoning + Acting)** paradigm for autonomous LLM agents.

## Features
- **Interleaved Reasoning & Tool Execution**: Synergizes step-by-step thinking traces with explicit action invocations.
- **Persistent Scratchpad History**: Auditable trajectory tracking across multi-turn interactions.
- **Zero External Dependencies**: Pure Python standard library.
- **Native MCP Protocol**: JSON-RPC 2.0 stdio server compatible with Claude Desktop, Cursor, and Windsurf.

## Architecture
```mermaid
graph TD
    UserQuery["User Request"] --> ReActLoop["ReAct Controller"]
    ReActLoop --> Thought["1. Thought (Internal Reasoning)"]
    Thought --> Action["2. Action (Tool Call Selection)"]
    Action --> Env["3. Tool / Environment"]
    Env --> Obs["4. Observation Feedback"]
    Obs --> Scratchpad["Append to Scratchpad"]
    Scratchpad --> Check{"Goal Reached?"}
    Check -- No --> Thought
    Check -- Yes --> Finish["FINISH -> Final Answer"]
```
