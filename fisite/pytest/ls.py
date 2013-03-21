import os
def lstree(currentPath,count):
    """docstring for lstree"""
    # TODO: write code...
    if not os.path.exists(currentPath):
        return

    if os.path.isfile(currentPath):
        filename =  os.path.basename(currentPath)
        print '\t' * count + '|--'+ filename
    elif os.path.isdir(currentPath):
        print '\t' * count + '|--'+ currentPath
        pathlist = os.listdir(currentPath)
        for eachpath in pathlist:
            lstree(currentPath+'/'+eachpath,count+1)

if __name__ == '__main__':
    lstree('/home/ifcheung/Desktop/Download/',1)
