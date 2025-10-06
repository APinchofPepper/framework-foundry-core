import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900 flex flex-col items-center justify-center p-8">
      <div className="flex gap-8 mb-8">
        <a href="https://vite.dev" target="_blank" className="block">
          <img src={viteLogo} className="h-24 w-24 hover:animate-spin transition-all" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank" className="block">
          <img src={reactLogo} className="h-24 w-24 hover:animate-spin transition-all" alt="React logo" />
        </a>
      </div>
      <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-8">
        Vite + React + Tailwind CSS v4
      </h1>
      <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg">
        <button 
          onClick={() => setCount((count) => count + 1)}
          className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg transition-colors mb-4"
        >
          count is {count}
        </button>
        <p className="text-gray-600 dark:text-gray-300">
          Edit <code className="bg-gray-100 dark:bg-gray-700 px-2 py-1 rounded">src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="text-gray-500 dark:text-gray-400 mt-8">
        Click on the Vite and React logos to learn more
      </p>
    </div>
  )
}

export default App
