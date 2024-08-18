import soundfile as sf
from vosk import Model, KaldiRecognizer, SetLogLevel
import json
import wave
import sys
import yt_dlp



def download_audio(url: str):
    output = "audio.mp3"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return ydl_opts["outtmpl"]



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


def transcribe(file):
    SetLogLevel(0)

    # wf = wave.open("./test-audio/test.wav", "rb")
    wf = wave.open(file, "rb")

    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        sys.exit(1)

    model = Model(lang="en-us")
    # You can also init model by name or with a folder path
    # model = Model(model_name="vosk-model-en-us-0.21")
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

    print(splitText)


download_audio("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
transcribe("./audio.mp3")