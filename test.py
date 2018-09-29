import os
import torch
import numpy as np
import cv2

from src.crowd_count import CrowdCounter
from src import network
from src.data_loader import ImageDataLoader
from src import utils

torch.backends.cudnn.enabled = True
torch.backends.cudnn.benchmark = False
vis = False
save_output = True

model_path = './final_models/mcnn_shtechC_30.h5'

output_dir = './output/'
model_name = os.path.basename(model_path).split('.')[0]
file_results = os.path.join(output_dir,'results_' + model_name + '_.txt')
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
output_dir = os.path.join(output_dir, 'density_maps_' + model_name)
if not os.path.exists(output_dir):
    os.mkdir(output_dir)


net = CrowdCounter()

trained_model = os.path.join(model_path)
network.load_net(trained_model, net)
net.cuda()
net.eval()
mae = 0.0
mse = 0.0

input_video_name = '.\\data\\render_sharpen.mp4'
cap = cv2.VideoCapture(input_video_name)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('.\\data\\render_sharpen_density.mp4', fourcc, 10.0, (480, 270))
ind = 0

while (True):
    ret, frame = cap.read()
    if (ret == True):
        # frame = cv2.resize(frame, (800, 600))
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = img.astype(np.float32, copy=False)
        ht = img.shape[0]
        wd = img.shape[1]
        ht_1 = int(ht/4)*4
        wd_1 = int(wd/4)*4
        img = cv2.resize(img,(wd_1,ht_1))
        img = img.reshape((1,1,img.shape[0],img.shape[1]))
        density_map = net(img)
        density_map = density_map.data.cpu().numpy()
        et_count = np.sum(density_map)
        print(et_count)
        density_map_color = np.uint8(255*density_map/np.max(density_map))
        density_map_color = density_map_color[0][0]
        density_map_color = cv2.cvtColor(density_map_color, cv2.COLOR_GRAY2BGR)
        out.write(density_map_color)
        # utils.save_density_map(density_map, '', 'data\\output_%04d.png' % ind)
        ind = ind + 1
    else:
        out.release()
        break 



# #load test data
# data_loader = ImageDataLoader(data_path, gt_path, shuffle=False, gt_downsample=True, pre_load=True)

# for blob in data_loader:                        
#     im_data = blob['data']
#     gt_data = blob['gt_density']
#     density_map = net(im_data, gt_data)
#     density_map = density_map.data.cpu().numpy()
#     gt_count = np.sum(gt_data)
#     et_count = np.sum(density_map)
#     mae += abs(gt_count-et_count)
#     mse += ((gt_count-et_count)*(gt_count-et_count))
#     if vis:
#         utils.display_results(im_data, gt_data, density_map)
#     if save_output:
#         utils.save_density_map(density_map, output_dir, 'output_' + blob['fname'].split('.')[0] + '.png')
        
# mae = mae/data_loader.get_num_samples()
# mse = np.sqrt(mse/data_loader.get_num_samples())
# print ('\nMAE: %0.2f, MSE: %0.2f' % (mae,mse))

# f = open(file_results, 'w') 
# f.write('MAE: %0.2f, MSE: %0.2f' % (mae,mse))
# f.close()