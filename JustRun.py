# -*- coding: utf-8-*-
from robot.sdk.AbstractPlugin import AbstractPlugin

class Plugin(AbstractPlugin):

    def handle(self, text, parsed):
        self.say('不干了，不干啦，我要跑路啦，世界那么大，我想去看看', cache=True)

    def isValid(self, text, parsed):
        return "跑路" in text

