import requests
import os
import logging

class Uploader:

    endpoint = '/repositories/<repo>/statements'

    def __init__(self, url, repo):
        self.endpoint = self.endpoint.replace('<repo>', repo)
        self.url = requests.compat.urljoin(url, self.endpoint)
        self.baseurl = url

    def upload(self, file):
        if not os.path.isfile(file):
            logging.error('%s is not a file', file)
            raise Exception(file + ' is not a file')
        file = open(file, 'rb').read()
        return requests.post(self.url, headers={'Content-Type': 'text/plain'}, data=file)

    def upload_dashboard(self):
        logging.warn('Dashboard: %s', requests.compat.urljoin(self.baseurl, '/import'))

