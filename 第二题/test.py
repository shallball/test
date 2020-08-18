import os
import xml.etree.ElementTree
import numpy as np
files=os.listdir('data')
sum=0
areas=[]
for file in files:
    root=xml.etree.ElementTree.parse('data/'+file).getroot()
    obs=root.findall('object')
    for ob in obs:
        sum+=1
        name=ob.find('name').text
        bbox=ob.find('bndbox')
        xmin=bbox.find('xmin').text
        ymin=bbox.find('ymin').text
        xmax = bbox.find('xmax').text
        ymax = bbox.find('ymax').text
        area=(int(ymax)-int(ymin))*(int(xmax)-int(xmin))
        areas.append(area)

area_max=max(areas)
area_mean=np.mean(areas)
area_var=np.var(areas)
txt=open('../2.txt','r+')
txt.write('总数：%s，平均面积：%s，最大面积：%s，面积的方差：%s'%(sum,area_mean,area_max,area_var))
txt.close()





