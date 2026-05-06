---
trigger: always_on
description: Workspace context and technology routing. Check package.json to load relevant skills.
---

## Workspace Context

**Before any task**: read the root `package.json` to determine the technologies and versions being used.

### Skill Routing

| Signal in package.json | Skill to load |
|---|---|
| `react` or `vite` | `vercel-react-best-practices`, `vercel-composition-patterns`, `react-manifesto`, `coding-conventions` |
| `tailwindcss ^4` or `@tailwindcss/postcss` | `tailwind-v4` |