__author__ = 'gaohuiyu'

from PIL import Image
import os, shutil

def moveImage(fileName):
    image = Image.open(fileName)
    directory = str(image.size[0])+'x'+str(image.size[1])
    abspath = os.path.abspath('.')
    if os.path.exists(abspath+'\\'+directory) == False:
        os.mkdir(abspath + '\\' + directory)
    image.close()
    shutil.move(abspath+'\\'+fileName, abspath+'\\'+directory+'\\'+fileName)

def justMoveImage():
    filesName = [x for x in os.listdir('.') if os.path.isfile(x)]
    for i in filesName:
        try:
            moveImage(i)
        except IOError:
            pass

if __name__ == '__main__':
    justMoveImage()