import { Note } from '../api';
import { NoteCard } from './NoteCard';

interface NoteListProps {
  notes: Note[];
  onDelete: (id: string) => void;
}

export function NoteList({ notes, onDelete }: NoteListProps) {
  return (
    <div>
      {notes.length === 0 ? (
        <p style={{ color: '#666' }}>No notes yet. Create your first note above!</p>
      ) : (
        notes.map((note) => (
          <NoteCard
            key={note.id}
            note={note}
            onDelete={onDelete}
          />
        ))
      )}
    </div>
  );
}
