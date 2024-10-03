import yt_dlp
from moviepy.editor import AudioFileClip

# URL do vídeo do YouTube
url = 'https://www.youtube.com/watch?v=TvQxO4DBu0g'

# Baixar o áudio do vídeo do YouTube usando yt-dlp
ydl_opts = {
    'format': 'bestaudio',  # Garantir que só o áudio seja baixado
    'outtmpl': 'audio.mp4',  # Nome do arquivo de saída
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# Carregar o áudio baixado
audio_clip = AudioFileClip('audio.mp4')

# Definir os tempos de início e fim em segundos (7 minutos e 12 segundos até 7 minutos e 20 segundos)
start_time = 2 * 60 + 39  # 7:12 = 432 segundos
end_time = 2 * 60 + 42    # 7:20 = 440 segundos

# Cortar o trecho desejado
audio_trecho = audio_clip.subclip(start_time, end_time)

# Salvar o trecho de áudio cortado como MP3
audio_trecho.write_audiofile("audio_trecho.mp3")

# Fechar os clipes para liberar recursos
audio_clip.close()
audio_trecho.close()
