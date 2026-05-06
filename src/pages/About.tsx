function About() {
  return (
    <div className="flex flex-col items-center justify-center py-12">
      <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">About This Project</h1>
      <p className="max-w-md text-center text-gray-600 dark:text-gray-300">
        This is a standard React SPA built with Vite, TypeScript, Tailwind CSS v4, and React Router v7.
      </p>
      <div className="mt-8 p-6 bg-gray-50 dark:bg-zinc-900 rounded-xl border border-gray-100 dark:border-zinc-800">
        <h2 className="text-xl font-semibold mb-2">Features Configured</h2>
        <ul className="list-disc list-inside space-y-2 text-left text-gray-700 dark:text-gray-200">
          <li>Tailwind CSS v4 (using Vite plugin)</li>
          <li>React Router v7 (unified routing)</li>
          <li>TypeScript & React 19</li>
        </ul>
      </div>
    </div>
  )
}

export default About
