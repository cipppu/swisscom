#!/usr/bin/python
import os

def print_directory_contents(sPath):
    for name in os.listdir(sPath):
        sPath = os.path.join(sPath, name)
        if os.path.isfile(sPath):
            print sPath
        else:
            scan_dir(sPath)

print_directoy_contents(sPath)










"""the os.walk way """ 


#import os

#for root, dirs, files in os.walk("."): 
#    for filename in files:
#        print(filename) 

