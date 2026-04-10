---
tags:
  - python
---
# Preliminaries

我更改了NumPy和Pandas中的默认控制台输出设置，以提升整本书的可读性和简洁性。例如，你可能会看到数字数据中印有更多精度的数字。为了完全匹配书中展示的输出，你可以先执行以下 Python 代码再运行代码示例：

```
import numpy as np
import pandas as pd
pd.options.display.max_columns = 20
pd.options.display.max_rows = 20
pd.options.display.max_colwidth = 80
np.set_printoptions(precision=4, suppress=True)
```

Python 社区已经为常用模块采用了多种命名规范：

```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm
```

# 04 Numpy 基础

Numerical Python

Numpy 的数组对象作为数据交换的通用语。

NumPy的部分功能如下：  
- ndarray，一个具有矢量算术运算和复杂广播能力的快速且节省空间的多维数组。  
- 用于对整组数据进行快速运算的标准数学函数（无需编写循环）。  
- 用于读写磁盘数据的工具以及用于操作内存映射文件的工具。  
- 线性代数、随机数生成以及傅里叶变换功能。  
- 用于集成由C、C++、Fortran等语言编写的代码的A C API。

对于大部分数据分析应用而言，我最关注的功能主要集中在：  
- 用于数据整理和清理、子集构造和过滤、转换等快速的矢量化数组运算。  
- 常用的数组算法，如排序、唯一化、集合运算等。  
- 高效的描述统计和数据聚合/摘要运算。  
- 用于异构数据集的合并/连接运算的数据对齐和关系型数据运算。  
- 将条件逻辑表述为数组表达式（而不是带有if-elif-else分支的循环）。  
- 数据的分组运算（聚合、转换、函数应用等）。

NumPy之于数值计算特别重要的原因之一，是因为它可以高效处理大数组的数据。这是因为：  
- NumPy是在一个连续的内存块中存储数据，独立于其他Python内置对象。NumPy的C语言编  
- 写的算法库可以操作内存，而不必进行类型检查或其它前期工作。比起Python的内置序列，  
- NumPy数组使用的内存更少。  
- NumPy可以在整个数组上执行复杂的计算，而不需要Python的for循环。

## 4.1 NumPy的ndarray：一种多维数组对象

其语法跟标量元素之间的运算一样
> ❓ and what is 标量元素

`np.random.randn(row, column)`生成随机 data

```IPython
In [12]: import numpy as np  
# Generate some random data  
In [13]: data = np.random.randn(2, 3)  
In [14]: data  
Out[14]:  
array([[-0.2047, 0.4789, -0.5194],  
       [-0.5557, 1.9658, 1.3934]])
```

ndarray是一个通用的同构数据多维容器，也就是说，其中的所有元素必须是相同类型的。每个数组都有一个shape（一个表示各维度大小的元组）和一个dtype（一个用于说明数组数据类型的对象）：  
```IPython
In [17]: data.shape  
Out[17]: (2, 3)  
In [18]: data.dtype  
Out[18]: dtype('float64')
```

本章将会介绍NumPy数组的基本用法，这对于本书后面各章的理解基本够用。虽然大多数数据分  
析工作不需要深入理解NumPy，但是**精通面向数组的编程和思维方式是成为Python科学计算牛人的一大关键步骤**。  
> 笔记：当你在本书中看到“数组”、“NumPy数组”、"ndarray"时，基本上都指的是同一样东西，即ndarray对象。

我要成为 Python 科学计算牛人。

### 创建 ndarray

创建数组最简单的办法就是使用array函数。它接受一切序列型的对象（包括其他数组），然后产生一个新的含有传入数据的NumPy数组。

