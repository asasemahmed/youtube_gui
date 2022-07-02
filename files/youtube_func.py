from pytube import YouTube
from tkinter import messagebox

def download_vedio(url: str, file: str, resolution: int) -> None:
    yt = YouTube(url)
    if resolution == 1:
        strem1 = yt.streams.get_lowest_resolution()
    elif resolution == 2:
        strem1 = yt.streams.get_highest_resolution()
        strem1.download(output_path=file)
    elif resolution == 360:
        strem1 = yt.streams.get_by_itag(18)
    else:
        strem1 = yt.streams.get_highest_resolution()

    if file == "":
        strem1.download()
    else:
        strem1.download(output_path=file)





