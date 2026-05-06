import { Routes, Route, Link } from 'react-router'
import Home from './pages/Home.tsx'
import About from './pages/About.tsx'

function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <nav className="flex items-center justify-between p-6 border-b border-gray-100 dark:border-zinc-800 bg-white/80 dark:bg-zinc-950/80 backdrop-blur-md sticky top-0 z-50">
        <div className="font-bold text-xl tracking-tight text-purple-600 dark:text-purple-400">
          React SPA
        </div>
        <div className="flex gap-6">
          <Link 
            to="/" 
            className="text-gray-600 dark:text-gray-300 hover:text-purple-600 dark:hover:text-purple-400 font-medium transition-colors"
          >
            Home
          </Link>
          <Link 
            to="/about" 
            className="text-gray-600 dark:text-gray-300 hover:text-purple-600 dark:hover:text-purple-400 font-medium transition-colors"
          >
            About
          </Link>
        </div>
      </nav>

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </main>
    </div>
  )
}

export default App