![[准备工作 - 利用python进行数据分析（第二版）.pdf#page=86&rect=69,229,325,337&color=yellow|准备工作 - 利用python进行数据分析（第二版）, p.86]]

> [!note]- 类型一致-连续内存的要求：为什么转化后的数字都加上了小数点？
> NumPy 数组的核心特性：所有元素必须是同一种数据类型（连续内存存储的基础）。
> 当输入列表元素类型不统一时，NumPy 会自动做向上类型转换（upcasting）：
> - 规则：int → float → complex，优先选择能容纳所有元素的最小类型
> - 这里列表里有 7.5（float），所以整个数组的 dtype 被推断为 float64
> - 所有整数（6,8,0,1）被自动转换成浮点数（6.0, 8.0, 0.0, 1.0），显示时就带了小数点

嵌套序列（比如由一组等长列表组成的列表）将会被转换为一个多维数组

```IPython
In [22]: data2 = [[1, 2, 3, 4], [5, 6, 7, 8]] 
In [23]: arr2 = np.array(data2) 

In [24]: arr2 
Out[24]: 
array([[1, 2, 3, 4],
       [5, 6, 7, 8]])
```

因为data2是列表的列表，NumPy数组arr2的两个维度的shape是从data2引入的。可以用属性ndim 和shape验证： 

```IPython
In [25]: arr2.ndim 
Out[25]: 2 
In [26]: arr2.shape 
Out[26]: (2, 4)
```
[[解惑：NumPy 中 ndarray.ndim 到底是什么？]]

除np.array之外，还有一些函数也可以新建数组。比如，zeros和ones分别可以创建指定长度或形状的全0或全1数组。empty可以创建一个没有任何具体值的数组。要用这些方法创建多维数组，只需传入一个表示形状的元组即可：
![[准备工作 - 利用python进行数据分析（第二版）.pdf#page=87&rect=72,139,523,392&color=yellow|准备工作 - 利用python进行数据分析（第二版）, p.87]]

> 注意：认为np.empty会返回全0数组的想法是不安全的。很多情况下（如前所示），它返回的都是一些未初始化的垃圾值

arange是Python内置函数range的数组版： 

```IPython
In [32]: np.arange(15) 
Out[32]: array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
```

![[准备工作 - 利用python进行数据分析（第二版）.pdf#page=88&rect=69,440,523,687&color=yellow|准备工作 - 利用python进行数据分析（第二版）, p.88]]

### ndarray 的数据类型

![[准备工作 - 利用python进行数据分析（第二版）.pdf#page=88&rect=62,192,523,390&color=yellow|准备工作 - 利用python进行数据分析（第二版）, p.88]]

dtype是NumPy灵活交互其它系统的源泉之一。多数情况下，它们直接映射到相应的机器表示，这使得“读写磁盘上的二进制数据流”以及“集成低级语言代码（如C、Fortran）”等工作变得更加简单。数值型dtype的命名方式相同：一个类型名（如float或int），后面跟一个用于表示各元素位长的数字。标准的双精度浮点值（即Python中的float对象）需要占用8字节（即64位）。

> 笔记：记不住这些NumPy的dtype也没关系，新手更是如此。通常只需要知道你所处理的数据的大致类型是浮点数、复数、整数、布尔值、字符串，还是普通的Python对象即可。当你需要控制数据在内存和磁盘中的存储方式时（尤其是对大数据集），那就得了解如何控制存储类型。

![[准备工作 - 利用python进行数据分析（第二版）.pdf#page=89&rect=66,254,524,698&color=yellow|准备工作 - 利用python进行数据分析（第二版）, p.89]]

你可以通过ndarray的astype方法明确地将一个数组从一个dtype转换成另一个dtype： 

```IPython
In [37]: arr = np.array([1, 2, 3, 4, 5]) 
In [38]: arr.dtype 
Out[38]: dtype('int64') 
In [39]: float_arr = arr.astype(np.float64) 
In [40]: float_arr.dtype 
Out[40]: dtype('float64')
```

> 注意：使用numpy.string_类型时，一定要小心，因为NumPy的字符串数据是大小固定的，发生截取时，不会发出警告。pandas提供了更多非数值数据的便利的处理方法。

> 笔记：调用astype总会创建一个新的数组（一个数据的备份），即使新的dtype与旧的dtype 相同。
[[不仅仅是强制转换：掌握 NumPy 中 astype() 的数据处理技巧]]

### NumPy 数组的运算

