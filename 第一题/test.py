import json
import cv2
import glob,os

txt_dirs = glob.glob(os.path.join('data', '*.txt'))
for dir in txt_dirs:
    dir0=dir
    dir1=dir.replace('txt','jpg')
    dir2=dir1.replace('data','../clip')
    dir3=dir1.replace('data', '../data_106')
    dir4=dir1.replace('data', '../clip_106')
    with open (dir0,'r') as fp:
        data=json.load(fp)
        rect=data['stMobile106'][0]['face106']['rect']
        left=rect['left']
        top=rect['top']
        right=rect['right']
        bottom=rect['bottom']

        image=cv2.imread(dir1)
        image1=image[top:bottom,left:right,:]
        cv2.imwrite(dir2, image1)

        pointsArray = data['stMobile106'][0]['face106']['pointsArray']
        for point in pointsArray:
            x = point['x']
            y = point['y']
            image[int(y), int(x)] = 0
        cv2.imwrite(dir3,image)
        image2=image[top:bottom,left:right,:]
        height=image2.shape[0]
        width=image2.shape[1]
        image3=cv2.resize(image2,(width*2,height*2))
        cv2.imwrite(dir4,image3)
