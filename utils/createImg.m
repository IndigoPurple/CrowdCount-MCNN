function createImg()

clc;
clear;

video_path='/media/richard/eda30030-75b7-4aba-ab13-39e8846fd05a/home/richard/data/shanghai/mcam_14.mp4';
video_obj=VideoReader(video_path);

frame_number=video_obj.NumberOfFrames;

for i=1:frame_number
    image_name=strcat('/media/richard/eda30030-75b7-4aba-ab13-39e8846fd05a/home/richard/data/image_14/im_',num2str(i),'.jpg');
    frame=read(video_obj,i);
    if mod(i,10)==0
        imwrite(frame,image_name,'jpg');
    end
end

disp('all images are written into directort image')
    

