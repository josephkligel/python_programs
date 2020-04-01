from pytube import Youtube

yt = Youtube("https://www.youtube.com/watch?v=J3h7Cv2fLe4")

print(yt.streams.all())
