---
name: react-manifesto
description: Foundational principles, core stack (React, Vite, Tailwind), and operational workflow for AI Agent development in React projects. Use when establishing project methodology or defining development standards for React/Vite.
proactive: match
match:
  - "vite"
  - "react"
  - "react manifesto"
  - "react development standards"
category: Architecture
human_reviewed: false
---

# React AI Agent Manifesto

This manifesto defines the foundational principles, core stack, and operational workflow for AI Agent development specifically for **React (Vite)** environments.

## Quick Start

| Rule | ✅ Correct | ❌ Incorrect |
|------|-----------|-------------|
| Component Type | Functional Components by default | Class Components |
| Interactivity | Standard React Hooks | Mutating state directly |
| Styling | Tailwind CSS utilities + design tokens | CSS Modules (unless existing), Inline styles |
| Data Fetching | React Query / Fetch API in `useEffect` | Blocking renders with synchronous fetches |
| State | Zustand or React Context | Prop drilling or over-using global state |
| Testing | Vitest/Jest + Playwright | No tests |

## 🏗️ Core Foundation Stack

This stack profile assumes a modern React (Vite) setup.

### Stack Profile: Modern React

| Category | Technology | Notes |
|:---|:---|:---|
| **Framework** | React 18/19 (Vite) | Fast refresh, optimized build |
| **Language** | TypeScript 5 | Strict mode enabled |
| **Styling** | Tailwind CSS v3/v4 | Mobile-first, utility-first |
| **State** | Zustand / Context | Minimize global state |
| **Data Fetching** | Fetch API / React Query | Standard API requests |
| **Forms** | React Hook Form + Zod | Type-safe validation |
| **Testing** | Vitest + Playwright | TDD approach |

### Principles for AI Agents:
- **Component-First**: Build modular, reusable functional components. Keep components focused on a single responsibility.
- **Type Safety**: No `any`. Use Zod for runtime validation (API responses, Form data).
- **Performance**: Optimize images and assets using standard Vite practices and lazy loading (`React.lazy`).
- **SEO**: Use React Helmet or document title API for meta tags if required, though standard SPAs may have limited SEO.

## 🗺️ Development Workflow

| Phase | Focus | Deliverables |
| :--- | :--- | :--- |
| **1. Discovery** | Identify Vite config, check `package.json` | Technology confirmation |
| **2. Architecture** | Define Component hierarchy and state | Component hierarchy diagram |
| **3. Implementation** | Clean code, hooks, and shared components | Feature-complete components |
| **4. Optimization** | Bundle analysis, image optimization | Optimized build size |
| **5. Verification** | Tests and quality audit | Green test suite, a11y passed |

## 🕹️ Applicability & Governance

1. **Mandatory Adoption**: This manifesto applies to all tasks involving React architecture or feature implementation.
2. **Standardization**: Follow the established folder structure (e.g., `src/components/`, `src/hooks/`, `src/utils/`).
3. **No Placeholders**: Agents must ship production-ready code with proper error handling and loading states.
4. **Accessibility (a11y)**: Use semantic HTML and ARIA attributes. Test with screen readers if possible.
