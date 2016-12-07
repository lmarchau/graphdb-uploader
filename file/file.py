#!/usr/bin/python2.7

import os
import logging

class File:

    @staticmethod
    def split(file, dir, nb=100000, prefix=None):
        if not prefix:
            prefix = os.path.splitext(os.path.basename(file))[0]
        if not os.path.exists(dir):
            logging.info('Create directory %s', dir)
            os.mkdir(dir)
        ext = os.path.splitext(file)[1]
        fo = open(file, 'r')
        count = 0
        fw = None
        part = 0
        for line in fo:
            if count % nb == 0:
                if fw is not None:
                    fw.close()
                new_file = prefix + '_' + str(part) + ext
                logging.info('Open file %s', new_file)
                fw = open(os.path.join(dir, new_file), 'w')
                part += 1
            fw.write(line)
            count += 1
        fw.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    File.split('test.nq', 'results')
