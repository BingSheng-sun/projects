def ptp(data):
    """极差（全距）"""
    return max(data) - min(data)

def mean(data):
    """算术平均"""
    return sum(data) / len(data)

def median(data):
    """中位数"""
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size //2]
    else:
        return mean(temp[size //2 -1:size // 2+1])
    
def var(data, ddof=1):
    """方差"""
    x_bar = mean(data)
    temp = [(num - x_bar) ** 2 for num in data]
    return sum(temp) / (len(data) - ddof)

def std(data, ddof=1):
    """标准差"""
    return std(data, ddof) / mean(data)

def cv(data, ddof=1):
    """变异系数"""
    return std(data, ddof) / mean(data)

def describe(data):
    """输出描述性统计信息"""
    print(f'均值：{mean(data)}')
    print(f'中位数：{median(data)}')
    print(f'极差：{ptp(data)}')
    print(f'方差：{var(data)}')
    print(f'标准差：{std(data)}')
    print(f'变异系数：{cv(data)}')

import statistics
