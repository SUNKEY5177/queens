import numpy as np


def queen(queen_list, result, current_column=0):
    for row in range(len(queen_list)):
        # 如果已至最后一列，则打印结果，跳出递归
        if current_column == len(queen_list):
            for i in range(len(queen_list)):
                result += [[i, queen_list[i]]]
                # print("[%d, %d]," % (i, queen_list[i]), end=" ")
            return
        # flag为可行性的标记
        queen_list[current_column], flag = row, True
        # 对当前列之前的各列进行遍历
        for column in range(current_column):
            # 排除同行及对角线上的位置，将flag设置为False
            if (queen_list[column] == row) or (abs(row - queen_list[column]) == current_column - column):
                flag = False
                # 只要有一个不满足的条件，就跳出遍历
                break
        # 如果可以放置，则递归调用自身，对下一列进行筛选
        if flag:
            queen(queen_list, result, current_column + 1)
    return result


def trigger(size):
    res = queen([None] * size, result=[])
    res_arr = []
    for i in range(len(res) // size):
        res_arr += [res[i * size:i * size + size]]
    return res_arr

