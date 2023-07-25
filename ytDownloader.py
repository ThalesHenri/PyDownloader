from pytube import YouTube
from sys import argv

#obetos e o argv é pra executar do terminal
link = argv[1]
yt = YouTube(link)

print("Downloader de videos do youtube.")
print("="*20)
print("Título: ", yt.title)
print("Views: ", yt.views)
print("Autor: ", yt.author)
print("baixando o seu vídeo   ##########")
yd = yt.streams.get_highest_resolution()
yd.download()
print("vídeo baixado com sucesso!")
#baixando da resolução mais alta

print("="*20)
