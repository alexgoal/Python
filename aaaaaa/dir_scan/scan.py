import os

currentDir = 'D:/Dev/Workspace/Java/rainbow-service'
for dirName, subdirList, fileList in os.walk(currentDir):
    print('%s' % dirName)
    for fname in fileList:
        abspath = dirName + os.sep + fname
        if fname.endswith('java'):
            print(abspath)
