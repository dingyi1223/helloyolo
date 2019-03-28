from voc_eval import voc_eval

import os

current_path = os.getcwd()
results_path = current_path+"/results"
sub_files = os.listdir(results_path)

mAP = []
for i in range(len(sub_files)):
    class_name = sub_files[i].split(".txt")[0]
    #rec, prec, ap = voc_eval('/home/zufall/dy/darknet/results/{}.txt', '/home/zufall/darknet/VOC/VOCdevkit/VOC2007/Annotations/{}.xml', '/home/zufall/retail_product/data/2007_test.txt', class_name, '.')
    rec, prec, ap = voc_eval('/home/zufall/dy/darknet/results/{}.txt', '/home/zufall/dy/darknet/xml/{}.xml', '/home/zufall/retail_product/data/val_only.txt', class_name, '.')
    print("{} :\t {} ".format(class_name, ap))
    mAP.append(ap)

mAP = tuple(mAP)

print("***************************")
print("mAP :\t {}".format( float( sum(mAP)/len(mAP)) ))
