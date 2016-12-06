#!/usr/bin/python2.7
import logging
import sys
import argparse

from file.dir import Dir
from uploader.upload import Uploader


def main(url, pathname):
    dir = Dir()
    files = dir.scan(pathname)
    if len(files) < 1:
        logging.warn("No file into " + pathname)
        sys.exit(0)
    uploader = Uploader(url)
    for file in files:
        logging.info('File: %s', file)
        response = uploader.upload(file)
        if 299 < response.status_code:
            logging.error('Request Error: %s', response.text)
        else:
            logging.info(response.text)
    uploader.upload_dashboard()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', dest='url', help='Repository endpoint', required=True)
    parser.add_argument('--dir', dest='directory', help='Directory contains data files', required=True)
    args = parser.parse_args()
    main(args.url, args.directory)
