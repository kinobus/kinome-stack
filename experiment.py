import os
import tempfile
from zlib import decompress, compress, error as zerr
from rpy2 import robjects
from subprocess import call


class PlateExperiment:

    def __init__(self, postData):

        # decompress if compressed with zlib
        # checks for a zlib header in bytestring which could invoke
        # false negatives
        if postData.has_key('compressed'):
            for key in postData.keys():
                try:
                    postData[key] = decompress(postData[key])
                except zerr as ze:
                    print 'ZLIB: %s' %(ze)
                    pass

        # write files out to temp
        self.tmpDir = tempfile.mkdtemp(suffix='_ks')

        for f in postData['files']:
            print f
            fopen = open(os.path.join(self.tmpDir, f), 'w')
            fopen.write(postData[f])
            fopen.close()

        try:
            # parse EnVision Plate Reader datasets
            self.pr = PlateReader(self.tmpDir, postData['files'])

        finally:
            # delete temp files
            print 'DELETE: %s' %(self.tmpDir)
            call(['rm', '-rf', self.tmpDir])


class PlateReader:
    '''
    parse EnVision plate reader using cellHTS2 package
    for the R programming language
    '''
    def __init__(self, expDir, files):
        '''
        expDir: tmp directory with experimental data files
        '''
        robjects.r('library')('cellHTS2')    # import
        # cellHTS2 object
        self.dataset = self.readPlateList(expDir, files)
    
    def readPlateList(self, expDir, files):
        '''
        wrapper for cellHTS2 method of the same name
        '''
        return robjects.r('readPlateList')(files[0], path=expDir)

    def attr(self, attrName):
        '''
        valid attributes for cellHTS2 object:
        assayData, phenoData, featureData, plateList, intensityFiles,
        plateData, experimentData, plateConf, screenLog, screenDesc
        '''
        return robjects.r('attr')(self.dataset, attrName)
