## Global view
1. Download https://sourceforge.net/projects/tuxguitar/?source=typ_redirect
2. go to itunes and copy paste files from playlist printed to pdf (posthardcore)
3. process this text doc -> retrieve artists + songs + love + plays
4. find a way to scrape this data from ultimate-guitar (if present) and save .gp files in folder
	- scrapy
	- url: https://www.ultimate-guitar.com/search.php?search_type=title&value=adelleda%20alexisonfire
	
5. with tux guitar file format batch converter -> convert all to midi
6. process midi -> input + output rnn
7. modeling :)

## 15/04

### Done
1. GuitarProScraper: example run with `crawl UltimateGuitar -a playlist=posthardcore -o posthardcore.csv -t csv` 
2. written with Selenium: download guitar pro files by clicking them (get_gp.py)

Installation:
1. virtualenv ENV
2. pip install -r requirements.txt
3. install chromedriver 

### TODO
1. make installation script
2. write down structure of project
3. get the whole data pipeline to work beautifully with one script
	-> with bash script
	-> all python script with argparse 
4. documentation

## 20/05

### Done
1. reset project setup:
    - main pkg: `blacknet`
    - project dir: main proj dir
    - data goes to `data` (wow..)
    - import proj vars go to blacknet.settings` (no shit)
    - utils to `blacknet.utils` (this guy never ceases to amaze me)
    - download script in `blacknet.GuitarProScraper.download.py`, removed `get_gp.py` (much wow)
    - relative imports (yuy)
    - Scrapy cfg:
        - root directory: project directory (quite nice)
        - cfg in `scrapy.cfg`
        - settings in `blacknet.settings` (uniform with other settings :) )
        - scraper in `blacknet.GuitarProScraper`
        - spiders in `blacknet.GuitarProScraper.spiders`
2. Annoying pop up about GDPR shows up when going to a tab url for the first time (without cookie), hotfixed in `blacknet.GuitarProScraper.download.py`

### TODO
1. reading guitarpro files:
    - EASY: .gp3, .gp4, .gp5 -> with PyGuitarPro pkg
    - DIFFICULT: .gpx -> C package MuseScore: https://github.com/musescore/MuseScore
        - package mscore
        - extend with native C++ code: https://docs.python.org/3.6/extending/extending.html
    - parse to midi => that way we can continue from there one (and extendible to other formats)
2. link to gp filename in DataFrame (in `blacknet.GuitarProScraper.download`)
3. normalize filenames

## 21/05
-> use musescore = c++ application -> gp to midi

### Building and compiling musescore
1. compilation ix: https://musescore.org/en/handbook/developers-handbook/compilation/compile-instructions-macos-git
   
Install Xcode
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install libogg libsndfile libvorbis pkg-config portaudio jack lame cmake git
```
Install Qt 5.9! Later installments are NOT compatible with MuseScore. 

## 25/05
Developer handbook for MuseScore (not so much with it to do everything in reasonable time span):
- https://musescore.org/en/handbook/developers-handbook
- https://musescore.org/en/handbook

Creating shared object from Qt project:
https://wiki.qt.io/How_to_create_a_library_with_Qt_and_use_it_in_an_application

How to use it?
1. make a .so file of whole Qt project
2. make new .cpp code calling the right functions from the MuseScore library (looks damn hard :( )
3. Convert all guitar pro files to midi in cpp code

TODO:
1. Qt tutorial
2. Some .cpp refresher (so long ago...)
3. create .so
4. Cython -> use .so

Other way to do it:
Parse everything myself in python code
-> read functions in musescore/importgtp.cpp

## 27/05
New strategy (again...) after all research done:
1. transform .gp3, .gp4, .gp5 to .mid with guitarpro library
2. Create model with these
3. add .gpx support by making new C++ library supporting this, wrap C++ code

## 30/05
wrote first utility functions in new python package `blacknet.converter`

## BUGS

### 21/05
- csv export of scraper -> adds rows instead of rewriting
- exception handling when driving chrome and clicking does not work