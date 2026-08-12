import { useState } from 'react';
import { createNote, NoteCreatePayload } from '../api';

interface NoteFormProps {
  onCreate: (note: any) => void;
}

export function NoteForm({ onCreate }: NoteFormProps) {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim() || !content.trim()) return;

    const payload: NoteCreatePayload = {
      title: title.trim(),
      content: content.trim(),
    };

    try {
      const newNote = await createNote(payload);
      onCreate(newNote);
      setTitle('');
      setContent('');
    } catch (error) {
      console.error('Failed to create note:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: '20px' }}>
      <div style={{ marginBottom: '10px' }}>
        <input
          type="text"
          placeholder="Note title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          style={{ width: '100%', padding: '8px', fontSize: '16px' }}
        />
      </div>
      <div style={{ marginBottom: '10px' }}>
        <textarea
          placeholder="Note content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          required
          rows={4}
          style={{ width: '100%', padding: '8px', fontSize: '14px' }}
        />
      </div>
      <button type="submit" style={{ padding: '8px 16px' }}>Add Note</button>
    </form>
  );
}
