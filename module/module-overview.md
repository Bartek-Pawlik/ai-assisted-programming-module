# Module overview

**AI-Assisted Programming** — Atlantic Technological University, semester 1.
A 5-credit module: 100–125 hours across 12 teaching weeks, of which 36 are
contact hours (1 hour lecture + 2 hour lab per week).

## The argument

The module is not a tour of AI coding tools. Tools change every few months
and the ones taught in week 11 will not be the ones a graduate uses in
2028. What transfers is the judgement: how to direct an assistant, how to
supply it with the right context, and how to evaluate what comes back.

So the shape is: **talk to it well** (prompting) → **give it the right
context** (RAG, MCP) → **let it act** (agents, CLI agents) → **ship what
it helps you build** (BaaS, CI/CD) → **know when to trust the vibe**
(vibe coding).

## Weekly topics

| Week | Topic | What it covers | Lab |
|---|---|---|---|
| 1 | Module Introduction | How the module runs, assessment, tooling setup | — |
| 2 | AIAP Overview | What AI-assisted programming is; the landscape and its limits | [setup](../labs/setup/) |
| 3 | Prompting | SPEC prompts, constraints and non-goals, personas, chain-of-thought, few-shot formatting | [prompting](../labs/prompting/) |
| 4 | RAG | Retrieval-augmented generation: chunking, embeddings, vector search, grounded answers | [rag](../labs/rag/) |
| 5 | MCP | Model Context Protocol: servers, clients, tools, and wiring an assistant to real systems | [mcp](../labs/mcp/) |
| 6 | Agents | Ask / edit / agent modes; autonomy, review loops, cloud agents | [agents](../labs/agents/) |
| — | *Reading week* | October bank-holiday week — revision for MCQ 1 | — |
| 7 | **MCQ 1 (20%)** | Assessment on weeks 1–6, lectures and labs | — |
| 8 | CLI Coding Agents | Terminal-based agents: Copilot CLI, Gemini CLI, and how they differ from in-editor tools | [cli-coding-agents](../labs/cli-coding-agents/) |
| 9 | BaaS | Backend-as-a-service: Firestore, auth, and an API an AI-built frontend can call | [baas](../labs/baas/) |
| 10 | CI/CD | Pipelines with GitHub Actions, and putting AI inside them (review, triage) | [cicd](../labs/cicd/) |
| 11 | Vibe Coding | Prompt-first development tools; where the approach works and where it fails | [vibe-coding](../labs/vibe-coding/) |
| 12 | **MCQ 2 (20%)** | Assessment on weeks 8–11, lectures and labs | — |

The **[project](../project/brief.md)** (60%) runs across the whole
semester and is due at the end of week 12.

## Calendar

The semester is derived, not stored: reading week is the week of the Irish
October bank holiday (the last Monday of October), week 1 begins six weeks
before it, and six teaching weeks sit each side. Nothing needs editing
year to year.

## Learning outcomes

1. **Identify and evaluate** the capabilities of AI-powered coding tools —
   generation, completion, and debugging assistance.
2. **Integrate** AI-based tools into a practical software development
   workflow, demonstrating their use in real coding scenarios.
3. **Critically analyse** the benefits and limitations of AI coding
   assistance, considering code quality, over-reliance, and potential
   biases.
4. **Explore** emerging trends in AI-assisted programming.

Outcome 3 is why the assessment looks the way it does: the MCQs are sat in
person, and the project is presented and defended.
