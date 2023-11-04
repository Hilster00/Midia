import os
import speech_recognition as sr
from moviepy.editor import VideoFileClip


def extrair_audio(video_path, output_audio_path):
    # Carrega o vídeo
    video = VideoFileClip(video_path)
    
    # Extrai o áudio
    audio = video.audio
    
    # Salva o áudio em um arquivo
    audio.write_audiofile(output_audio_path)

def transcrever_audio(audio_path,nome_arquivo):
    recognizer = sr.Recognizer()

    # Carrega o arquivo de áudio
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        # Reconhece a fala usando a API do Google
        texto_transcrito = recognizer.recognize_google(audio, language="pt-BR")
        with open(f"{nome_arquivo}.txt","a") as arquivo:
            arquivo.write(texto_transcrito)
    except sr.UnknownValueError:
        print("Não foi possível entender a fala")
    except sr.RequestError as e:
        print(f"Erro ao fazer a requisição para a API do Google: {e}")
        

if __name__ == "__main__":
    videos=[]

    if os.path.exists('./videos.txt'):
        with open("videos.txt","r") as lista:
            videos=lista.read()
            
        videos=videos.split("\n")
        while "" in videos:
            videos.remove("")
            
        for video in videos:
            video_path = f"{video}.mp4"
            audio_path = "audio.wav"
            
            extrair_audio(video_path, audio_path)
            transcrever_audio(audio_path,f"{video}")
            os.remove(audio_path)
    else:
         with open("./videos.txt","a") as arquivo:
            arquivo.write("video 1")
            
