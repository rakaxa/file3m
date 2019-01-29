import os
import sys
import glob

if __name__ == '__main__':
  if len(sys.argv) != 2:
    quit("usage : > python3 file3Mdel.py [directoryName]")    
  for file in glob.glob(sys.argv[1] + '/*.*'):
    if os.path.getsize(file) > 3000000:
      os.remove(file)

