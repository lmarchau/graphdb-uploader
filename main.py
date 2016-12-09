#!/usr/bin/python2.7
import logging
import shutil
import sys
import argparse
import os

import time

from file.dir import Dir
from file.file import File
from uploader.upload import Uploader


def main(url, repository, pathname, tmpdir):
    if tmpdir and os.path.exists(tmpdir):
        logging.error('TMP dir %s exists, but may not', tmpdir)
        raise Exception('TMP dir %s exists, but may not', tmpdir)

    dir = Dir()
    files = dir.scan(pathname)
    if len(files) < 1:
        logging.warn("No file into " + pathname)
        sys.exit(0)

    if tmpdir:
        for file in files:
            File.split(file, tmpdir)
        files = dir.scan(tmpdir)

    uploader = Uploader(url, repository)
    for file in files:
        logging.info('File: %s', file)
        response = uploader.upload(file)
        if 299 < response.status_code:
            logging.error('Request Error: %s', response.text)
        else:
            logging.info('OK ' + response.text)
    uploader.upload_dashboard()
    if tmpdir:
        logging.info('Remove %s and contents', tmpdir)
        shutil.rmtree(tmpdir)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', dest='url', help='Repository endpoint', required=True)
    parser.add_argument('--repo', dest='repo', help='Repository', required=True)
    parser.add_argument('--dir', dest='directory', help='Directory contains data files', required=True)
    parser.add_argument('--tmp', dest='tmpdir', help='Temporary Directory contains small datas files, do not exist')
    args = parser.parse_args()
    main(args.url, args.repo, args.directory, args.tmpdir)
