import cv2
import os
import numpy as np
import sys
import argparse
import shutil
import pdb
import copy


'''
python3 gt_viz.py --root_dir=/mnt/lsxu/work/datasets/dealed_multi_task_big_dataset  --index=0  --list_file='aug_balanced_samples.txt'
python3 gt_viz.py --root_dir=/mnt/lsxu/work/datasets/bus_aug --index=0 --list_file=bus_aug.txt
python3 gt_viz.py --root_dir=/mnt/lsxu/work/datasets/det_seg_aug --index=0 --type=det_seg --list_file=det_seg_aug.txt
'''


seg_color = [[255,0,0], #blue 1
             [0,255,0], #green 2
             [0,0,255], #red 3
             [255,255,0] #cyan 4
             ]


def read_label(img, label_path):
    if not os.path.exists(label_path):
        return False
    lines = [l.strip() for l in open(label_path, 'r').readlines()]
    for line in lines:
        label, x, y, w, h = line.split()
        if(int(label) == 0):
            cv2.rectangle(img, (int(float(x)-float(w)/2), int(float(y)-float(h)/2)), \
                (int(float(x)+float(w)/2), int(float(y)+float(h)/2)), (0, 255, 0), 2)
        elif(int(label) == 1):
            cv2.rectangle(img, (int(float(x)-float(w)/2), int(float(y)-float(h)/2)), \
                (int(float(x)+float(w)/2), int(float(y)+float(h)/2)), (255, 0, 0), 2)
        elif(int(label) == 2):
            cv2.rectangle(img, (int(float(x)-float(w)/2), int(float(y)-float(h)/2)), \
                (int(float(x)+float(w)/2), int(float(y)+float(h)/2)), (0, 0, 255), 2)
    return True

def read_seg_label(img, lane_path, freespace_path):
    print(img_path)
    lane_label = cv2.imread(lane_path, cv2.IMREAD_GRAYSCALE)
    if lane_label is None:
        print("failed to read {}".format(lane_path))
        return False

    freespace_label = cv2.imread(freespace_path, cv2.IMREAD_GRAYSCALE)
    if lane_label is None:
        print("failed to read {}".format(freespace_label))
        return False
    img[freespace_label != 0] = [255,255,255]
    for i in range(1,5):
        img[lane_label == i] = seg_color[i-1]
    
    return True


def write_label(img, label_path, label_dst_path, direction, mouse_x, mouse_y):
    lines = [l.strip() for l in open(label_path, 'r').readlines()]
    label_context = ''
    for line in lines:
        label, x, y, w, h = line.split()
        if(abs(mouse_x - float(x)) < float(w)/2 and \
            abs(mouse_y - float(y)) < float(h)/2):
            new_label = int(label) + direction
            if new_label >= 3:
                new_label=0
            elif new_label < 0:
                new_label = 2
            label_context += str(new_label) + ' ' + x + ' ' + y + ' ' + w + ' ' + h + '\n'
        else:
            label_context += label + ' ' + x + ' ' + y + ' ' + w + ' ' + h + '\n'
    label_txt_file = open(label_path, 'w')

    label_txt_file.write(label_context)
    label_txt_file.flush()

    shutil.copyfile(label_path, label_dst_path)

def creating_bbox(img, label_path, label_dst_path, new_label, bbox_x1, bbox_y1, w1,h1):
    lines = [l.strip() for l in open(label_path, 'r').readlines()]
    label_context = ''
    for line in lines:
        label, x, y, w, h = line.split()
        label_context += label + ' ' + x + ' ' + y + ' ' + w + ' ' + h + '\n'
    new_center_x = bbox_x1 + int(w1/2)
    new_center_y = bbox_y1 + int(h1/2)
    label_context += new_label + ' ' + str(new_center_x) + ' ' + str(new_center_y) + ' ' + str(w1) + ' ' + str(h1) + '\n'
    label_txt_file = open(label_path, 'w')

    # label_txt_dst_file = open(label_dst_path, 'w')
    label_txt_file.write(label_context)
    label_txt_file.flush()

    shutil.copyfile(label_path, label_dst_path)


def write_seg_label(img, seg_path_, direction, mouse_x, mouse_y):
    print(seg_path_)
    if lane_label is None:
        print("failed to read {}".format(label_path))
        return

    freespace_path = "./labels/task_segmentation/FreespaceLabels/" + seg_path_[:-4] + '_rcb.png'
    freespace_label = cv2.imread(freespace_path, cv2.IMREAD_GRAYSCALE)
    if lane_label is None:
        print("failed to read {}".format(freespace_label))
        return

    point_label = lane_label[mouse_y,mouse_x]
    point_label_ori = point_label
    new_label = 100
    if point_label != 0:
        labeling_common_link_zone(img, lane_label, mouse_x, mouse_y, point_label, new_label)
        if direction == 1:
            point_label +=1
        else:
            point_label -=1
        if point_label == 0:
            point_label = 4
        if point_label == 5:
            point_label = 1
        lane_label[lane_label == new_label] = point_label
        cv2.imwrite(seg_dst_path,lane_label)

    img[freespace_label != 0] = [255,255,255]

    for i in range(1,5):
        img[lane_label == i] = seg_color[i-1]
    #img[freespace_label != 0] = 80

