import cv2
import json
import os
import numpy as np

basedir = 'Smoke data annotations/'
imagedir = 'images/' 
mask_outdir = 'masks/'
if not os.path.exists(mask_outdir):
    os.mkdir(mask_outdir)
    
for files in os.listdir(basedir):
    data = json.load(open(os.path.join(basedir,files),'r'))
    imagefn = files.strip().split('.')[0]+'.jpg'
    img = cv2.imread(os.path.join(imagedir, imagefn))
    try:
        x = data[0]['regions'][0]['shape_attributes']['all_points_x']
        y = data[0]['regions'][0]['shape_attributes']['all_points_y']
    except:
        print(files)
        continue
    imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    mask = np.zeros_like(imgray)
    ctr = np.zeros((len(x),2), np.int)
    ctr[:,0] = x
    ctr[:,1] = y
    ctr = ctr.astype(int)
    mask = cv2.drawContours(mask,[ctr],0,(255),-1)
    cv2.imwrite(os.path.join(mask_outdir, imagefn), mask)