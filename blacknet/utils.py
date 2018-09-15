import pandas as pd
import os.path

from . import settings as s


def read_playlist(fn):
    fn_path = os.path.join(s.PLAYLIST_DIR, fn)
    return pd.read_csv(fn_path, sep='\t', header=None) \
            .rename({0: 'Song',
                     1: 'Artist',
                     #2: 'Plays'
                     }, axis='columns')


def check_if_exists_or_create(directory):
    """Check if dir exists, create otherwise."""
    if not os.path.exists(directory):
        os.makedirs(directory)
