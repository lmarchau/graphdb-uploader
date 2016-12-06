import path
import os
import logging

class Dir:

    def scan(self, pathname):
        results = []
        if not os.path.exists(pathname) or not os.path.isdir(pathname):
            logging.error('Path %s does not exists', pathname)
            raise Exception(pathname + ' does not exists or not a dir')
        results.extend(path.path(pathname).walkfiles())
        return results
