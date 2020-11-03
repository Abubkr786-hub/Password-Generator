import pafy

url = "https://www.youtube.com/watch?v=h-KHWUq3B7I"
video = pafy.new(url)
# count = video.viewcount
# print(str(count) )

audiostreams = video.audiostreams
for i in audiostreams:
    print(i.get_filesize())
audiostreams[3].download()
print("Download Successful !")
