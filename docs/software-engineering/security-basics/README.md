# Security Basics

This section is about trust boundaries, misuse resistance, and secure change management.

## Purpose

Use this page to organize security into:
- identity and authorization
- data handling and validation
- secret and credential control
- dependency and SDLC risk

## First Principles

- Security is part of software design, not a final review step.
- Trust boundaries should be explicit in code, config, and operational rules.
- Least privilege is easier to maintain than broad access plus ad hoc exceptions.
- AI-assisted coding increases supply-chain, secret-handling, and unsafe-action risk if boundaries are vague.

## Canonical Modules

- `authn-vs-authz`
- `input-validation-and-output-encoding`
- `secrets-management`
- `least-privilege`
- `dependency-and-supply-chain-risk`
- `secure-sdlc-basics`

## Math And Code

- Math here is limited but real: scope counts, credential age, risk thresholds, and exposure surface all matter.
- Code should default to deny-by-default boundaries, explicit validation, secret isolation, and reviewable privilege changes.

## When To Use What

- Start with identity and trust boundaries before specialized controls.
- Use least privilege and secret isolation early, not after incidents.
- Add supply-chain controls once dependency count and automation increase.
- Treat secure SDLC work as part of delivery quality, not a separate domain.
