import time as t


class MyTimer:
    # 开始
    def start(self):
        self.begin = t.localtime()
        print("计时开始！...")

    # 停止
    def stop(self):
        self.end = t.localtime()
        print("计时结束！...")

    # 计算
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.stop[index] - self.start[index])
            self.prompt += str(self.lasted[index])
        print(self.prompt)
