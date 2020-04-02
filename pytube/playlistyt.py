from pytube import Playlist

link = input("Paste link of YouTube playlist here: ")

try:
    print("Downloading links...")
    Playlist(link).download_all("/home/jkligel/Downloads/VideoDownloader")
    print("\nCompleted Downloading")
except:
    print("Error downloading")
