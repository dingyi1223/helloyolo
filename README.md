# helloyolo
新手小白的第一次记录。

- 这是项目 [helloyolo](https://github.com/dingyi1223/helloyolo) ，欢迎访问。

- 这个项目的版本库是 **Git格式** ，在 Windows、Linux、Mac OS X
平台都有客户端工具可以访问。虽然版本库只提供Git一种格式，
但是你还是可以用其他用其他工具访问，如 ``svn`` 和 ``hg`` 。

- 使用darknet框架

### 步骤
- [x] 环境配置
- [x] train
- [x] 批量test
- [x] 批量valid
- [x] recall
- [ ] 计算mAP
- [ ] 待续

## 版本库地址

支持三种访问协议：

* HTTP协议: `https://github.com/dingyi1223/helloyolo.git` 
* Git协议: `git://github.com/dingyi1223/helloyolo.git` 
* SSH协议: `ssh://git@github.com/dingyi1223/helloyolo.git` 

## 克隆版本库

操作示例：

    $ git clone git://github.com/dingyi1223/helloyolo.git


# 环境配置
### darknet下载:
[官网](https://pjreddie.com/darknet/yolo)

```
git clone https://github.com/pjreddie/darknet
cd darknet
make
```

### YOLO GPU配置
[参考](https://blog.csdn.net/luoying_ontheroad/article/details/81136973)

1.打开darknet/MakeFile文件，将`GPU=0 --> GPU=1`

2.`CUDNN=0 --> CUDNN=1`

3.`NVCC=/usr/local/cuda-9.0/bin/nvcc`（这里nvcc所在位置注意修改成自己的）

4.在darknet中重新`make`

# train
[darknet53.conv.74](https://pjreddie.com/media/files/darknet53.conv.74)

`./darknet detector train cfg/voc.data cfg/yolov3-voc.cfg darknet53.conv.74`

- 需要修改cfg/voc.data中train的路径：`train  = <path-to-voc>/train.txt`
- 如果需要把终端信息记录到文件，使用命令`| tee train_log.txt`
- 训练好的weights文件保存在backup文件夹中
- 直接下载训练好的weights,[yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)

# test
### 单个图像文件test
`./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights data/dog.jpg`

结果保存在`prediction.jpg`中。可以加`-out aa.jpg`自己另存为

### 批量test
需要修改`/example/detector.c`源码中的`test_detector`函数

[参考链接1](https://blog.csdn.net/cgt19910923/article/details/80528559)
[参考链接2](https://blog.csdn.net/mieleizhi0522/article/details/79989754)

- 每次修改后需要重新make
- `strncpy(b, filename+33, strlen(filename)-37);`这一行需要根据文件名字和地址的字符串个数改变，长度不符合的话会出现乱码
-  第630行`sprintf(newfile,"/home/zufall/dy/darknet/outfiletest/%s", b);`修改成保存结果的路径
- 批处理的图片用路径写在`name.txt`中,放在darknet文件夹下`ls -R /.../*.jpg > name.txt`
- 问题：跑完一次./darknet之后再make，再跑，会出现GPU显存不足问题。解决： `nvidia-smi` 然后`sudo kill -9 PID号`.。或者用`CTRL+C`退出darknet的运行，不要用`ctrl+D`！
- test三个参数：data,cfg,weights

`./darknet detector test /home/<your_path>/cfg/voc.data /home/<your_path>/cfg/yolov3-voc.cfg /home/<your_path>/backup/yolov3.weights`

# valid

`./darknet detector valid /home/<your_path>/cfg/voc.data /home/<your_path>/cfg/yolov3-voc.cfg /home/<your_path>/backup/yolov3.weights -out ''`

结果在results文件夹中，一个类一个txt文件.按列，分别为：图像名称 | 置信度 | xmin,ymin,xmax,ymax

# recall

需要修改`/example/detector.c`源码中的`validate_detector_recall`函数

[参考链接](https://blog.csdn.net/mieleizhi0522/article/details/79989754)

`./darknet detector recall /home/<your_path>/cfg/voc.data /home/<your_path>/cfg/yolov3-voc.cfg /home/<your_path>/backup/yolov3.weights`

# 基于VOC的mAP计算

[参考链接](https://blog.csdn.net/amusi1994/article/details/81564504)

1.valid，生成results/{}.txt

2.[voc_eval.py](https://github.com/rbgirshick/py-faster-rcnn/tree/master/lib/datasets)

3.新建compute_mAP.py

```python2 compute_mAP.py```
    
   **参数：**
    
   - valid生成的txt
   - 标注的原始xml文件
   - 验证集txt文本路径，注意只有名字没有前后缀
   - 待验证的类别名
   - pkl文件的路径。在python2环境下运行compute_mAP.py会在当前路径下生成annots.pkl。如果换了数据集或者换了新的类别需要删除掉，再重新生成。
 
 4.**直接计算出所有单类别的mAP和总的mAP**
 `python computer_Single_ALL_mAP.py `
 
 
