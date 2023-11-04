import moviepy.editor as mp


arquivo = "Nome_Video.mp4" 

#converter de mp4 para mp3
audio = mp.VideoFileClip(arquivo)
audio.audio.write_audiofile("./Nome_Audio.mp3")
