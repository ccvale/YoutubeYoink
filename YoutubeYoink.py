from pytube import YouTube, Stream

# take url and type

def download(video: Stream):
    try:
        video.download()
    except:
        raise RuntimeError('There has been an issue downloading the file. Please try again.')

#url, fileType = input('Enter url and filetype (mp3 or mp4): ').split(' ').lower()
url = 'https://www.youtube.com/watch?v=EMlM6QTzJo0'
fileType = 'mp3'

if fileType not in ['mp3', 'mp4']:
    raise ValueError('Invalid file type for the expected operation. Please try again selecting an mp3 or mp4 file instead.')
else:
    video = YouTube(url)
    if url == 'mp3':
        download(video.streams.get_audio_only())

    else:
        download(video.streams.get_lowest_resolution())
