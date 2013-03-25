#!/usr/bin/env python

# kinome-stack server
# a RESTful API server for siRNA screen data
# Copyright (c) 2013 Joseph Lee, Nick Robin, Kinobus
# http://github.com/kinobus

# This software is freely available under the MIT Licence
# See LICENSE for details

import web
import os
import kslabkey
from zlib import compress, decompress, error as zerr
from urllib import urlencode
from urlparse import parse_qs
from experiment import PlateExperiment


class index:
    def GET(self, name):
        '''
        data request
        currently returns kinome reference table
        '''
        print name
        reqData = web.input()
        return kslabkey.getList(reqData, *(name.split('/')))

    def POST(self, name):
        '''
        POST EnVision Plate Reader data
        '''
        postData = web.input(_unicode=True, files=[])
        #import pdb; pdb.set_trace()
        pe = PlateExperiment(postData)


class favicon:
    def GET(self):
        return ''


urls = (
    '/(.*)', 'index',
    '/favicon\.ico', 'favicon'
)
        

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
