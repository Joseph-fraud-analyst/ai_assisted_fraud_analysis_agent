# AI Agent Evaluation and Safety Test Suite — Demonstration Project

## Purpose
A small test suite for evaluating a fraud-analysis assistant's reliability and safety before any real-world use. The suite tests whether a candidate output:
- distinguishes observed indicators from confirmed facts;
- admits uncertainty and missing information;
- avoids unsupported fraud conclusions;
- resists instructions embedded in untrusted case notes;
- avoids exposing sensitive data unnecessarily;
- keeps consequential decisions with a human reviewer;
- returns a valid, auditable structure.

**Demonstration only.** The included candidate system is a local mock function; this project does not call an external AI model. It tests safety properties of outputs and input handling, not the full capabilities of a production model.

## Run
Requires Python 3.10+; no third-party dependencies.

```bash
python -m unittest discover -s tests -v
python src/run_suite.py
```

The test runner prints a pass/fail summary and writes `output/evaluation_results.json`.

## Test categories
1. Incomplete evidence
2. Conflicting history
3. Prompt injection in untrusted notes
4. Sensitive-data exposure
5. Unsupported claims
6. Ambiguous instructions
7. Human-review and automated-action boundaries
8. Schema and auditability

## Limitations
A passing local suite is not a certification, independent audit, or proof that an AI model is safe. Before use with a real model, add model-specific adversarial tests, privacy review, representative data, versioned evaluation sets, and human sign-off.
