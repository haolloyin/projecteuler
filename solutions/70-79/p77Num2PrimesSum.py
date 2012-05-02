
# coding=utf-8
"""
Project Euler - Problem 77
Created at: 2011-06-14 12:38:38
"""

import time

start = time.time()

HUNDRED = 10
all = [i for i in range(HUNDRED - 1, 0, -1)]

count = len(all)
solution = [0] * count
answer = 0

def testSolution(solution):
    """
    测试所给取法 solution 是否正确，若错误则立即退出程序
    """
    global all
    if sum([all[i] * solution[i] for i in range(count)]) != HUNDRED:
        print " NO ..."
        exit()

def find(value, next, solution):
    """
    根据给定面值 value，下一个待取面值的下标 next
    和当前取法 solution 递归探寻
    """
    global all
    coins = all[next: ] # 所有待取出的面值
    i = next
    for c in coins:
        remain = value - c # 剩余面值
        solution[i] += 1 # 假设当前面值 c 可取
        if remain > 0:
            find(remain, i, solution) # 递归，从当前面值往下查找
        elif remain < 0:
            solution[i] -= 1 # 不可取
        else:
            global answer
            answer += 1
            print answer, ":", solution
            testSolution(solution) # 测试当前取法是否正确
            solution[i] -= 1 # 撤销当前选择的面值    
        i += 1
    solution[next] -= 1
        

find(HUNDRED, 0, solution)

print "%.8f Secs" % (time.time() - start)
print "Answer:", answer
print "Solved at:", time.asctime()

