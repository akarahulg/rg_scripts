#!/usr/bin/env python3

import os
import subprocess

def download_playlist():
    playlist_url = "https://open.spotify.com/playlist/70XaRIzoHYDYyAGEAde0lX?si=32c476199c9c46f5"
    download_path = os.path.expanduser("~/Music/mymusic")
    
    # Ensure the download path exists
    os.makedirs(download_path, exist_ok=True)
    
    # Run the spotdl command
    command = f"spotdl {playlist_url} --output {download_path}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    download_playlist()

