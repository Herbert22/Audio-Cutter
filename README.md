# recortar-parte-do-audio
Este projeto em Python permite baixar o áudio de um vídeo do YouTube e extrair um trecho específico do áudio. O áudio é baixado no formato MP4 e, em seguida, um intervalo de tempo definido é cortado e salvo como um arquivo MP3.

### Funcionalidades
Baixar o áudio de qualquer vídeo do YouTube.
Extrair um trecho específico do áudio com base no tempo de início e fim (em minutos e segundos).
Salvar o trecho de áudio extraído em formato MP3.

### Pré-requisitos
Antes de executar o script, você precisará instalar as seguintes dependências:
Python 3.10 ou superior
yt-dlp (para baixar o áudio do YouTube)
moviepy (para manipulação de áudio e vídeo)

### Instalação das dependências:
  pip install yt-dlp moviepy

### Como usar
Clone o repositório ou baixe o código.
Defina a URL do vídeo do YouTube no script Python.
Especifique os tempos de início e fim do trecho de áudio que deseja extrair.
Execute o script e o áudio será baixado e o trecho desejado será salvo como audio_trecho.mp3.

### Exemplo de uso:
No script Python, você pode ajustar a URL do vídeo e o intervalo de tempo (em segundos):

  url = 'https://www.youtube.com/watch?v=EXEMPLO_DE_URL'
  
  start_time = 7 * 60 + 12  # Exemplo: 7:12 (432 segundos)
  end_time = 7 * 60 + 20    # Exemplo: 7:20 (440 segundos)

###Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request com sugestões e melhorias.
