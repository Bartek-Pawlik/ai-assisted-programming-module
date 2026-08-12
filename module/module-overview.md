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

## Currency — reviewed August 2026

This module's material was first written in 2025. That is a long time in
this field, so the content carries an explicit position on where things
now stand rather than quietly ageing:

- **"Understand every line" is retired as a rule.** Roughly 92% of US
  developers use AI coding tools daily, under a third trust the output,
  and fewer than half always review before committing. The module teaches
  the honest version instead: the unit of review moved from the line to
  the behaviour, and the guarantee moved from your eyes to your tests.
  Accountability did not move anywhere.
- **RAG is not dead, but it is no longer the default.** Long context
  handles small corpora better and more cheaply; retrieval earns its place
  on scale, cost, freshness and citation. Week 4 now teaches the decision,
  not just the pipeline.
- **Prompt engineering is being subsumed by context engineering.** Week 3
  keeps the SPEC drills — they are the practisable half — and adds the
  question that matters more now: *is this wrong because I asked badly, or
  because it doesn't know something?*
- **MCP became a standard and then changed shape.** The 2026-07-28
  specification removed the `initialize` handshake and session header for
  a stateless core. Week 5 teaches both models and why the change happened.
- **Spec-driven development is the counter-trend to vibe coding**, and
  week 11 now runs them against each other rather than demonstrating one.
- **Security of AI-generated code** enters through week 11's lab, where
  students audit an app they vibe-coded. Around 45% of AI-generated
  samples carry an OWASP Top-10 vulnerability, so the exercise reliably
  finds something.

Percentages here come from 2026 industry surveys of varying rigour. They
are taught as indicative of direction, and that caveat is taught with
them.

## Weekly topics

| Week | Topic | What it covers | Lab |
|---|---|---|---|
| 1 | Module Introduction | How the module runs, assessment, tooling setup | — |
| 2 | AIAP Overview | What AI-assisted programming is; the landscape and its limits | [setup](../labs/setup/) |
| 3 | Prompting &amp; Context Engineering | SPEC prompts, constraints and non-goals, personas, chain-of-thought, few-shot — then the shift from *how you ask* to *what you put in front of the model* | [prompting](../labs/prompting/) |
| 4 | RAG &amp; Retrieval Strategy | Chunking, embeddings, vector search, grounded answers — and when long context beats retrieval outright | [rag](../labs/rag/) |
| 5 | MCP | Model Context Protocol: servers, clients, tools, and the 2026 move to a stateless protocol core | [mcp](../labs/mcp/) |
| 6 | Agents | Ask / edit / agent modes; autonomy, review loops, cloud agents | [agents](../labs/agents/) |
| — | *Reading week* | October bank-holiday week — revision for MCQ 1 | — |
| 7 | **MCQ 1 (20%)** | Assessment on weeks 1–6, lectures and labs | — |
| 8 | CLI Coding Agents | Terminal-based agents: Copilot CLI, Gemini CLI, and how they differ from in-editor tools | [cli-coding-agents](../labs/cli-coding-agents/) |
| 9 | BaaS | Backend-as-a-service: Firestore, auth, and an API an AI-built frontend can call | [baas](../labs/baas/) |
| 10 | CI/CD | Pipelines with GitHub Actions, and putting AI inside them (review, triage) | [cicd](../labs/cicd/) |
| 11 | Vibe Coding &amp; Spec-Driven Development | Prompt-first tools and the backlash against them; comprehension debt, the security cost, and when a spec beats a prompt | [vibe-coding](../labs/vibe-coding/) |
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
