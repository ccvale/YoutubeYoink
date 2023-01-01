from pytube import YouTube, Stream
import os

class YoutubeVideo:
    def __init__(self, url: str = '', fileType: str = ''):

        if os.name == 'nt':
            self.DOWNLOAD_FOLDER = f'{os.getenv("USERPROFILE")}\\Downloads'
        else:
            self.DOWNLOAD_FOLDER = f'{os.getenv("HOME")}/Downloads'

        self.url = url
        self.fileType = fileType

    def download(self, video: Stream):
        try:
            return video.download(self.DOWNLOAD_FOLDER)
        except:
            raise RuntimeError('There has been an issue downloading the file. Please try again.')

    def setURL(self, choice):
        self.url = choice
    
    def setFileType(self, choice):
        self.fileType = choice


    def convert(self):
        print(self.url, self.fileType)
        if self.fileType not in ['MP3', 'MP4']:
            raise ValueError('Invalid file type for the expected operation. Please try again selecting an mp3 or mp4 file instead.')
        else:
            video = YouTube(self.url)
            if self.fileType == 'MP3':
                of = self.download(video.streams.get_audio_only())
                base, ext = os.path.splitext(of)
                new = base + '.mp3'
                os.rename(of, new)

            else:
                self.download(video.streams.get_highest_resolution())
            
