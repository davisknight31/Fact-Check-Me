import soundfile as sf
from vosk import Model, KaldiRecognizer, SetLogLevel
from pydub import AudioSegment
import json
import wave
import sys
import yt_dlp
import ffmpeg




def download_audio(url: str):
    output = "audio"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',        # Extract the audio using FFmpeg
                'preferredcodec': 'wav',            # Convert the audio to WAV format
            },
        ],
        'postprocessor_args': [
            '-ac', '1',              # Ensure the output is mono (1 channel)
            '-ar', '44100',          # Set the sample rate to 44100 Hz (CD quality)
            '-sample_fmt', 's16'     # Set the sample format to 16-bit
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return ydl_opts["outtmpl"]


# def convert_audio():
#     audio = AudioSegment.from_mp3("audio.mp3")
#     audio = audio.set_channels(1)
#     audio = audio.set_sample_width(2)

#     audio.export('final_audio.wav', format='wav')

# def convert_mp3_to_mono_wav():
#     (
#         ffmpeg
#         .input("audio.wav")
#         .output("output_file.wav", ac=1, ar='44100', format='wav', acodec='pcm_s16le')
#         .run()
#     )


# model_path = "./vosk-models/vosk-model-small-en-us-0.15"
# audio_file_path = "./test-audio/HelloWord.wav"

# # Load the Vosk model
# model = Model(model_path)

# # Load audio file
# audio, samplerate = sf.read(audio_file_path)


# recognizer = KaldiRecognizer(model, samplerate)

# transcription = ""
# for chunk in audio:
#     if recognizer.AcceptWaveform(chunk):
#         result = recognizer.Result()
#         result_json = json.loads(result)
#         transcription += result_json.get("text", "")

# # Get final result
# final_result = recognizer.FinalResult()
# final_result_json = json.loads(final_result)
# transcription += final_result_json.get("text", "")


def transcribe():
    SetLogLevel(0)

    wf = wave.open('audio.wav', "rb")

    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        sys.exit(1)

    # model = Model(lang="en-us")
    # You can also init model by name or with a folder path
    model = Model(model_name="vosk-model-en-us-0.21")
    model = Model("C:/Users/davis/.cache/vosk/vosk-model-small-en-us-0.15")
    # model = Model("models/en")

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    rec.SetPartialWords(True)

    splitText = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # print(rec.Result())
            res = json.loads(rec.Result())
            print(res["text"])
            splitText.append(res["text"])
        # else:
        #     print('n/a')
        #     print(rec.PartialResult())

    # res = json.loads(rec.FinalResult())
    # print(res["text"])
    # transcription = ""
    # for chunk in audio:
    #     if rec.AcceptWaveform(chunk):
    #         result = rec.Result()
    #         result_json = json.loads(result)
    #         transcription += result_json.get("text", "")


    # final_result = rec.FinalResult()
    # final_result_json = json.loads(final_result)
    # transcription += final_result_json.get("text", "")

    for text in splitText:
        print(text)


# download_audio("https://www.youtube.com/watch?v=N9B59PHIFbA") # make and do english
download_audio("https://www.youtube.com/watch?v=EbODOruXads")

transcribe()
# convert_audio()
# transcribe("./audio.mp3")