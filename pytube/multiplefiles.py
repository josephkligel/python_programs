from pytube import YouTube

video_list = open("ytlink.txt")

for i in video_list:
    yt = YouTube(i)

    try:
        dw = yt.streams.first()
        print("Downloading...")
        dw.download("/home/jkligel/Downloads/VideoDownloader")

        print("Completed the download of", i)
    except:
        print("Download failed for", i)
