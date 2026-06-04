# Assessments

Use this page to check whether the track is changing how you reason about software, not just increasing the number of modules you have read.

## Decision Table

| Readiness area | You are ready when | Weak signal |
| --- | --- | --- |
| Contracts | You can name caller expectations and compatibility rules | You describe only implementation details |
| Tests | You can pick the smallest useful verification set | You add broad tests without knowing the invariant |
| Security | You can draw the trust boundary and privilege rule | You treat security as a final checklist |
| Operations | You can name the production signal and rollback trigger | You cannot say what should page or rollback |
| AI-assisted work | You can review generated code against specs and failure modes | You trust the diff because it looks plausible |

## Workflow

| Step | Action | Output |
| --- | --- | --- |
| 1 | Pick one proposed change or module | Assessment target |
| 2 | Answer contract, failure, test, signal, rollback, and AI-impact questions | Readiness score |
| 3 | Identify the weakest answer | Next module or section to revisit |
| 4 | Repeat on a capstone scenario | End-to-end evidence |

## Section Checks

- Tooling: Can you explain what spec, review, and CI gates are required before AI-generated code should merge?
- APIs: Can you design a mutating endpoint with schema evolution, idempotency, and retry behavior that stays safe under duplicates?
- Testing: Can you name the smallest useful test portfolio for a risky change and justify why each test exists?
- Security Basics: Can you distinguish authn, authz, least privilege, secrets handling, and supply-chain risk in one system?
- Concurrency: Can you explain whether a workflow should use a queue, a lock, or an idempotent consumer?
- Observability: Can you pick an SLI, define an SLO, and say when humans should page vs ticket?
- Reliability: Can you describe the rollback path before rollout starts?
- Performance: Can you explain the latency budget and the main bottleneck before proposing caching?
- System Design: Can you justify service boundaries and state ownership without hand-waving?
- Platform And Delivery: Can you explain the blast radius and change budget of a rollout?

## Capstone Readiness

You are ready for capstones when you can do all of these:

- write a short spec before implementation
- identify the contract and invariant of the change
- choose a focused verification set
- name the key production signal
- describe the rollback path
- explain the trust boundary

## Graduation Check

The track is working if you can review a proposed change and answer these six questions quickly:

1. What is the contract?
2. What can fail?
3. How is it tested?
4. What will we observe in production?
5. What is the rollback path?
6. What changes because AI helped write it?

## Weak Signals

You probably need another pass through the foundations if:

- you optimize implementation before clarifying contracts
- you add retries without thinking about idempotency or overload
- you trust generated code because it looks plausible
- you cannot say what should trigger rollback
