import copy
import random
# Consider using the modules imported above.
 
# 常见的2个参数 *args,**kwargs，*args是非关键字参数，用于元组，**kw是关键字参数，用于字典
#  **kwargs：
# 关键标志为星号**，名称可以随意。
# 当传入函数中的参数个数未知但需要知道参数的名称时，使用**kw。
# 传入函数中的几个参数组成字典。
 
 
class Hat:
    def __init__(self, **balls):
        self.contents = []
        # i 表示某个颜色的球
        # balls[i]表示该颜色球的个数
        # j循环表示在contents中添加j个该颜色的元素
        for i in balls:
            # print('i:', i)
            for j in range(balls[i]):
                self.contents.append(i)
                # print('contents:', self.contents)
 
    def draw(self, number):
        if number >= len(self.contents):
            temp = self.contents.copy()
            self.contents.clear()
            return temp
        temp = []
        # 在0到contents中球的数量之间生成一个随机数
        # 作为下标，取出对应的球contents[n]放入temp数组中
        # 并从原contents中删除，因为是不放回抽取
        for i in range(number):
            n = random.choice(range(0, len(self.contents)))
            temp.append(self.contents[n])
            self.contents.pop(n)
        return temp
 
 
# expected_balls是字典，expected_balls[j]得到的实际上是每个球对应的数量
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        for j in expected_balls:
            # print('expected_balls[j]:', expected_balls[j])
            # print('count(j):', drawn.count(j))
            if expected_balls[j] > drawn.count(j):
                count -= 1
                break
        count += 1
    return count/num_experiments
