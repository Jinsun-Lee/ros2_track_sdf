#!/usr/bin/env python3

import os
import torch
import rclpy
import warnings
from ultralytics import YOLO
from interfaces_pkg.msg import StudentSpec
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

def main():
    
    rclpy.init()
    node = rclpy.create_node('pub_my_computer_spec')
    
    
    publisher = node.create_publisher(StudentSpec, "computer_spec", 1)
    msg = StudentSpec()
    
    
    user = os.path.basename(os.path.expanduser("~"))
    
    
    model_name = None
    with open('/proc/cpuinfo') as f:
        for line in f:
            if line.strip():
                if line.rstrip('\n').startswith('model name'):
                    model_name = line.rstrip('\n').split(':')[1]
    cpu_model = model_name
    cpu_core = os.cpu_count()
    
    
    from collections import OrderedDict
    meminfo=OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    total_mem = meminfo['MemTotal']
    free_mem = meminfo['MemFree']
    

    gpu_count = 0
    if torch.cuda.is_available():
        gpu_count = torch.cuda.device_count()
    all_gpu_models = ""
    for i in range(gpu_count):
        gpu_name = torch.cuda.get_device_name(i)
        all_gpu_models += gpu_name + " "
    

    model = YOLO('yolov8x-seg.pt', verbose=False)
    results = model.predict(source='https://ultralytics.com/images/bus.jpg') #, device="cpu")
    
    
    pre = results[0].speed['preprocess']
    inf = results[0].speed['inference']
    pos = results[0].speed['postprocess']


    msg.user = user
    msg.cpu_model = cpu_model
    msg.cpu_core = cpu_core
    msg.total_mem = total_mem
    msg.free_mem = free_mem
    msg.gpu_num = gpu_count
    msg.gpu_model = all_gpu_models
    msg.preprocess = pre
    msg.inference = inf
    msg.postprocess = pos
    msg.is_possible = True
    if inf >= 600:
        msg.is_possible = False
    
    publisher.publish(msg)
    
    node.get_logger().info("\n\n조교한테 제출 완료!")
    rclpy.shutdown()
        
if __name__ == '__main__':
    main()
    
