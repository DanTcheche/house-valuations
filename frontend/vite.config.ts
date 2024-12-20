import path from "path";
import react from "@vitejs/plugin-react";
import { defineConfig, loadEnv } from "vite";
import type { ConfigEnv, UserConfigExport } from "vite";

const config = ({ mode }: ConfigEnv): UserConfigExport => {
  // Load and merge environment variables
  process.env = { ...process.env, ...loadEnv(mode, process.cwd()) };

  const {
    VITE_APP_ENV,
    VITE_APP_URL,
  } = process.env;

  const baseConfig = {
    plugins: [
      react(),
    ].filter(Boolean),
    build: {
      sourcemap: true,
      manifest: true,
      rollupOptions: {
        input: { main: path.resolve(__dirname, "index.html") },
      },
    },
    server: {
      open: false,
      host: true,
      origin: VITE_APP_ENV === "local" ? VITE_APP_URL : "",
    },
    resolve: {
      alias: [{ find: "@", replacement: path.resolve(__dirname, "./src") }],
    },
  };

  return defineConfig(baseConfig);
};

export default config;
