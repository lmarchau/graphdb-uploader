import requests
import os
import logging

class Uploader:

    endpoint = '/rest/data/import/upload'

    def __init__(self, url):
        self.url = requests.compat.urljoin(url, self.endpoint)
        self.baseurl = url

    def upload(self, file):
        if not os.path.isfile(file):
            logging.error('%s is not a file', file)
            raise Exception(file + ' is not a file')
        files = {'file': open(file, 'rb')}
        return requests.post(self.url, files=files)

    def upload_dashboard(self):
        logging.warn('Dashboard: %s', requests.compat.urljoin(self.baseurl, '/import'))

