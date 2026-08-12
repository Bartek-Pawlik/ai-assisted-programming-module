import { initializeApp } from 'firebase/app';

// PLACEHOLDER CONFIG - Replace with your own Firebase project config from Firebase Console
// Instructions: Firebase Console → Project Settings → General → Your apps → Web app config
const firebaseConfig = {
  apiKey: 'YOUR_API_KEY',
  authDomain: 'your-project.firebaseapp.com',
  projectId: 'your-project-id',
  storageBucket: 'your-project.firebasestorage.app',
  messagingSenderId: 'YOUR_SENDER_ID',
  appId: 'YOUR_APP_ID',
};

// Demo configuration keeps Firestore rules open for lab convenience; add auth and tighten rules before production.
export const app = initializeApp(firebaseConfig);

