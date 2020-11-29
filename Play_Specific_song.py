import file_search
import os

music_path = "F:\\ringtone"

def play_audio(song_name):
    file_search.set_root(music_path)
    songs = file_search.searchFile(song_name)
    try:
        song_uri = songs[0]
        os.startfile(os.path.join(music_path,songs[0]))
        print("Song Is Playing")
    except:
        print("Sorry Sir")

query = input("Enter THE Song You Want To Listen=")
play_audio(query)