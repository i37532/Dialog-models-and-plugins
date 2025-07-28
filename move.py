#!/usr/bin/env python3
# -*- coding: utf-8-*-

from robot.sdk import unit
from robot.sdk.AbstractPlugin import AbstractPlugin
from data_publisher import get_publisher

class Plugin(AbstractPlugin):

    def handle(self, text, parsed):
        slots = unit.getSlots(parsed, 'DIRECTION_DISTANCE')  # 取出所有词槽
        # 遍历词槽，找出 user_person 对应的值
        for slot in slots:
            if slot['name'] == 'user_move':
                for slot2 in slots:
                    if slot2['name'] == 'user_move_distance':
                            direction = slot['normalized_word']  # 方向
                            distance = slot2['normalized_word']  # 距离
                            msg = '向{}移动{}'.format(direction, distance)
                            self.say(msg, cache=True)
                            # self.say('好的，向{}移动{}！'.format(slot['normalized_word'],int(slot2['normalized_word'])))
                            publisher = get_publisher()
                            while True:
                                message = f"status 移动通知:{direction} {distance}"
                                print(f"发送消息: {message}")
                                if publisher.send_message(message):
                                    break
                            return
        # 如果没命中词槽，说 hello world
        self.say('hello world!', cache=True)

    def isValid(self, text, parsed):
        # 判断是否包含 HELLO_WORLD 意图
        return unit.hasIntent(parsed, 'DIRECTION_DISTANCE')

