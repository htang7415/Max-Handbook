---
name: code-lab-web-sync
description: Rules and workflow for keeping Code Lab content in sync with the TypeScript Next.js site via a content indexer, and deploying on Vercel.
license: Complete terms in LICENSE
---

# Code Lab Web Sync

Use this skill whenever changing:
- `docs/**`
- `web/` Next.js app or content-indexer

## Goal

Make the website a clean view of the repository:
- No duplicated source-of-truth content
- Stable URLs from `track/topic/slug`
- Fast builds and predictable deploy on Vercel