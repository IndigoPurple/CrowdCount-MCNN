function getPositionInfo()
%图像标定函数，用来标定图像中的head所在位置
%标定完成后之间点击关闭图像显示框
clc;
clear;
im = imread('F:\Giga\primary_school_20180912_1_img\GT_IMG\im_50.jpg');
g=imresize(im,0.25);
imwrite(g,'F:\Giga2.0\CrowdCount-MCNN\data\original\shanghaitech\part_C_final\images\IMG_366.jpg')
imshow(g);
hold on;
p=[];
try
   while true
     a=ginput(1);
     p=[p;a];
     plot(a(1),a(2),'r*');
   end     
catch  
     b=size(p);
     b=b(1);
     image_info={};
     image_info.location=p;
     image_info.number=b;
     save F:\Giga2.0\CrowdCount-MCNN\data\original\shanghaitech\part_C_final\ground_truth\GT_IMG_366.mat image_info;
end   

