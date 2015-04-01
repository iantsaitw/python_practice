from subprocess import call
import os
import re

skip_hidden =  re.compile('^\.')

call(["echo","Sample ..."])
os.chdir("/srv/shared")
call(["ls", "-l"])
for dirPath, dirNames, fileNames in os.walk("/home/yntsai"):
    if not skip_hidden.match(dirPath):
        print dirPath
        for f in fileNames:
            print os.path.join(dirPath, f)
