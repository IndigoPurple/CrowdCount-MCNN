function getPositionInfo()

im = imread('./GT_IMG/im_100.jpg');
imshow(im);
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
    save GT_INFO/GT_IMG_101.mat image_info;
end   

