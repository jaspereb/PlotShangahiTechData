# This script plots the shanghai tech dataset for checking.
# It will search the dataToPlot folder for GT_*.mat files then try to find a matching .jpg file (same name) and plot the 
# annotations on this image. The image is then saved to the dataPlotted folder. 

import os
import cv2
import argparse
import scipy.io

circleRad = 3
circleColour = (0,0,255)
circleThick = -1

inPath = "./dataToPlot/"
outPath = "./dataPlotted/"

inFiles = sorted(os.listdir(inPath))

for i,file in enumerate(inFiles):
    if(not file.endswith('.mat')):
        continue

    if(not file[0:3] == 'GT_'):
        print("Skipping .mat file missing GT_ prefix: {}".format(file))
        continue

    #find img file
    imName = os.path.splitext(file)[0]
    imName = imName[3:] + '.jpg'

    try:
        I = cv2.imread(os.path.join(inPath,imName))
    except:
        print("Failed to read image {}, does it exist?".format(imName))

    #read GT
    gtMat = scipy.io.loadmat(os.path.join(inPath,file))
    gtMat = gtMat['image_info']
    numberDots = gtMat[0][0][0][0][1][0][0] #how good are matlab structs :-/
    gtMat = gtMat[0][0][0][0][0] #nx2 array

    for n in range(0,gtMat.shape[0]):
        I = cv2.circle(I, (int(gtMat[n][0]),int(gtMat[n][1])), circleRad, circleColour, circleThick)

    assert(n+1 == numberDots)

    cv2.imwrite(os.path.join(outPath,'plotted_'+imName),I)

    if(i%50 == 0):
        print("Processed {} files".format(i))
   
print("All Done")