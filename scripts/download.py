import argparse

from blacknet.GuitarProScraper.download import download_files

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wrapper to download guitar pro files from scraped playlist. '
                                                 'Currently only chrome is supported.')

    parser.add_argument(metavar='input-file',
                        help='csv file (comma separated with header) as input.',
                        dest='input_file')
    parser.add_argument('--download-dir',
                        help='absolute path to write guitar pro files to in a new directory, based on name.'
                             ' (eg.: data/playlists and input file rock.csv -> new dir: data/downloaded/rock)',
                        action='store_true')
    parser.add_argument('--max-download',
                        help='How many files to download at most.',
                        default=None,
                        type=int)
    parser.add_argument('--sleep-time',
                        help='How long to wait before changing urls in the test browser',
                        default=0,
                        type=float)

    args = parser.parse_args()

    download_files(args.input_file,
                   max_download=args.max_download,
                   sleep_time=args.sleep_time,
                   download_dir=args.download_dir)





