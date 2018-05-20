# Blacknet (under dev)

Music generation package based on your preferences defined in playlists. Currently under development.

## Project stages
1. Scraping guitar pro files from https://www.ultimate-guitar.com/ (**_Test_**)
2. Transforming guitar pro (`.gp[3456]?`) files to midi (`.mid`) (**_TODO_**)
3. Transforming midi files to numerical data (**_TODO_**)
4. Modeling with LSTM (**_TODO_**)
5. Playing :) and wrapping everything up (**_TODO_**)

## Quick start
make sure to have these installed (the classics):
- python3 (at least v3.6)
- pip
- virtualenv

If so, clone this repository and install PyPi packages from the requirements file into a new 
environment. Activate this environment.
```
git clone https://github.com/devdnhee/blacknet-melancholy
virtualenv ENV -p python3
source ENV/bin/activate
pip install -r requirements.txt
```

The first step is to retrieve all URLs where `.gp` files with the best user ratings are downloadable.
The only supported text input at the moment are files structured in the following format:
```
TITLE_1 ARTIST_1  OTHER_1
TITLE_2 ARTIST_2  OTHER_2
  ...
TITLE_N ARTIST_N  OTHER_N
```
Hence, csv files with a tab separator. These can be created by simply copy pasting an iTunes playlist.
An interesting addition (but with much less priority) is to create these files with OCR on pdfs, 
to create an end-to-end system.

It is advised to store these playlist files in the `data/playlists` directory (Although this can easily
be modified in `blacknet/settings.py`).

With these files as input, we can use the _scrapy_ library to retrieve all sorts of information from which
the URL is the crucial one.
```
scrapy crawl UltimateGuitar -a playlist=test -o data/scraped/posthardcore.csv -t csv
```

Unfortunately, it didn't seem trivial to send the right HTTP request to access the guitar pro file itself.
This is why the output is a csv file which can be interpreted by pandas.

To effectively download the guitar pro files, `blacknet/GuitarProScraper/download.py` should be executed.
This we can do with for example
```
python scripts/download.py data/scraped/test.csv --max-download 2 --sleep-time 0.5 --download-dir
```
(To know what the args do, just call `python scripts/download.py -h`)