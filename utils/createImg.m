function createImg()
%20180913-Improvement:Traversing all files in the folder
clc;
clear;

PathRoot = 'E:/primary_school_20180912_2/';
list = dir(fullfile(PathRoot));

fileNum = length(list);
for k = 3:fileNum %From 3 because list includes path . and ..
    disp(list(k).name)
    video_path=strcat('E:/primary_school_20180912_2/', list(k).name);
    video_obj=VideoReader(video_path);

    frame_number=video_obj.NumberOfFrames;

    for i=1:frame_number
        image_name=strcat('E:/data/img/primary_school_20180912_2/im_',k,num2str(i),'.jpg');
        frame=read(video_obj,i);
        if mod(i,10)==0
            imwrite(frame,image_name,'jpg');
        end
    end
end



disp('all images are written into directort image')
    
