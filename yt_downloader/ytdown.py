from pytube import YouTube 
from pytube.contrib.search import Search

SAVE_PATH = './yt_downloads/'

TRACKS = [
'gurenge lisa',
'kaikai kitan eve',
'guren does',
]

LINKS=[
'https://www.youtube.com/watch?v=Ph1a-k13Hsg',
'https://www.youtube.com/watch?v=1tk1pqwrOys',
'https://www.youtube.com/watch?v=QYrAscfzyPI',
]

def get_videos_from_name():
	links = []
	stop = 1
	while stop == 1:
		name = input("Type in the name of the video you would like to download: ")
		v_id = Search(name).results[0].video_id
		link = f"https://www.youtube.com/watch?v={v_id}"
		links.append(link)
		stop = int(input("Enter 1 if you would like to download more videos. \nEnter 0 if you are done."))
	return links

def get_videos_from_link():
	links = []
	stop = 1
	while stop == 1:
		link = input("Paste in your YouTube video link: ")
		links.append(link)
		stop = int(input("Enter 1 if you would like to download more videos. \nEnter 0 if you are done."))
	return links

def name_to_link(linklist):
	newlist = []
	for name in linklist:
		v_id = Search(name.lower()).results[0].video_id
		link = f"https://www.youtube.com/watch?v={v_id}"
		newlist.append(link)
	return newlist

def download_yt_audio_only(yt_links):
	for link in yt_links:
		try:
			yt = YouTube(link) 
			yt.check_availability() # checking if the video is found
			print(f"Video was found: {yt.title}")
			audio_streams = yt.streams.filter(only_audio=True) # create stream object and filter out only audio to a list
		except:
			raise TypeError(f"Content not found: {yt.title}, link: {link}")

		try: 
		    # download first audio in the list 
		    audio_streams[0].download(output_path=SAVE_PATH)
		    print(f"File is downloaded: {yt.title}")
		except: 
		    print("Error during download")

if __name__ == "__main__":

	# Get videos one by one with terminal inputs
	#yt_lista = get_videos_from_name()
	#download_yt_audio_only(yt_lista)

	# Same but with links inserted
	#yt_lista = get_videos_from_link()
	#download_yt_audio_only(yt_lista)
	
	# Download from name list

	#ytlinks = name_to_link(TRACKS)
	#download_yt_audio_only(ytlinks)

	# Donwload from link list
	download_yt_audio_only(LINKS)

	# Prints out when finished
	print("All task finished.")
