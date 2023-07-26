# 调用模块
# （生成随机数模块）
import random
# （显示时间模块）
import time

# 显示时间
t = time.localtime(time.time())
localtime = time.asctime(t)
时间 = "当前时间：" + time.asctime(t)
print(时间)
print("_________________________________________________________________________\n")

# 游戏名
print("                             数字猜猜乐")
print("_________________________________________________________________________\n")

# 让玩家选择难度
nd = input("选择难度（简单：0； 普通：1； 困难：2； 更加困难：3）：")
难度 = int(nd)

# 根据难度设置游戏参数
if 难度 == 0:
    counts = 3
    answer = 作弊答案 = random.randint(1,10)
if 难度 == 1:
    counts = 5
    answer = 作弊答案 = random.randint(1,100)
if 难度 == 2:
    counts = 10
    answer = 作弊答案 = random.randint(1,1000)
if 难度 == 3:
    counts =15
    answer = 作弊答案 = random.randint(1,10000)

# 让玩家输入猜测
temp = input("""不妨猜一下我现在心里想的是哪个数字(输入0即可结束游戏)(输入-1获取提示)(输入-2获取答案)
:""")
guess = int(temp)

# 开始游戏循环
while counts > 0:
    # 提示玩家获取提示
    提示 = -1
    作弊 = -2

    # 显示小飞机
    小飞机 = """猜对啦！
奖励你一架小飞机！           
             @                             
            / \\          
            * *                  
            * *           
            * *                   
        * * * * * *                       
      * * * * * * * *                  
    * * * * * * * * * *                   
            * *                           
            * *                          
          * * * *                      
        * * * * * *
        """
    
    # 判断猜测是否正确
    if guess == answer and answer < 1000:
        print("你是我心里的蛔虫吗？！")
        print("哼，猜中了也没奖励！")
        break
    if guess == answer and answer > 1000:
        print(小飞机)
        break
        
    # 判断玩家是否获取提示
    if guess == 提示:
        if answer > 10 and answer < 100:
            提示数字 = answer // 10
            print("第一位是" + str(提示数字))
        if answer < 10:
            print("是一个个位数")
        if answer > 100 and answer < 1000:
            提示数字 = answer // 100
            print("第一位是" + str(提示数字))
        if answer > 1000 and answer < 10000:
            提示数字 = answer // 1000
            print("第一位是" + str(提示数字))
        else:
            print("提示无效")
    # 判断玩家是否作弊
    if guess == 作弊:
        print("答案是：", 作弊答案)
    else:
        # 判断猜测是否正确
        if guess == 0:
            break
        # 判断猜测是否小了
        if guess < answer and guess!= -1:
            print("猜小了！")
        # 判断猜测是否大了
        if guess > answer and guess!= -1:
            print("猜大了！")
    # 减少机会
    counts = counts - 1
    # 判断是否还有机会
    if counts == 0:
        print("你只剩下最后一次机会了！")
    else:
        print("你还剩下" + str(counts) +"次机会了！")

    # 让玩家继续猜测
    继续 = input("继续猜：")
    guess = int(继续)        
        
# 判断玩家是否猜对
if guess!= answer:
        print("正确答案是" + str(answer) )

# 结束游戏
print("游戏结束，不玩了^_^")
