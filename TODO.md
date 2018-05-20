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

## 21/05

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