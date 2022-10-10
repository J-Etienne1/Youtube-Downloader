
import pytube 
a=input("video url-")
fetch = pytube.YouTube(a)
filter = fetch.streams.filter(progressive=True, file_extension='mp4')
filter.get_highest_resolution().download()
print("Download finished")
exit=input()




