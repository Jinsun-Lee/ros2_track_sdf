#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import cv2
from interfaces_pkg.msg import StudentSpec

class SubscriberNode(Node):
    def __init__(self):
        super().__init__("sub_student_computer_spec")
        self.subscription = self.create_subscription(StudentSpec, "computer_spec", self.callback, 10)
        self.count = 0
                       
    def callback(self, msg):
        self.count +=1
        user = msg.user
        cpu_model = msg.cpu_model
        cpu_core = msg.cpu_core
        total_mem = msg.total_mem 
        free_mem = msg.free_mem
        gpu_count = msg.gpu_num
        all_gpu_models = msg.gpu_model
        pre = msg.preprocess
        inf = msg.inference
        pos = msg.postprocess        
        is_ok = msg.is_possible
        if is_ok:
            is_ok = "OK!"
            
        pre = f"Preprocess: {pre:.1f}ms"
        inf = f"Inference: {inf:.1f}ms"
        pos = f"Postprocess: {pos:.1f}ms"
        
        print(f"\n\nNo.{self.count}-----------------------------------")
        print(f"User          : {user}")
        print(f"CPU Core Num  : {cpu_core}")
        print(f"CPU Model     :{cpu_model}")
        print(f"Total Memory  : {total_mem}")
        print(f"Free Memory   : {free_mem}")
        print(f"GPU Count     : {gpu_count}")
        print(f"All GPU Models: {all_gpu_models}")
        print(f"{pre}, {inf}, {pos}")
        print(f">>> {is_ok}")



        
def main(args=None):
    print("토픽 computer_spec을 subscribe합니다")
    
    rclpy.init(args=args)
    node = SubscriberNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\n\nshutdown\n\n")
        pass
    node.destroy_node()
    cv2.destroyAllWindows()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()    
