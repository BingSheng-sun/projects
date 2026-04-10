---

---

# 0x 查询三日内创建的文档
````
```dataview
Table file.ctime as "创建日期"
Where date(today) - file.ctime <= dur(3 day)
Sort file.ctime desc
```
````

````
```dataview
Table file.ctime as "创建日期"
Where date(today) - file.ctime <= dur(3 day)
Sort file.ctime desc
```
````


# 1x
## 10 Metadata元数据

### 查询文档的元数据
```
	```dataview
	TABLE this
	WHERE file = this.file
	LIMIT 1
	```
```

### Dataview 只能查询有索引的内容

- 文件中的元数据
	- 文件本身
	- 文件中的列表
- 文件的隐式字段

## 11 如何向文档中添加元数据

### Properties

快捷键法：ctrl + ;
命令面板法：ctrl + p，搜索添加文档属性 (英文为 add file property)；
鼠标右键文件标题：选择增加文档属性 (英文为 add file property)；
标签页标题栏的竖着的三个点：选择增加文档属性 (英文为 add file property)；
原来的手动输入 --- 依旧可行；

>[!tip] 注意 Yaml规则
>>- 大小写敏感，可以使用中文；
>>- 冒号后要跟一个空格；
>>- 使用缩进来代表层级关系；
>>- 缩进时只能用空格，不能用 Tab；
>>- 缩进的空格数不重要，但是同一级元素必须左对齐；
>>- 用井号标识注释，从 `#` 到当前行的末尾是注释；
>

>[!danger] 注意
>>如果你的 YAML 格式正确，则阅读模式下会自动隐藏，否则会标红报错；
占位符里的冒号后有空格，如{{time: HH:mm}}，留意占位符里的 time,或者 date 冒号后面也是要添加一个空格的；
可以使用所有字符作为键 or 值（包括 emoji 在内），但若放在键的位置，则仍需要放入中括号中，除了 task 的情况；
dv 检索时，原关键字的值的格式必须正确，否则 dv 会报错，但这种情况下不是代码写错了，而是代码检索的对象有问题；

