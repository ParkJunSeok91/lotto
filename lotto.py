__author__ = 'user'

import random
import time

class Lotto:
    def pickup(self):
        self.lotto = random.sample(range(1,46), 6)
        self.lotto.sort()
    def show(self):
        print(self.lotto)

print('공을 굴리고 있습니다')
time.sleep(1)
lotto = Lotto()
print('공 6개를 추첨하겠습니다')
time.sleep(1)
lotto.pickup()
lotto.show()
print('추첨이 끝났습니다 당신은 꽝이겠지요ㅋㅋㅋ다음 기회에 ....')
