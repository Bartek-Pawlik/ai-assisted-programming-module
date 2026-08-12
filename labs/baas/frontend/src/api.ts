function resolveApiBaseUrl(): string {
  // 1. Try to derive from current window location (most robust for Codespaces)
  if (typeof window !== "undefined") {
    const { protocol, hostname } = window.location;
    
    if (hostname.endsWith(".app.github.dev")) {
      // Handle format: 5173-codespace-name.app.github.dev
      const portFirstMatch = hostname.match(/^(\d+)-(.+)\.app\.github\.dev$/);
      if (portFirstMatch) {
        return `${protocol}//${portFirstMatch[2]}-8000.app.github.dev`;
      }

      // Handle format: codespace-name-5173.app.github.dev
      const nameFirstMatch = hostname.match(/^(.+)-(\d+)\.app\.github\.dev$/);
      if (nameFirstMatch) {
        return `${protocol}//${nameFirstMatch[1]}-8000.app.github.dev`;
      }
    }
  }

  // 2. Fallback to environment variable if it's set and NOT localhost
  const configured = import.meta.env.VITE_API_URL;
  if (configured && !configured.includes("localhost")) {
    return configured;
  }

  // 3. Default to localhost
  return "http://localhost:8000";
}

const API_BASE_URL = resolveApiBaseUrl();

export interface Note {
  id: string;
  title: string;
  content: string;
  created_at: string;
}

export interface NoteCreatePayload {
  title: string;
  content: string;
}

async function handleResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    const body = await response.text();
    throw new Error(`API error ${response.status}: ${body}`);
  }
  return response.json() as Promise<T>;
}

export async function listNotes(): Promise<Note[]> {
  const response = await fetch(`${API_BASE_URL}/notes`);
  return handleResponse<Note[]>(response);
}

export async function createNote(payload: NoteCreatePayload): Promise<Note> {
  const response = await fetch(`${API_BASE_URL}/notes`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return handleResponse<Note>(response);
}

export async function deleteNote(id: string): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/notes/${id}`, {
    method: "DELETE",
  });
  if (!response.ok) {
    const body = await response.text();
    throw new Error(`API error ${response.status}: ${body}`);
  }
}
