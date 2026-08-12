// Extend ImportMetaEnv typing so TypeScript recognises Vite variables we rely on.
interface ImportMetaEnv {
  readonly VITE_API_URL?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