def mouse_event(event,x,y,flags,param):
    global ix, iy, creating_box, bbox_x1, bbox_y1
    if event==cv2.EVENT_LBUTTONDOWN:
        if(flags == 17): #shift signal
            write_label(img, label_path, label_dst_path, 1, x, y)
            write_seg_label(img,seg_path,1,x, y)
            read_label(img, label_path)
            cv2.imshow('image', img)
        elif(flags == 9): #ctrl signal
            write_label(img, label_path, label_dst_path, -1, x, y)
            write_seg_label(img,seg_path,-1,x,y)
            read_label(img, label_path)
            cv2.imshow('image', img)
        else:
            creating_box = True
            bbox_x1 = x
            bbox_y1 = y
            print(bbox_x1, bbox_y1)
            #write_label(img, label_path, label_dst_path, '0', x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if creating_box is True:
            img_clone = copy.deepcopy(img)
            cv2.rectangle(img_clone, (int(bbox_x1), int(bbox_y1)), (int(x), int(y)), (0, 0, 255), 2)
            cv2.imshow('image',img_clone)
        else:
            img_clone = copy.deepcopy(img)
            cv2.line(img_clone,(0,y),(img_clone.shape[1],y),(255,255,255),2)
            cv2.line(img_clone,(x,0),(x,img_clone.shape[0]-1),(255,255,255),2)
            cv2.imshow('image', img_clone)
    elif event == cv2.EVENT_LBUTTONUP:
        if creating_box is True:
            w = x - bbox_x1
            h = y- bbox_y1
            print(bbox_x1, bbox_y1, w ,h)
            if w >=5 and h >=5:
                creating_bbox(img, label_path, label_dst_path, '0', bbox_x1, bbox_y1, w,h)
                read_label(img, label_path)
                cv2.imshow('image', img)
            creating_box = False


file_path_index = 0
global img,label_path,seg_path,label_dst_path, seg_dst_path,lane_label
global creating_box, bbox_x1, bbox_y1
creating_box = False
bbox_x1 = -1
bbox_y1 = -1
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--root_dir',dest='root_dir',required=False,help='example: -p ./input_wrong_label_list_path.txt')
parser.add_argument('--index',dest='start_index',required=False,type=int, help='example: --index 16')
parser.add_argument('--list_file', dest='list_file')
parser.add_argument('--type', dest="type", required=False, type=str, default='det', help="ground truth type")
args = parser.parse_args()
if(args.start_index == None):
    file_path_index = 0
else:
    file_path_index = args.start_index

root_dir = args.root_dir
list_file = args.list_file
list_file = os.path.join(root_dir, list_file)
gt_type = args.type
gt_lines = []
count = 0
with open(list_file, 'r') as fp_list:
    line = fp_list.readline()
    while line:
        count += 1
        if count % 1000 == 0:
            print("%d data dealed!" % count)

        gt_lines.append(line)
        line = fp_list.readline()



cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_event)
pause = True
while(1):
    line = gt_lines[file_path_index]
    gt_items = line.split(' ')
    img_path = os.path.join(root_dir, gt_items[0])
    img = cv2.imread(img_path.strip())

    if gt_type == 'det':
        label_path = os.path.join(root_dir, gt_items[1].strip())
        flag_bbox = read_label(img, label_path)
    elif gt_type == 'seg':
        seg_path = os.path.join(root_dir,gt_items[2].strip())
        lane_seg_path = os.path.join(root_dir, gt_items[1].strip())
        flag_seg = read_seg_label(img, lane_seg_path, seg_path)
    else:
        label_path = os.path.join(root_dir, gt_items[3].strip())
        seg_path = os.path.join(root_dir,gt_items[2].strip())
        lane_seg_path = os.path.join(root_dir, gt_items[1].strip())
        flag_seg = read_seg_label(img, lane_seg_path, seg_path)
        flag_bbox = read_label(img, label_path)
    cv2.imshow('image', img)
    if pause is True:
        k=cv2.waitKey(0)
        if k==ord('z'):
            if(file_path_index == 0):
                continue
            else:
                file_path_index-=1
        elif k == ord('r'):  # run
            pause = False
        elif k==ord('x'):
            file_path_index+=1
            if(file_path_index == len(gt_lines)):
                print("annotation check game over !")
                break
        elif k==ord('q'):
            print("quit from nullmax annotation check tool!")
            wrong_label_file.close()
            break
    else:
        k=cv2.waitKey(200)
        file_path_index += 1
        if k == ord('p'): #pause
            pause = True
cv2.destroyAllWindows()
