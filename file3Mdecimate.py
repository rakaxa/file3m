import os
import sys
import glob
from PIL import Image

if __name__ == '__main__':
  if len(sys.argv) != 2:
    quit("usage : > python3 file3Mdecimate.py [directoryName]")    
  for file in glob.glob(sys.argv[1] + '/*.*'):
    if os.path.getsize(file) > 3000000:
      im = Image.open(file)
      for q in range(100, 1, -1):
        savefile = file + str(q) + ".jpg"
        im.save(savefile, 'JPEG', quality = q)
        if os.path.getsize(savefile) <= 3000000:
          os.remove(file)
          break
        else:
          os.remove(savefile)
#      os.remove(file)
