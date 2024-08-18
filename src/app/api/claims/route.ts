import { NextResponse } from "next/server";
import { OpenAI } from "openai";
// import { AssemblyAI } from "assemblyai";import Audio2TextJS from 'audio2textjs';
import Audio2TextJS from "audio2textjs";

// const audioToText = requireaudio2textjs");

async function transcribeAudio() {
  try {
    const filePath = "./path/to/your/audio-file.wav";
    const transcription = await Audio2TextJS.transcribeAudio(filePath);

    console.log("Transcription:", transcription);
  } catch (error) {
    console.error("Error during transcription:", error);
  }
}

transcribeAudio();
// export async function GET(req: Request) {}

// // /app/api/users/route.ts
// import { NextResponse } from 'next/server';

// export async function GET(req: Request) {
//   const { searchParams } = new URL(req.url);
//   const action = searchParams.get('action');

//   if (action === 'fetchUser') {
//     return fetchUser();
//   } else if (action === 'fetchAllUsers') {
//     return fetchAllUsers();
//   } else {
//     return NextResponse.json({ error: 'Invalid action' }, { status: 400 });
//   }
// }

// async function fetchUser() {
//   // Logic to fetch a single user
//   const user = { id: 1, name: 'John Doe' };
//   return NextResponse.json(user);
// }

// async function fetchAllUsers() {
//   // Logic to fetch all users
//   const users = [
//     { id: 1, name: 'John Doe' },
//     { id: 2, name: 'Jane Doe' },
//   ];
//   return NextResponse.json(users);
// }
