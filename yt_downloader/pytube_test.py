from pytube import YouTube 
from pytube.contrib.search import Search

somelink = 'https://www.youtube.com/watch?v=1tk1pqwrOys'

yt = YouTube(somelink)
audio_stream = yt.streams.filter(only_audio=True)[0]
audio_stream.download()
