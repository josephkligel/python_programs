from pytube import YouTube

link = input("Paste link of YouTube video here: ")

try:
    yt = YouTube(link)
    dw = yt.streams.first()
    print("Downloading...")
    dw.download("/home/jkligel/Downloads/VideoDownloader")
    print("\nCompleted the download of", link)
except:
    print("Error downloading", link)
