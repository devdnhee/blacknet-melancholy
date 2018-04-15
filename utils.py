import pandas as pd
import os.path

ABS_PATH = os.path.abspath(__file__)
ABS_DIR = os.path.dirname(ABS_PATH)
PLAYLIST_DIR = os.path.join(ABS_DIR, 'playlists')

def read_playlist(fn):
    fn_path = os.path.join(PLAYLIST_DIR, fn)
    return pd.read_csv(fn_path, sep='\t', header=None) \
            .rename({0: 'Song', 1: 'Artist', 2: 'Plays'}, axis='columns')