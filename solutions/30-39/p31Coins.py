
# coding=utf-8

# Project Euler - Problem 31
# Created at: 2011-06-13 17:35:04

import time

start = time.time()

all = [200, 100, 50, 20, 10, 5, 2, 1]
count = len(all)
solution = [0] * count
answer = 0

def testSolution(solution):
    """
    测试所给取法 solution 是否正确，若错误则立即退出程序
    """
    global all
    if sum([all[i] * solution[i] for i in range(count)]) != 200:
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
            #print answer, ":", solution
            #testSolution(solution) # 测试当前取法是否正确
            solution[i] -= 1 # 撤销当前选择的面值    
        i += 1
    solution[next] -= 1
        

find(200, 0, solution)

print "%.8f Secs" % (time.time() - start)
print "Answer:", answer
print "Solved at:", time.asctime()

"""
3.70740104 Secs
Answer: 73682
Solved at: Mon Jun 13 19:26:24 2011

You are the 18939th person to have solved this problem.
"""
