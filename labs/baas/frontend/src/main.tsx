import { StrictMode, useState, useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import { listNotes, Note } from './api';
import { NoteForm } from './components/NoteForm';
import { NoteList } from './components/NoteList';

function App() {
  const [notes, setNotes] = useState<Note[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadNotes();
  }, []);

  const loadNotes = async () => {
    try {
      setError(null);
      const data = await listNotes();
      setNotes(data);
    } catch (error) {
      console.error('Failed to load notes:', error);
      setError(error instanceof Error ? error.message : 'Failed to load notes');
    }
  };

  const handleCreate = (newNote: Note) => {
    setNotes((prev) => [...prev, newNote]);
  };

  const handleDelete = (id: string) => {
    setNotes((prev) => prev.filter((n) => n.id !== id));
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
      <h1>📝 Firebase Notes</h1>
      <p style={{ color: '#666' }}>A simple note-taking app built with FastAPI + React + Firebase</p>
      
      {error && (
        <div style={{ padding: '10px', backgroundColor: '#ffebee', color: '#c62828', borderRadius: '4px', marginBottom: '20px' }}>
          Error: {error}
        </div>
      )}

      <NoteForm onCreate={handleCreate} />
      <NoteList notes={notes} onDelete={handleDelete} />
    </div>
  );
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
