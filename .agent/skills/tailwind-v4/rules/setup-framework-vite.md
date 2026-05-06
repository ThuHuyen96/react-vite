---
title: "Vite + React Integration"
impact: "CRITICAL"
impactDescription: "Eliminates JS config overhead, enables zero-runtime CSS with Vite."
tags: ["setup", "vite", "react", "framework", "integration"]
---

## Vite + React Integration

Tailwind v4 works with Vite via the official Vite plugin (`@tailwindcss/vite`).

**Setup (Vite Plugin - recommended):**

```js
// vite.config.ts
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
})
```

```css
/* src/index.css */
@import 'tailwindcss';

@source './components/**/*.tsx';
@source './pages/**/*.tsx';
```

```tsx
// src/main.tsx
import './index.css'
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

**Incorrect (v3 config reference):**

```js
// tailwind.config.js - NOT the v4 way
module.exports = {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
}
```

**Correct (v4 CSS source detection):**

```css
/* In index.css */
@import 'tailwindcss';

/* Explicit source paths if auto-detection misses files */
@source './src/**/*.tsx';
```

**Trade-offs / When NOT to use:**

- **Complex custom PostCSS pipelines:** The `@tailwindcss/vite` plugin uses lightningcss under the hood for maximum performance, which might bypass some older PostCSS plugins. If you heavily rely on other PostCSS plugins, you might need to use `@tailwindcss/postcss` instead.

Reference: [Installation - Vite](https://tailwindcss.com/docs/installation/vite)
