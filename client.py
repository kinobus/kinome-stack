#!/usr/bin/env python

# This is an example client for kinome-stack

import requests
import os
from zlib import compress, error as zerr
from urllib import urlencode

if __name__ == '__main__':
    from sys import argv
    # expect a hostname, followed by a
    # file list, starting with platelist key file
    hostname = argv[1]
    fListPath = argv[2:]    # file list with rel path
    filesNames = []      # path stripped
    d = {}
    for f in fListPath:
        fopen = open(f, 'r')
        fdata = fopen.read()
        fopen.close()
        fname = os.path.split(f)[-1]
        filesNames.append(fname)
        d.update({ fname: fdata })
    d.update({ 'files': filesNames })
    postData = urlencode(d, True)
    
    resp = requests.post(hostname, data=postData)
    print resp
