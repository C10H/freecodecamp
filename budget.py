class Category:
    def __init__(self,name):
        self.name=name
        # 题目明确ledger is a list
        self.ledger=[]
        self.funds=0
    # 预存
    def deposit(self,amount,description=''):
        # 格式是题目要求的，且description默认值为空字符
        self.ledger.append({"amount": amount, "description": description})
        self.funds+=amount

    # 消费或者说提取，与deposit函数一样，amount为负数
    # 前提是funds为正数，即有存货，返回True，否则返回False
    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.funds-=amount
            return True
        return False

    def get_balance(self):
        return self.funds

    # other也是一个list
    def transfer(self,amount,other):
        if not self.check_funds(amount):
            return False

        # 转移到other的list中
        # 若发生了转移，funds需要减去这一部分的amount，否则需要加上
        # 若发生了转移，funds可能增加也可能减少，都属于发生了改变，返回True
        self.ledger.append({'amount':-amount,'description':"Transfer to {}".format(other.name)})
        self.funds-=amount
        other.ledger.append({"amount": amount, "description":"Transfer from {}".format(self.name)})
        other.funds+=amount
        return True

    # 根据要求，check_funds用在withdraw()和transfer()中
    def check_funds(self,amount):
        if self.funds>=amount:
            return True
        return False

    # 打印的要求：
    # 标题行30个字符，名称居中，两侧为“*”字符
    # description靠左对齐，最大23位，多余的不显示
    # amount靠右对齐，最大7位，多余的不显示
    # 新增一行Total显示
    def __str__(self):
        s=''
        s+=self.name.center(30,'*')+'\n'
        for x in self.ledger:
            if len(x['description'])>23:
                s+=x['description'][0:23]
            else:
                s+=x['description'][0:23].ljust(23)
            s+="{0:.2f}".format(x['amount']).rjust(7)
            s+='\n'
        s+='Total: {}'.format(self.funds)
        return s

#不是四舍五入，而是舍去个位！
# categories is a list
# chart 显示每个category的花费百分比
# 左侧显示0-100的标签，用'o'字符表示柱高，不是整数的，应该四舍五入到最近的10处
# 水平线应该比最后一个bar空两行
# 每个category的名称在对应的bar下方垂直显示
# 最上方显示标题为"Percentage spent by category"
def create_spend_chart(categories):
    s="Percentage spent by category\n"
    sum=0
    withdraws={}
    # 百分比的计算只包含withdrawals
    for x in categories:
        withdraws[x.name]=0
        for y in x.ledger:
            if y['amount']<0:
                withdraws[x.name]+=y['amount']
        withdraws[x.name]=-withdraws[x.name]
    for x in withdraws:
        sum+=withdraws[x]
    for x in withdraws:
        withdraws[x]=int(withdraws[x]/sum*100)

    for i in range(100,-10,-10):
        s+=str(i).rjust(3)+'| '
        for x in categories:
            if withdraws[x.name]>=i:
                s+='o  '
            else:
                s+='   '
        s+='\n'
    s+=' '*4+'-'*(1+len(categories)*3)+'\n'

    maxlen=0
    for x in categories:
        if len(x.name)>maxlen:
            maxlen=len(x.name)
    for i in range(maxlen):
        s+=' '*5
        for x in categories:
            if len(x.name)>i:
                s+=x.name[i]+'  '
            else:
                s+=' '*3
        s+='\n'
    return s[0:-1]

if __name__ == "__main__":
    food=Category('food')
    entertainment=Category('entertainment')
    business=Category('Business')
    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    actual = create_spend_chart([business, food, entertainment])
    print(actual)