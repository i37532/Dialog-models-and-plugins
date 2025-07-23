#!/usr/bin/env python3

import zmq
import time

# 创建 ZeroMQ 上下文
context = zmq.Context()

# 创建一个 PUB 套接字（发布者）
socket = context.socket(zmq.PUB)

# 绑定端口：在本地发布数据（绑定一次即可）
socket.bind("tcp://192.168.110.203:5556")

print("数据发布器启动中...")

while True:
    # 模拟要发送的数据（可以替换为真实传感器或状态数据）
    message = "status 速度:1.23 姿态:0.56"
    
    # 发送带“话题”的消息（这里话题是 status）
    socket.send_string(message)
    print("已发送：", message)

    time.sleep(0.1)  # 每 100ms 推送一次

