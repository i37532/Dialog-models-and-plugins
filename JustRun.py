# -*- coding: utf-8-*-
#!/usr/bin/env python3

from robot.sdk.AbstractPlugin import AbstractPlugin
from data_publisher import DataPublisher

class Plugin(AbstractPlugin):

    def handle(self, text, parsed):
        self.say('不干了，不干啦，我要跑路啦，世界那么大，我想去看看', cache=True)
        publisher = DataPublisher()
        # 重复发送10次信息
        for _ in range(10):
            # 发送消息到 ZeroMQ 发布者
            # 注意：这里的消息格式可以根据实际需要调整
            message = "status 跑路通知:我不干了"
            publisher.send_message(message)

    def isValid(self, text, parsed):
        return "跑路" in text


