import { deleteNote, Note } from '../api';

interface NoteCardProps {
  note: Note;
  onDelete: (id: string) => void;
}

export function NoteCard({ note, onDelete }: NoteCardProps) {
  const handleDelete = async () => {
    if (!confirm('Delete this note?')) return;
    
    try {
      await deleteNote(note.id);
      onDelete(note.id);
    } catch (error) {
      console.error('Failed to delete note:', error);
    }
  };

  return (
    <div style={{ 
      border: '1px solid #ddd', 
      padding: '15px', 
      margin: '10px 0',
      borderRadius: '4px',
      backgroundColor: '#fafafa'
    }}>
      <h3 style={{ marginTop: 0 }}>{note.title}</h3>
      <p style={{ whiteSpace: 'pre-wrap' }}>{note.content}</p>
      <p style={{ fontSize: '12px', color: '#666' }}>
        Created: {new Date(note.created_at).toLocaleString()}
      </p>
      <button 
        onClick={handleDelete} 
        style={{ color: 'red', padding: '4px 12px' }}
      >
        Delete
      </button>
    </div>
  );
}
