import requests
from pytube import YouTube
url = ""
r = requests.get(url, stream = True)
chunk_size = 256
with open('igi.mp4','wb') as f:
    for chunk in r.iter_content(chunk_size=chunk_size):
        f.write(chunk)