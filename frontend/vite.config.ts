import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  // 'base' ensures asset paths are relative, making it easier 
  // for FastAPI to serve the build files later.
  base: './', 
  resolve: {
    alias: {
      // This allows you to use '@' as a shortcut for the 'src' folder
      '@': path.resolve(__dirname, './src'),
    },
  },
  build: {
    // This matches the folder your Dockerfile expects
    outDir: 'dist',
    // Helps with debugging by generating source maps (optional)
    sourcemap: true,
    // Ensures the build fails if there are Rollup errors
    emptyOutDir: true,
  },
  server: {
    // Useful for Docker: allows the dev server to be accessible externally
    host: '0.0.0.0',
    port: 5173,
  }
});
