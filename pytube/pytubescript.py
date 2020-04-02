from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=J3h7Cv2fLe4")

dw = yt.streams.get_by_itag(18)
dw.download("/home/jkligel/Downloads")