[更详细的YAML语法](https://pkmer.cn/Pkmer-Docs/10-obsidian/obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/dataview/dataview%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95/43---yaml-%E5%9F%BA%E7%A1%80)

### Inline Fields

今天[天气::晴天]
今天(天气::晴天)

局部字段


## 12 添加元数据到列表和任务

因为时间与任务或者列表总捆绑在一块，比如一个任务的 ddl，或者是完成时间，且 Dataview 为这类转换提供了简化语法，因此把这一节单独拿出来。

![[Pasted image 20251119125037.png]]

两种方法记录的实际上是同一个元数据。也就是说，表情 🗓️ 对应的属性就是 due，即截止日期。用图像代表截止日期更直观。

提示

对于 obsidian 来说，任务和列表（有序列表和无序列表）实际上是同一类数据的不同形式，都可以用这种方法为他们加上元数据来方便后续的查询；

除此之外，还有其他的 Emoji 表情代表不同的含义：

Emoji 表情	属性 Field Name	含义
🗓️	due	截止日期
✅	completion	完成日期
➕	created	创建日期
🛫	start	开始日期
⏳	scheduled	预期完成日期
这时候你或许会说，这些表情我平常都不用，难不成每次还来要这篇文章里面复制粘贴吗？

obsidian 最新版本已经不支持 win7 了，而 win10 及以上版本的电脑，可以只通过一个快捷键加一次鼠标点击，就能输入这些表情；

在任意界面，用快捷键 win + . 或 win + ; 打开 Emoji 表情窗口，上面五个 Emoji 标签均能在里面找到，分别为：

🗓：线圈日历，在 “庆祝和物品” 中；
🛫：航班起飞：在 “交通和地点” 栏中第六行，直接打字 “飞机” 也会出现；
✅：空心对勾，在最后一栏 “符号” 中；
➕：加号：在最后一栏 “符号” 中，直接打字 “加号” 也会出现；
⏳：沙正往下流的沙漏，在 “庆祝和物品” 的最后一行，直接打字 “沙漏” 也会出现；


其中部分可以直接打字显示（默认输入法），使用过的表情也会出现在 Emoji 表情窗口的 “最近使用” 栏中，视觉上比打两个冒号好了很多，输入也不会很麻烦；



还有其他几种可能更适合你的添加图标的方式

Obsidian 插件：Icon Shortcodes 通过短代码方式，快速筛选和输入
Obsidian 插件：Emoji Toolbar 快速插入 Emoji 符号
Obsidian 插件：Obsidian Icons 提供插入图标符号的功能


## 13 Metadate的数据类型

Metadata是一个键值对(Key - Value)即(Field Name - Field)

### Field Name

>[!tip] Field Name 值自动修改规则
>>- 如果有粗体、斜体等格式，格式会被擦除，变成普通文本；
>>- 如果中间无空格，原本有大写的 Key 值和全部字母小写后的值都可以当作其 Key 值；
>>- 如果中间有空格，会被替换成 `-`，并且所有大写字母会被换成小写字母；

| 原 Field Name 的写法 |                修改后                 |       改动内容        |
| :--------------: | :--------------------------------: | :---------------: |
|   `**basic**`    |              `basic`               |       去掉粗体        |
|     `Basic`      | `Basic` 或 `basic` （不能是 `BaSic` 之类） |       增加了小写       |
|  `basic field`   |           `basic-field`            |    用 `-` 替换空格     |
| `**Bold Field**` |             `bold-key`             | 去掉粗体，并替换空格，同时全部小写 |

### Field 属性域

属性域具有数据类型，也就是说，它能够区分数字、文字、时间类型等。不同的数据类型具有不同的信息，比如数字有可以量化的信息，文字有内容信息，时间有年月日信息，布尔类型有真假信息。有了不同的数据类型，我们才可以更高效且准确的进行查询，因此数据类型非常有必要存在。

#### string 字符串

默认的数据类型，也是最常用的数据类型。当一个 Feild 没有对应的类型时，就为 string 类型(可以使用双引号包含，也可以不用)。

直接输入中文一般都是字符串。

#### number 数字类型

不区分整数还是小数，全部都为数字类型。

#### boolean 布尔类型

`true` and `false`

用于读书笔记的元数据时，可以与是否读完/总结/做好读书笔记等 Field Nmae 关联使用

#### date 时间类型

匹配 [ISO8601表示法](https://pkmer.cn/Pkmer-Docs/10-obsidian/obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/dataview/dataview%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95/42---iso-8601) 的文本将自动转换为日期对象；

[[Dataview 支持的时间格式 ISO 8601 的含义-Pkmer]]

例如：`2023-07-17`，`2023-07-17T16:34:000`，`2021-08-13T14:20:18.992847200-04:00`，能够包含年月日、时分秒、纳秒甚至时区的信息；

- 从时间域 field 中提取信息

|        语法         |            解释             |
| :---------------: | :-----------------------: |
|    field.year     |           获取年份            |
|    field.month    |           获取月份            |
|  field.weekyear   | 获取周数（从每年的第一天开始算，一年约 52 周） |
|    field.week     |   获取周数（从每个月第一天，一月约 4 周）   |
|   field.weekday   | 获取星期数（星期 1 为 1、星期 2 为 2）  |
|     field.day     |           获取天数            |
|    field.hour     |           获取小时数           |
|   field.minute    |           获取分钟数           |
|   field.second    |           获取秒数            |
| field.millisecond |           获取纳秒数           |

#### duration 定长时间

Date 时间是指一个时间点，而 Duration 是指一段时间。比如 1 分钟、1 天、1 年等；

语法：

- 时间长度 + 单位
- 中间可以紧挨着，也可以空格分割，也可以逗号分割，还可以组合；
- 时间长度是数字，单位单复数都行，有：
    - 秒：s、sec、secs、second、seconds；
    - 分钟：m、min、mins、minnute、minutes；
    - 小时：h、hr、hrs、hour、hours；
    - 天：d、day、days；
    - 周：w、wk、wks、week、weeks；
    - 月：mo、month、months；（注意和分钟区分）
    - 年：yr、yrs、year、years；（注意没有 y）


> [!example] 例子
> 
> - 紧挨着：1min
> - 空格分割：3 day
> - 逗号分隔：2 min, 3 hours
> - 组合：1 second 2 min 3 h
> - 顺序无关紧要：2m1s3h 和上一个的结果一致

#### link 链接

链接也是其中的一种数据结构，语法和在正文中的一致： `[[链接]]` 或 `[[链接|显示的名字]]` ；

示例：

- 在文档属性：`Linkto: [[...]]`
- 在行内字段中：`Linkto:: ...` ；

#### array 数组（List 列表）

多值属性的值域

添加在文档属性中有两种写法：

- 如果是源码模式，有两种写法：
    - 第一种是以逗号分割，用方括号 `[ ]` 括起来；
    - 第二种是用无序列表；

```
---
tags: [obsidian, 插件, Dataview]
---
```

也可以写成

```
---
tags: 
  - obsidian
  - 插件
  - Dataview
---
```

- 如果你是实时预览模式，你只需要在选择该属性为列表 List，每输入一个值点击回车确认即可

![Dataview 中的 Metadata 的数据类型--array 数组（List 列表）](https://cdn.pkmer.cn/images/PixPin_2023-12-17_14-28-03.gif!pkmer)

添加在行内字段中就直接用逗号分割，如 tags:: obsidian, 插件, Dataview

>[!attention] 注意
>一个列表中的所有属性的属性值都要相同，因此例如 `example:: 值1, 值2, 3`。这三个属性值的数据类型都是字符串，包括第三个属性值 “3”。如果所有属性值都是数字，或者都是布尔值的时候，他们的数据类型才会是数字或者字符串。但凡有一个不是，dataview 会把他们都以字符串的格式识别。因此如果遇到你用列表中的数字加减发现报错，不妨用 `typeof()` 函数检查一下这个 ” 数字 ” 会不会其实是字符串。

#### object 对象

有的属性，没法用一个值来概括，而需要多个值来概括时，这个属性就是一个对象，我们把对象的一个个属性都作为属性域。（列表的多值属性是同一种含义，共享一个属性，对象的多个属性域有不同的含义，是属性的属性，如果有学过面向对象编程应该很熟悉）

语法：

```
--- 
obj: 
  key1: "Value" 
  key2: 3 
  key3: 
   - "List1" 
   - "List2" 
   - "List3" 
---
```

举个例子，比如文件为记录一部电影，属性可以有前奏和片尾曲这两个对象，他们可以有歌名和歌手的属性：

复制

```
Prelude: 
  - name: ...
  - singer: ...
EndSong:
  - name: ...
  - singer: ...
```

>[!caution] 注意
>从这里也能看出元数据对于查询有很大帮助。我们可以利用不同数据类型的元数据提供的信息，对文件进行检索，最终查询出符合我们给定的条件（比如作者来自中国需要用 `from = 中国` 来筛选）的所有结果；

## 14 隐式字段
1. 如何查看一个文件里面所有的隐式字段；
2. 每一个字段的含义；
3. 具体的查看某一个特定的隐式字段的方法；

文件中的一些已经自动有索引的内容，比如文件的名字，文件的创建时间、修改时间等，我们称之为文件的隐式字段。他们也是能够被 Dataview 检索到的。

>[!abstract] 文件的隐式字段有两种
>- 文件自动索引的字段：file；
>- 列表和任务的隐式字段：file.lists, file.tasks；

### 查看文件的隐式字段

输入下面的代码可以显示当前文件的所有元数据。

复制

````
```dataview
TABLE this
WHERE file = this.file
limit 1
```
````

其中，file 就是该文件的隐式字段，它的数据类型是 [object 对象](https://pkmer.cn/Pkmer-Docsdata%E7%9A%84%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)。[向文件添加了其他元数据](https://pkmer.cn/Pkmer-Docs/10-obsidian/obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/dataview/dataview%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95/11---%E6%B7%BB%E5%8A%A0%E5%85%83%E6%95%B0%E6%8D%AE%E8%87%B3%E6%96%87%E4%BB%B6)（添加到前言或者用行内字段添加至正文），他们将与 file 属性处于同一级或覆盖 file 属性中的子属性（添加元数据时使用已有的属性名就能替换）。

>[!tip] 
>- 无该属性值时会空着；
>- 查询结果中会有一些属性值为 `...`，这是因为 Dataview 的查询结果只会显示两级属性值；

可以用 `this` 指代本文件，用 `this.file` 特指是本文件的属性。不用 `this` 的时候泛指所有选中的文件。我们用点运算符 `.` 来调用更下一级的属性，如 `file.path` 是指文件的路径；

### 隐式字段的含义

>[!attention] 大多数的属性的直接数据类型是 array 数组，下面的数据类型指代的是数组里面元素的类型;

#### file 隐式字段

|      属性名 (17)      |     数据类型     |                                 解释                                  |
| :----------------: | :----------: | :-----------------------------------------------------------------: |
|    `file.path`     |  string 字符串  |                         文件的路径（相对于整个 Vault）                          |
|   `file.folder`    |  string 字符串  |                      文件所属的文件夹的路径（相对于整个 Vault）                       |
|    `file.name`     |  string 字符串  |                                 文件名                                 |
|    `file.link`     |   link 链接    |                             引用这篇文件时的链接                              |
|  `file.outlinks`   |   link 链接    |                                该文件外链                                |
|   `file.inlinks`   |   link 链接    |                             指向本文的文件的链接                              |
|    `file.etags`    |  string 字符串  |             该文件的所有标签  <br>例如文件中有标签 `#A/B` ，只会有 `#A/B`；              |
|    `file.tags`     |  string 字符串  |     该文件的所有标签，以及他们的各级标签  <br>例如文件中有标签 `#A/B` ，就会有 `#A/B` 和 `#A`；     |
|   `file.aliases`   |  string 字符串  | 别名，添加元数据直接覆盖即可，可以取多个；  <br>例如在 frontmatter 中写 `aliases: [别名1, 别名2]` |
|    `file.lists`    |  object 对象   |                       文件中出现的所有列表的信息（任务是特殊的列表）                       |
|    `file.tasks`    |  object 对象   |                            文件中出现的所有任务的信息                            |
|    `file.ctime`    |  date 时间类型   |                       文件的创建时间（c 代表 create 创建）                       |
|    `file.mtime`    |  date 时间类型   |                      文件最后修改时间（m 代表 modify 修改）                       |
|    `file.size`     |  number 数字   |                           文件的大小（单位为 byte）                           |
|   `file.starred`   | boolean 布尔类型 |        文件是否被星标（核心插件星标已经被书签替代）  <br>该属性无法被覆盖，书签标记也无法令其为 true         |
| `file.frontmatter` |  object 对象   |                               前言中的元数据                               |
|     `file.ext`     |  string 字符串  |                     文件的拓展名（ext 是 extension 的缩写）                     |

#### 列表和任务的隐式字段

他们的能用 `file.lists` 和 `file.tasks` 调用

试下将上面的 Dataview 代码中第一行的 this 改成 `file.lists` 和 `file.tasks` ；

（最后的 `limit 1` 是限制 dataview 只输出一个查询结果，防止查询结果过长导致的卡顿。）

````
```Dataview
table file.lists, file.tasks
where file = this.file
limit 1
```
````

在 `file.lists` 中我们提到过，任务是一种特殊的列表（从他们的语法也能看出来），因此任务有所有列表有的属性，还有列表没有的属性（status, checked, completed, fullyCompeleted），后面只用列表统称两者；

##### 任务和列表都有的属性

|属性名|数据类型|解释|
|:-:|:-:|:-:|
|`symbol`|array 数组|符号|
|`link`|link 链接|该列表上方最近的可链接的标题|
|`section`|link 链接|该列表上方最近的可链接的标题（与 link 一致）|
|`text`|string 字符串|列表的正文|
|`tags`|array 数组|该列表中所有的标签|
|`line`|number 数字|该列表所在行|
|`lineCount`|number 数字|次列表占用的行数|
|`list`|number 数字|该组列表的起始行|
|`outlinks`|link 链接|该列表的外链|
|`path`|string 字符串|列表所处的文件的路径|
|`children`|array 数组|列表的子列表和子列表的子列表|
|`task`|boolean 布尔类型|判断该列表是不是一个任务，值为 true 时是任务|
|`annotated`|boolean 布尔类型|判断该列表是否包含元数据|
|`position`|object 对象|包含了这组列表的位置的起始信息|
|`subtasks`|object 对象|列表的子列表和子列表的子列表（与 children 一致）|
|`real`|boolean 布尔类型|判断该列表是不是一个任务，值为 true 时是任务（与 task 一致）|
|`header`|link 链接|该列表上方最近的可链接的标题（与 link 和 section 一致）|

###### 位置 `position`

位置属性的数据类型是对象，它的子属性有 `start` 和 `end`，他们的数据类型都是 object 对象，分别代表记录了这个列表的起始位置。它们的子属性有 `line` 、`col` 和 `offset`。

- `position.start.line` 和 `position.end.line` 都代表该列表所在行（不是列表组）；
- `position.start.col` 代表第一个字符所在列，`position.end.col` 代表最后一个字符所在列；
- `position.start.offset` 代表文件开头到列表第一个字符所含的字符数，`position.end.offset` 代表文件开头到列表最后一个字符所含的字符数；

###### 子列表 subtasks 和 children

这两个属性结果一致，数据类型是 object 对象。他们的其他属性前面都出现过，只有一个新的属性 `parent` 还没出现过。`parent` 的数据类型是 number 数字，代表他们的上级所在行。

###### 用简写语法 (Shorthand Syntax) 定义的五个属性

在 [12 - 添加元数据至列表和任务](https://pkmer.cn/Pkmer-Docs/10-obsidian/obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/dataview/dataview%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95/12---%E6%B7%BB%E5%8A%A0%E5%85%83%E6%95%B0%E6%8D%AE%E8%87%B3%E5%88%97%E8%A1%A8%E5%92%8C%E4%BB%BB%E5%8A%A1) 中我们提到，使用图标简写语法可以为列表或任务添加五个属性

|     属性名      |  数据类型   |   解释   |
| :----------: | :-----: | :----: |
|    `due`     | date 时间 |  截止日期  |
| `completion` | date 时间 |  完成日期  |
|  `created`   | date 时间 |  创建日期  |
|   `start`    | date 时间 |  开始日期  |
| `scheduled`  | date 时间 | 预期完成日期 |

##### 任务特有的属性

|属性名|数据类型|解释|
|:-:|:-:|:-:|
|`status`|string 字符串|任务的语法中，方括号内的字符（一般完成为 x）|
|`checked`|boolean 布尔类型|方括号内是否有非空格字符（不一定是 x）|
|`completed`|boolean 布尔类型|只有方括号内为 x 才为 true|
|`fullyCompleted`|boolean 布尔类型|任务及其所有子任务是否完成|
>[!summary] 上面的属性中，有不少属性之间的含义是完全一样的，有的属性之间只有细微差别
>由于 `file.tasks` 只比 `file.lists` 多了一些属性，下面只列举了 `file.lists` 的部分，可以把 lists 改为 tasks 即可得到 `file.tasks` 的对应属性。
>>[!example] 完全相同的属性
>>file.path 和 file.lists.path；
>>link、section 和 header；
>>position.start.line 和 position.end.line；
>>file.lists.children 和 file.lists.subtasks；
>>file.lists.task 和 file.lists.real；
>>
>>>[!example] 相近但不相等的属性
>>> - `file.etags` 和 `file.tags` ；
>> >- `file.lists` 和 `file.tasks` ；
>> >- `file.lists.check` 、`file.lists.completed` 和 `file.lists.fullyCompleted` ；


### 具体查看隐式字段

这里只给出简单的 Dataview 代码，现在还不理解没关系，对应上面看懂属性的含义，知道在做什么即可

#### 查询文件自带的元数据的属性

用查询文件的创建时间和最后一次修改时间举例，上文我们已经说过他们对应的属性名是 `file.ctime` 和 `file.mtime`，中间用逗号分割。将下面的代码直接放在正文中即可。（你也可以自己试试查询别的属性）

````
```dataview
table file.ctime, file.mtime
where file = this.file
```
````

简单解释一下这两行代码在做什么，更具体的请看 [21 - 查询类型](https://pkmer.cn/Pkmer-Docs/10-obsidian/obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/dataview/dataview%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95/21---%E6%9F%A5%E8%AF%A2%E7%B1%BB%E5%9E%8B) 和 [23 - 操作符](https://pkmer.cn/Pkmer-Docs/10-obsidian/obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/dataview/dataview%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95/23---%E6%93%8D%E4%BD%9C%E7%AC%A6)

- 第一行是确定以表 table 的形式显示查询结果，以及查询文件的创建日期和最后一次修改时间；
- 第二行是将搜索范围缩小到 this file，也就是这段代码所在的文件；

#### 查询列表和任务的元数据

列表和任务是在 file 属性下的子属性 `file.lists` 和 `file.tasks`，我们这里查询列表的正文 `text`

````
```dataview
table file.lists.text, file.tasks.text
where file = this.file
```
````

这段代码能查询到你当前文件的列表和任务的正文

#### 查询属性的数据类型

上面我们给出了所有隐式字段的数据类型，其实可以用 [函数 typeof()](https://pkmer.cn/Pkmer-Docs/10-obsidian/obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/dataview/dataview%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95/30---dataview-%E6%8F%90%E4%BE%9B%E7%9A%84%E5%87%BD%E6%95%B0-function#^528a53) 手动查询，括号内填想要查询的属性值，函数就会返回数据类型。

- 当输入值为属性值时

````
```dataview
table typeof(file), typeof(file.lists.link)
where file = this.file
```
````

可以看到我们这里一共查询了三个属性，`file`, `file.lists.link`, 。这时候你可能想问，明明上文说了 `file.lists.link` 的数据类型是 link 链接，为什么查询出来的结果是 array 数组。这是因为上文给出的数据类型都是最终的数据类型，也就是数组内的元素的数据类型，可以试试查下 `file.lists.link[0]` 的数据类型，也就是 `file.lists.link` 这个数组中的第一个元素的数据类型。（用方括号取数组中的元素，下标从 0 开始）

- 当输入值为普通值时

````
```dataview
table without id typeof("这里的值可以换成下面的")
limit 1
```
````

|输入|输出|
|:-:|:-:|
|`typeof(8)`|”number”|
|`typeof("text")`|”string”|
|`typeof([1, 2, 3])`|”array”|
|`typeof({ a: 1, b: 2 })`|”object”|
|`typeof(date(2023-07-19))`|”date”|
|`typeof(dur(8 minutes))`|”duration”|

## 15 Literals 字面常量

Dataview 中可以使用的字面常量有三种

- 一般字面常量 (General)：数字、字符串等；
- 时间字面常量 (Date)：某个时间点；
- 定长时间字面常量 (Duration)：一段时间；

### 一般字面常量 General

|字面常量 Literal|解释 Description|
|:-:|:-:|
|`0`|数字 0|
|`1337`|正数 1337|
|`-200`|负数 -200|
|`"The quick brown fox jumps over the lazy dog."`|用了 26 个字母的字符串|
|`[[链接]]`|链接|
|`[[]]`|指向本文的链接|
|`[1, 2, 3]`|1, 2, 3 组成的列表|
|`[[1, 2], [3, 4]]`|[1, 2] 和 [3, 4] 组成的列表|
|`{ a: 1. b: 2 }`|含有属性 a=1 和 b=2 的一个对象|
|`date(2023-07-21)`|日期|
|`dur(2 days 4 hours)`|一段定长时间|

### 日期的字面常量

如果你尝试用 `typeof()` 函数获取类似 `2023-07-21` 或者 `"2023-07-21"` 的数据类型，他会告诉你是 number 类型和 string 类型。我们需要用 `date()` 函数把这些类型转换成日期；

````
```dataview
table without id
typeof(2023-07-21), typeof("2023-07-21")
limit 1
```
````

|       字面常量 Literal       |      描述 Description      |
| :----------------------: | :----------------------: |
|    `date(2023-07-21)`    |      日期：2023-07-21       |
| `date(2023-07-21T14:55)` |  具体到分钟的日期（T 分开天数和具体时间）   |
|      `date(today)`       |       今天的日期（具体到天数）       |
|       `date(now)`        |     现在的日期和时间（具体到纳秒）      |
|     `date(tomorrow)`     |       明天的日期（具体到天数）       |
|       `date(sow)`        |  start of week——这周的开始日期  |
|       `date(eow)`        |   end of week——这周的结束日期   |
|       `date(som)`        | start of month——这个月的开始日期 |
|       `date(eom)`        |  end of month——这个月的结束日期  |
|       `date(soy)`        |  start of year——今年的开始日期  |
|       `date(eoy)`        |   end of year——今年的结束日期   |

比如你想记录这周创建的所有文件，你可以这样写

````
```dataview
table file.cday
where file.cday >= date(sow)
```
````

这周创建不一定是七天内，不能写成 `where file.cday >= date(now) - dur(7 day)`；


### 定长日期

用函数 `dur()` 即可，括号内可以填符合格式的时间，通过这个函数就能映射成一个 dateview 能够识别的时间。我们还可以对这个时间做运算。符合的格式可以看 Metadata 数据类型中的 [Duration部分](https://pkmer.cn/Pkmer-Docs/10-obsidian/obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/dataview/dataview%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95/13---metadata%E7%9A%84%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B#^df2612).

举几个只用了最简写的例子（其他的写法上面的链接处都有）

- 大多数为英文首字母，有重复的（比如分钟 minute 和月 month）才有所区分，年比较特殊得用 `yr` 而不是 `y`；
- 中间可以挨着也可以有空格；
- 复合时间用逗号分割，dataview 会自动对他们求和。因此复合时间没有顺序要求，比如可以时分秒，也可以秒分时，也可以秒时分；
- 没有规定秒一定要小于 60，`dur(61s)` 会解释成 1 分 1 秒；

|字面常量 Literal|描述 Description|
|:-:|:-:|
|`dur(1s)`|一秒|
|`dur(3m)`|三分钟|
|`dur(5h)`|五小时|
|`dur(2d)`|两天|
|`dur(4w)`|四周|
|`dur(6mo)`|六个月|
|`dur(7 yr)`|七年|
|`dur(1s, 2m, 3h)`|3 小时、2 分钟和 1 秒钟|

接下来，我们开始真正开始进入到代码的世界，[20 - 四种查询方式](https://pkmer.cn/Pkmer-Docs/10-obsidian/obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/dataview/dataview%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95/20---%E5%9B%9B%E7%A7%8D%E6%9F%A5%E8%AF%A2%E6%96%B9%E5%BC%8F)，或是返回 [Dataview基本语法](https://pkmer.cn/Pkmer-Docs/10-obsidian/obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/dataview/dataview%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95/dataview%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95)。

# 2x
## 20 Dataview 支持的四种查询方式

Dataview 一共提供了四种查询的方式，后两者涉及到 JavaScript ，不在 Dataview 基础语法中介绍

查询方式	介绍
DQL 行内查询	可以直接插入文章中，像 excel 中使用函数那样，可以实现级联，缺点是功能不完整
DQL 代码块查询	Dataview 用的最多的查询方式
DVJS 行内查询	和 DQL 行内查询类似，但是功能更多，但是需要用 javascript
DVJS 代码块查询	可以满足大部分要求
DQL 行内查询：无痕插入文中
注意

使用这种查询时，需要在 Dataview 设置中打开 Enable Inline Queries 设置。

行内 DQL 需要写在行内代码中，适合小范围嵌入元数据使用；

以一个等号开头，后面跟需要显示的元数据；
如果是当前文件的元数据，用 this 指代。如果是别的文件的元数据，用那个文件的链接指代；
查询本文件的名字：

`= this.file.name`
你会发现，在你光标移动到别处后，他就会变成文件的名字。

查询别的文件的元数据：用链接代表那个文件（方括号内的 file 替换成目标文件的文件名）

`= [[file]].file.name`
小技巧：修改行内查询的前缀

你可以在 Dataview 设置中的“代码块设置”>“内联查询前缀”中将 = 更改为另一个前缀 (如 dv: 或~)

DQL 代码块查询
从 01 - 简单示例 可以观察到，dataview 的代码主要分为四个部分：

确定结果展示的方式以及展示的内容；
确定搜索的范围；
确定搜索的条件；
对搜索结果进行调整；
他们一般会以下图方式排列，翻译成文字就是：按照什么查询类型从某个文件夹或者按照某个标签查询，通过操作符对查询结果做了一些操作后，展示查询字段



写成代码代码就是：
````
```dataview
<Query-Type> <Fields> 
From <Source> 
<Data-Command> <Expression> 
<Data-Command> <Expression> 

%% 注释：可以有很多个 <Data-Command> %%
```
````
比如举个例子：

按照表格的显示
检索文件夹 ” 日记/2023” 中的所有文件
满足创建日期距离今天不超过 30 天的文件
展示这些文件中的 ” 心情 ” 和 ” 天气 ” 元数据
````
```dataview
Table 心情, 天气
From "日记/2023"
Where date(today) - file.cday < 30 
```
````
接下来具体讲讲这四个部分

Query-Type 查询类型
Dataview 一共提供了四种查询类型：LIST, TABLE, TASK, CALENDAR，选择不同的类型会获得不同的展示效果。查询类型也是一个完整的 DQL 查询所唯一需要的。

详细解释

Fields 字段
我们想要展现的内容，内容为 表达式，不妨配合 字面常量 使用；

例如：如果想展示搜索到的文件的名字，可以写 table file.name；

可以在 14 - 隐式字段 中查看文件自带的所有 Metadata 和他们的含义；

Source 查询域
即查询的范围，查询的内容来自于哪里。可以是标签（Tags）、文件夹（Folders）、某个特定的文件（Specific Files），又或是一个链接（Links）；

例如：如果范围是含有某标签，可以写 from ·#标签，可以在 33 - 操作符 中查看更具体的解释；

Data-Command 操作符
我们对查找到的内容做的操作（筛选，排序，成组，拆分，限制数量等），具体见 23 - 操作符。还可以配合 Dataview 提供的一些 函数 更好的进行查询。

提示

Query Type 决定查询的输出格式，这是我们查询唯一的必需信息（甚至只有这个内容都可以）；
Dataview 对大小写不敏感，TABLE、table 和 Table 是一样的效果，看个人习惯选择即可。但引号内的内容区分大小写；
支持中文；
代码的结构并不是必须按照上面给的格式，你可以自行换行，比如把搜索的 Field 写在第二行，又或者当语句不长的时候全部写在一行都是可以的；
DQL 查询从上到下逐行执行，你可以写很多个 Data-Command；
利用 JavaScript 进行行内查询
注意

使用这种查询时，需要在 Dataview 设置中打开 Enable Inline JavaScript Queries 设置。

此处仅给一个示例，具体请看其他相关文章

This page was last modified at `$= dv.current().file.mtime`.
这段代码使用了 JS 进行了行内查询，获取最后一次修改当前文件的时间。

DataviewJS
注意

使用这种查询时，需要在 Dataview 设置中打开 Enable JavaScript Queries 设置。

这里给出一段 [Blue-Topaz 示例库](PKM-er/Blue-topaz-example: Blue topaz themes example vault for Obsidian (github.com)) 主页中的一段代码，他会告诉你你使用 Obsidian 的天数，以及创建了笔记、标签和代办的个数

````
```dataviewjs
let ftMd = dv.pages("").file.sort(t => t.cday)[0]
let total = parseInt([new Date() - ftMd.ctime] / (60*60*24*1000))
let totalDays = "您已使用 ***Obsidian*** "+total+" 天，"
let nofold = '!"misc/templates"'
let allFile = dv.pages(nofold).file
let totalMd = "共创建 "+ allFile.length+" 篇笔记"
let totalTag = allFile.etags.distinct().length+" 个标签"
let totalTask = allFile.tasks.length+"个待办。 "
dv.paragraph(
	totalDays + totalMd + "、" + totalTag + "、" + totalTask
)
```
````
接下来，我们开始学习 dataview 语法的 21 - 查询类型，或是返回 Dataview基本语法。


## 21 查询类型

[[Dataview 提供的四种查询类型-Pkmer]]


## 22 查询字段

[[Dataview 中的查询字段可以是什么-Pkmer]]

## 23 操作符

[[Dataview 支持的Data Commands 操作符-Pkmer]]

## 24 表达式

[[Dataview 支持的表达式 Expression-Pkmer]]

# 3x

## 30 函数

[[Dataview 提供的函数 Function-Pkmer]]

## 31 构造函数

[[Dataview 中的构造函数-Pkmer]]

## 32 数值运算函数

[[Dataview 中的数值运算函数-Pkmer]]

## 33 对象操纵函数

[[Dataview 中的对象操纵函数-Pkmer]]

## 34 字符串操纵函数

[[Dataview 中的字符串操纵函数-Pkmer]]

## 35 常用函数

[[Dataview 中的实用函数-Pkmer]]

# 4x

## 40 常见问题faq

[[Dataview 相关的 FAQ - 常见问题-Pkmer]]

## 41 DQL和SQL的区别

[[Dataview 中的 DQL 与 SQL 的区别-Pkmer]]

## 42 ISO 8601

[[Dataview 支持的时间格式 ISO 8601 的含义-Pkmer]]

## 43 yaml基础

[[Dataview 中的 YAML-Pkmer]]

# Dataview 语法实战

[PKMer_Dataview 语法实战](https://pkmer.cn/Pkmer-Docs/10-obsidian/obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/dataview/dataview%E8%AF%AD%E6%B3%95%E5%AE%9E%E6%88%98/dataview%E8%AF%AD%E6%B3%95%E5%AE%9E%E6%88%98/)

[[Dataview 测试实战]]