---
tags:
  - python
---
## 认识 JSON

如果希望把一个列表或者一个字典中的数据保存到文件中又该怎么做呢？

JSON 是“JavaScript Object Notation”的缩写，它本来是 JavaScript 语言中创建对象的一种字面量语法，现在已经被广泛的应用于跨语言跨平台的数据交换。使用 JSON 的原因非常简单，因为它结构紧凑而且是纯文本，任何操作系统和编程语言都能处理纯文本，这就是**实现跨语言跨平台数据交换**的前提条件。

[JSON 的官方网站](https://www.json.org/json-zh.html)

```json
{
    name: "骆昊",
    age: 40,
    friends: ["王大锤", "白元芳"],
    cars: [
        {"brand": "BMW", "max_speed": 240},
        {"brand": "Benz", "max_speed": 280},
        {"brand": "Audi", "max_speed": 280}
    ]
}
```

跟 Python 中的字典非常类似而且支持嵌套结构

表1：JavaScript 数据类型（值）对应的 Python 数据类型（值）

|JSON|Python|
|---|---|
|`object`|`dict`|
|`array`|`list`|
|`string`|`str`|
|`number`|`int` / `float`|
|`number` (real)|`float`|
|`boolean` (`true` / `false`)|`bool` (`True` / `False`)|
|`null`|`None`|

表2：Python 数据类型（值）对应的JavaScript数据类型（值）

| Python                    | JSON                         |
| ------------------------- | ---------------------------- |
| `dict`                    | `object`                     |
| `list` / `tuple`          | `array`                      |
| `str`                     | `string`                     |
| `int` / `float`           | `number`                     |
| `bool` （`True` / `False`） | `boolean` (`true` / `false`) |
| `None`                    | `null`                       |

## 对JSON文件格式的数据进行读取

**将字典处理成 JSON 格式（以字符串形式存在）**

```python
import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(json.dumps(my_dict))
```

**将字典处理成 JSON 格式并写入文本文件，只需要将`dumps`函数换成`dump`函数并传入文件对象即可**

```python
import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
with open('data.json', 'w') as file:
    json.dump(my_dict, file)
```

### json模块的重要函数

- `dump` - 将 Python 对象按照 JSON 格式序列化到文件中
- `dumps` - 将 Python 对象处理成 JSON 格式的字符串
- `load` - 将文件中的 JSON 数据反序列化成对象
- `loads` - 将字符串的内容反序列化成 Python 对象

“序列化（serialization）在计算机科学的数据处理中，是指将数据结构或对象状态转换为可以存储或传输的形式，这样在需要的时候能够恢复到原先的状态，而且通过序列化的数据重新获取字节时，可以利用这些字节来产生原始对象的副本（拷贝）。与这个过程相反的动作，即从一系列字节中提取数据结构的操作，就是反序列化（deserialization）”。

### 反序列化操作（连续）

我们可以通过下面的代码，读取上面创建的`data.json`文件，将 JSON 格式的数据还原成 Python 中的字典。

```python
import json

with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)
```

## 包管理 pip

Python 标准库中的`json`模块在数据序列化和反序列化时性能并不是非常理想

<u>可以使用三方库`ujson`来替换`json`。</u>

`pip --version`

`pip list`

`pip install ujson`

更新`ujson`三方库。

```shell
pip install -U ujson
```

删除`ujson`三方库。

```shell
pip uninstall -y ujson
```

> **提示**：如果要更新`pip`自身，对于 macOS 系统来说，可以使用命令`pip install -U pip`。在 Windows 系统上，可以将命令替换为`python -m pip install -U --user pip`。

## 使用网络API获取数据

Python 通过 URL 接入网络，我们推荐大家使用`requests`三方库，它简单且强大，但需要自行安装。

```shell
pip install requests
```

获取国内新闻并显示新闻标题和链接。（举例）

```python
import requests

resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
if resp.status_code == 200:
    data_model = resp.json()
    for news in data_model['newslist']:
        print(news['title'])
        print(news['url'])
        print('-' * 60)
```

## 晚话

Python 中实现序列化和反序列化除了使用`json`模块之外，还可以使用`pickle`和`shelve`模块，但是这两个模块是使用特有的序列化协议来序列化数据，因此序列化后的数据只能被 Python 识别，关于这两个模块的相关知识，有兴趣的读者可以自己查找网络上的资料。处理 JSON 格式的数据很显然是程序员必须掌握的一项技能，因为不管是访问网络 API 接口还是提供网络 API 接口给他人使用，都需要具备处理 JSON 格式数据的相关知识。