from tqdm import tqdm
import requests
chunk_size = 1024
resp = requests.get("https://images.unsplash.com/photo-1533467915241-eac02e856653?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;w=1000&amp;q=80",stream=1)
is_chunked = resp.headers.get('transfer-encoding','') == 'chunked'
content_length = resp.headers.get('content-length')
total_size = 0
if not is_chunked and content_length.isdigit():
    total_size = int(content_length)
else:
    content_length = None
with open('flower.png','wb') as f:
    try:
        for data in tqdm(iterable=resp.iter_content(chunk_size=chunk_size), total=total_size/1024, unit='KB'):
            f.write(data)
    except ConnectionAbortedError:
        print('\nPlease check your internet connection')
        exit()
    print('Download Complete')