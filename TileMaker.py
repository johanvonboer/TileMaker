import os
import configparser
import image_slicer
from shutil import copyfile
import cv2

config = configparser.ConfigParser()
config.read('config.ini')

inputMap = config['DEFAULT']['inputMap']
rootTargetDirectory = config['DEFAULT']['rootTargetDirectory']
zoomLevels = int(config['DEFAULT']['zoomLevels'])

if not os.path.exists(rootTargetDirectory):
    os.makedirs(rootTargetDirectory)

baseFactor = 2
originalBaseFactor = baseFactor



def makeTiles():
    global rootTargetDirectory, zoomLevels, baseFactor

    for zl in range(1, zoomLevels):

        rows = baseFactor
        columns = baseFactor
        slices = rows * columns

        print("Processing - Zoom Level:"+str(zl)+" Slices:"+str(slices)+" Columns:"+str(columns)+" Rows:"+str(rows))

        tiles = image_slicer.slice(inputMap, slices, columns, rows, False)
        zlTargetDirectory = "tiles/"+str(zl)

        #make zoomlevel directory if not exists
        if not os.path.exists(zlTargetDirectory):
            os.makedirs(zlTargetDirectory)

        for tile in tiles:
            currentTargetDirectory = rootTargetDirectory+"/"+str(zl)+"/"+str(tile.row-1)
            if not os.path.exists(currentTargetDirectory):
                os.makedirs(currentTargetDirectory)

            tileFilename = str(tile.column-1)+".png";
            #print(currentTargetDirectory+"/"+tileFilename)

            tile.save(filename=currentTargetDirectory+"/"+tileFilename)
            scaleTile(currentTargetDirectory+"/"+tileFilename)
        
        baseFactor = baseFactor * 2



def scaleTile(tilePath):
    img = cv2.imread(tilePath, cv2.IMREAD_UNCHANGED)
    dim = (256, 256)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(tilePath, resized)


#make zoom level 0! (which is just the entire map in 1 image)
rootTilePath = "/0/0"
if not os.path.exists(rootTargetDirectory+rootTilePath):
        os.makedirs(rootTargetDirectory+rootTilePath)

print("Creating root tile")
copyfile(inputMap, rootTargetDirectory+rootTilePath+"/0.png")
scaleTile(rootTargetDirectory+rootTilePath+"/0.png")

print("Making tiles")
makeTiles()

print("DONE!")