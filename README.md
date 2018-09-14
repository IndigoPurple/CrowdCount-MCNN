### 使用MCNN进行Crowd Counting

---

> 安志成
>
> github地址：https://github.com/IndigoPurple/CrowdCount-MCNN

```
本文主要基于https://github.com/svishwa/crowdcount-mcnn；
该项目是对CVPR 2016 paper "Single Image Crowd Counting via Multi Column Convolutional Neural Network"的实现；
我们希望使用这个已经比较成熟的模型来对我们的data set进行测试，查看其方法对我们的数据集进行crowd counting的效果如何！
* 我们的程序对其源代码进行了改写，将其从2.7版本的python改为3.6版本
```

#### 一、 环境搭建

首先要搭建深度学习的环境，本项目采用的环境配置如下：

- Ubuntu16.04 （win10系统下也可）
- python 3.6
- anaconda
- nvidia cuda 9.2
- cudnn for cuda 9.2
- pytorch

```
具体搭建过程可参考博客
https://blog.csdn.net/Mrx_Nh/article/details/79888928
但是一些版本应根据自己主机配置进行更改（如NVIDIA驱动）
```

#### 二、运行测试

原文基于ShanghaiTech数据集进行了测试和训练，得到了较好的训练效果，我们首先测试程序能否在该数据集上正常运行。

1. 运行data_preparation文件夹下的create_gt_test_set_shtech.m，生成ground_truth_csv文件
2. 运行test.py，如果缺少相关package，添加进项目即可
3. 如果运行成功，可在output文件夹下查看生成的density map
4. 运行train.py，可以看到在迭代循环过程中，MSE和MAE在不断变化，待其趋于稳定后，停止程序

### 三、构建自有数据集

使用我们自己的采集到的视频构建数据集，构建过程主要包含以下两个MATLAB脚本：

1. createImg.m 用于将视频分成图片帧
2. getPositionInfo.m 用于标定图中head位置，生成ground_truth文件

#### 四、 Fine Tune

...









