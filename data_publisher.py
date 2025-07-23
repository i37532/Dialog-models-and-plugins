#!/usr/bin/env python3

import zmq

class DataPublisher:
    def __init__(self, address="tcp://192.168.110.203:5556"):
        # 创建 ZeroMQ 上下文
        self.context = zmq.Context()
        # 创建一个 PUB 套接字（发布者）
        self.socket = self.context.socket(zmq.PUB)
        # 绑定端口：在本地发布数据（绑定一次即可）
        self.socket.bind(address)
        print("数据发布器启动中...")

    def send_message(self, message):
        # 发送带“话题”的消息
        self.socket.send_string(message)
        print("已发送：", message)
