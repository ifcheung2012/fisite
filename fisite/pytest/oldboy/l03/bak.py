# -*- coding: utf-8 -*-
__author__ = 'ifcheung'
from optparse import OptionParser
import logging

MSG_USAGE = "tar [ -s <sourcefilename>][ -d <desttarfilename>][-f <isfullbackup:True,False>]"
parser = OptionParser(usage=MSG_USAGE)
parser.add_option("-s", "--source", action="store",
                  dest="sourceFile",
                  type="string",
                  help="full path of sourcefiles")
parser.add_option("-d", "--desttarfile", action="store",
                  dest="destFile",
                  type="string",
                  help="full path of backup files")
parser.add_option("-f", "--full", action="store_true", default=False,help="is full backup?")
parser.add_option("-v", action="store_true", dest="verbose")



fakeArgs = ['-f', 'thefile.txt', '-z', 'xyz', '-p', 'arg2','arg3']
helpargs = ['-h']
# (options, args) = parser.parse_args(fakeArgs)

logger = logging.getLogger()
file = logging.FileHandler("tar.log")
logger.addHandler(file)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
file.setFormatter(formatter)
logger.setLevel(logging.NOTSET)

for i in xrange(0,10):
    logger.info(str(i))
    logger.error(str(i)+":errror!")


# if options.pdcl:
#     print 'pdcl is true'
#     print options.fileName
# if options.zdcl:
#     print 'zdcl is true', args,args[0],args[1],args[2]

if __name__ == '__main__':
    pass