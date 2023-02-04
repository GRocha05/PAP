import importlib.util
import subprocess

def import_module(name):
    spec = importlib.util.find_spec(name)
    if spec is None:
        # The module does not exist, install it
        subprocess.run(["pip", "install", name])
        spec = importlib.util.find_spec(name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

try:
    import spotipy
except ModuleNotFoundError:
    import_module("spotipy")
try:
    import tekore
except ModuleNotFoundError:
    import_module("tekore")
from spotipy.oauth2 import SpotifyOAuth

client_id = "1a461569754e47b2871c1a6d225b005a"
client_secret= "d1fdb011a77e4120b57ee2b671976cf3"
redirect_url= "http://localhost"


try:

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url, scope="user-read-email user-read-private user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-recently-played user-library-read user-library-modify user-top-read playlist-read-private playlist-modify-private playlist-read-collaborative playlist-modify-public streaming app-remote-control user-follow-read user-follow-modify")) 



except spotipy.oauth2.SpotifyOauthError as e:
    print("idk")
    print(e)


def play_music(request):  
    results = sp.search(q=request, type='track')  
    musics = []
    musics.append(results['tracks']['items'][0]['uri'])
    for i in sp.recommendations(seed_tracks=[results['tracks']['items'][0]['uri']])['tracks']:
        musics.append(i['uri'])
    sp.start_playback(uris=musics)
   
    

def play_music_playlist(request):
     
    results = sp.search(q=request, type='playlist')
    for i in results['playlists']['items']:
        print(i['name'])
        print(i['uri'])
        sp.start_playback(context_uri=i['uri'])
        break
    
def play_music_artist(request):
     
    results = sp.search(q=request, type='artist')
    for i in results['artists']['items']:
        print(i['name'])
        print(i['uri'])
        sp.start_playback(context_uri=i['uri'])
        break

def play_like_music():     
    first = sp.current_user_saved_tracks()['items'][0]['track']['uri']
    sp.start_playback(uris=[first])
    musics=[] 
    for times in range(0,2):
        try:
            for music in sp.current_user_saved_tracks(offset=20*times)['items']:
                musics.append(music['track']['uri'])
        except (IndexError):            
            continue
    sp.start_playback(uris=musics)


def play_album(request):
    results = sp.search(q=request, type='album')
    for i in results['albums']['items']:
        sp.start_playback(context_uri=i['uri'])
        break


def pause_music():
    sp.pause_playback()
    
def resume_music():
    try:
        sp.start_playback()
    except spotipy.client.SpotifyException:
        print("Ocorreu algum problema, tente novamente.")

def next_music():
    sp.next_track()
    
def previous_music():
    sp.previous_track()
    
def volume_music(request):
    sp.volume(int(request))
    
def shuffle_music():
    sp.shuffle(True)

def unshuffle_music():
    sp.shuffle(False)

def repeat_music():
    sp.repeat('track')        

def unrepeat_music():
    sp.repeat('off')

def show_queue():
    for i in sp.queue()['queue']:
        print(i['name'])

import os
from mylib import * 
os.system("cls")
print(get_exe('Spotify'))
open_app('Spotify')

quit()
while True:
    try: 
        device = sp.devices()['devices'][0]['id']
    except:
        from mylib import *
        open_app('Spotify')
    os.system("cls")
    print("What do you want to do?")
    print("1. Play a song")
    print("2. Play a playlist")
    print("3. Play an artist")
    print("4. Play liked songs")
    print("5. Pause")
    print("6. Resume")
    print("7. Next")
    print("8. Previous")
    print("9. Volume")
    print("10. show queue")
    ask = input("Enter your choice: ")
    try:
        match ask:
            case "1":
                print("Enter the song name: ")
                song = input()
                play_music(song)
            case "2":
                print("Enter the playlist name: ")
                playlist = input()
                play_music_playlist(playlist)
            case "3":    
                print("Enter the artist name: ")
                artist = input()
                play_music_artist(artist)
            case "4":
                play_like_music()
            case "5":
                pause_music()
            case "6":
                resume_music()
            case "7":
                next_music()
            case "8":
                previous_music()
            case "9":
                volume= input("Enter the volume: ")
                volume_music(volume)
            case "10":
                show_queue()
    except Exception as e:
        print(e)
        input("Press enter to continue...")
        
  
        


