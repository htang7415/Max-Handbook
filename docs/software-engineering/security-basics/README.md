# Security Basics

This section is about trust boundaries, misuse resistance, and secure change management.

## Purpose

Use this page to organize security into:
- identity and authorization
- data handling and validation
- secret and credential control
- dependency and SDLC risk
- LLM and agentic workflow risk

## First Principles

- Security is part of software design, not a final review step.
- Trust boundaries should be explicit in code, config, and operational rules.
- Least privilege is easier to maintain than broad access plus ad hoc exceptions.
- AI-assisted coding increases supply-chain, secret-handling, and unsafe-action risk if boundaries are vague.
- Agentic systems add a new trust boundary: untrusted text can influence tool calls, memory, permissions, and external side effects.
- Supply-chain controls should include provenance, dependency review, and automated risk signals instead of relying only on package reputation.
- Agentic security reviews should include goal manipulation, unsafe tool use, overbroad permissions, memory poisoning, and human-approval boundaries.
- Claude Code's security model is a useful reference pattern: read-only by default, explicit permission for edits or shell commands, sandboxing, and write boundaries around the project.
- Frontier-model safety frameworks should influence software threat modeling when model capability, autonomy, or deployment scale increases.

## Decision Table

| Control | Use when | Failure it blocks |
| --- | --- | --- |
| Authn/authz split | A request depends on identity and permission | Confusing who the user is with what they can do |
| Input validation and output encoding | Data crosses a trust boundary | Injection and malformed data propagation |
| Secrets management | Credentials or tokens exist outside one process | Leaks, overbroad access, and rotation gaps |
| Least privilege | A service, person, or agent can perform actions | Excessive blast radius |
| Supply-chain review | Dependencies, generated code, or automation enter delivery | Untrusted code and provenance gaps |
| Secure SDLC | Security checks must survive repeated change | Review-only security that does not scale |

## Workflow

| Step | Action | Output |
| --- | --- | --- |
| 1 | Draw the trust boundary | Untrusted inputs, identities, and side effects |
| 2 | Define allowed actions | Authorization and privilege rules |
| 3 | Validate inputs and protect secrets | Boundary controls |
| 4 | Review dependencies and generated code | Supply-chain evidence |
| 5 | Add security checks to delivery | Repeatable gate |

## Canonical Modules

- `authn-vs-authz`
- `input-validation-and-output-encoding`
- `secrets-management`
- `least-privilege`
- `dependency-and-supply-chain-risk`
- `secure-sdlc-basics`

## Math And Code

- Math level: `low`
- Main quantitative objects: scope counts, credential age, risk thresholds, and exposure surface.
- Code shape: deny-by-default checks, validators, secret-handling policies, and reviewable privilege transitions.

## References

- [Claude Code Security](https://code.claude.com/docs/en/security)
- [Google DeepMind Frontier Safety Framework](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)

## When To Use What

- Start with identity and trust boundaries before specialized controls.
- Use least privilege and secret isolation early, not after incidents.
- Add supply-chain controls such as SLSA-style provenance checks and OpenSSF Scorecard-style repository signals once dependency count and automation increase.
- Treat secure SDLC work as part of delivery quality, not a separate domain.
- Use `docs/ai-agents/guardrails` when model output can trigger tools, connector actions, memory writes, or other external effects.
