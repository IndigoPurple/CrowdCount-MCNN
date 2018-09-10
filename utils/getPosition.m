function  getPosition()

clear;
clc;
im = imread('./GT_IMG/im_100.jpg');
imshow(im);
hold on;
[x,y]=ginput;
a=[x,y];
b=size(x);
b=b(1);
image_info={};
image_info.location=a;
image_info.number=b;
save GT_INFO/GT_IMG_100.mat image_info;
disp("done");
