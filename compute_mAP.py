from voc_eval import voc_eval
#import _pickle as cPickle
#import numpy as np
#np.seterr(divide='ignore', invalid='ignore')

rec,prec,ap = voc_eval('/home/zufall/dy/darknet/results/{}.txt', '/home/zufall/darknet/VOC/VOCdevkit/VOC2007/Annotations/{}.xml', '/home/zufall/retail_product/data/2007_test.txt', 'person', '.')

print('rec',rec)
print('prec',prec)
print('ap',ap)
