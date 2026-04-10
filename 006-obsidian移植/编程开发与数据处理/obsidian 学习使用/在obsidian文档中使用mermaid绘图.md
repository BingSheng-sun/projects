---
aliases:
  - 如何在文档中更好地工作-在markdow文件中学习、实践和思考mermaid
tags:
  - obsidian
  - mermaid
start: 2026-03-26
end:
duration:
---
```
classDiagram  
    direction LR  
  
    %% ############## 核心类 ##############  
    class Note {  
        + String title  
        + String content  
        + Date createTime  
        + Date updateTime  
        + List~Tag~ tags  
        + void addTag()  
        + void removeTag()  
        + void updateContent()  
    }  
  
    class Task {  
        + String id  
        + String name  
        + String status  
        + int duration  
        + Date startTime  
        + Date endTime  
        + void start()  
        + void finish()  
        + void delay()  
    }  
  
    class GanttChart {  
        + String title  
        + dateFormat  
        + axisFormat  
        + List~Task~ tasks  
        + void addTask()  
        + void removeTask()  
        + void adjustInterval()  
    }  
  
    class Config {  
        + String theme  
        + bool excludeWeekends  
        + String textPosition  
        + bool showData  
        + void saveConfig()  
        + void loadConfig()  
    }  
  
    %% ############## 辅助类 ##############  
    class Tag {  
        + String name  
        + String color  
    }  
  
    class Section {  
        + String name  
        + List~Task~ tasks  
        + void addTask()  
    }  
  
    %% ############## 类关系 ##############  
    %% 1. 笔记拥有多个标签（关联）  
    Note "*" -- "*" Tag : 包含  
  
    %% 2. 甘特图包含多个任务（组合）  
    GanttChart *-- "*" Task : 管理  
  
    %% 3. 任务属于某个Section（聚合）  
    Section o-- "*" Task : 包含  
  
    %% 4. 甘特图依赖配置（依赖）  
    GanttChart ..> Config : 使用  
  
    %% 5. 笔记与任务关联（一个笔记对应多个任务）  
    Note "1" -- "*" Task : 管理
```

当一个代码规范被创造出来的时候，他一定是符合大部分代码工作者的习惯而且是适应创作者脑海里的时代判断的，而我作为学习者所要做的就是理解。[^1] 

> [!note]- AI
> 当这种理解与具体工具结合时，便能高效地将其应用于实践。比如，在 Obsidian 这款以“关联思考”为核心的笔记软件中，利用 Mermaid 语法绘制图表，就是一种将结构化思维可视化的强大方式。
> 
> Mermaid 的语法简洁直观，正如一个设计良好的代码规范，它能让用户专注于内容逻辑而非绘图细节。在 Obsidian 中，你只需创建一个代码块，并将语言标识设为 `mermaid`，即可开始创作。
> 
> ### 一个简单的流程图示例
> 
> ```mermaid
> graph TD
>     A[打开Obsidian] --> B(创建/编辑笔记)
>     B --> C{需要图解逻辑?}
>     C -->|是| D[插入mermaid代码块]
>     C -->|否| E[继续文本记录]
>     D --> F[使用语法绘制图表]
>     F --> G[即时预览与调整]
>     G --> B
> ```

[关于 Mermaid | Mermaid 中文网](https://mermaid.nodejs.cn/intro/)

# Log

> [!note]- 3.26
> 学习mermaid是一个不小的项目，我是说，它有着非常丰富且详细的教程文档。

# 教程内容

## CSDN-Mermaid 使用-斐夷所非

### 流程图（Flowchart）

#### 适用场景

业务流程、算法步骤、工作流、系统逻辑梳理

#### 布局方向

- `TB`：从上到下（默认）
- `BT`：从下到上
- `LR`：从左到右
- `RL`：从右到左

#### 节点类型

| 节点形状    | 语法         | 用途       |
| :------ | :--------- | :------- |
| 矩形      | `id[文字]`   | 普通步骤     |
| 圆角矩形    | `id(文字)`   | 起止/常规步骤  |
| 体育场形    | `id([文字])` | 特殊步骤     |
| 子程序形    | `id[[文字]]` | 子流程      |
| 圆柱形     | `id[(文字)]` | 数据存储/数据库 |
| 圆形      | `id((文字))` | 开始/结束    |
| 菱形      | `id{文字}`   | 条件判断     |
| 六边形     | `id{{文字}}` | 事件/过程    |
| 平行四边形   | `id[/文字/]` | 输入       |
| 反向平行四边形 | `id[\文字\]` | 输出       |

#### 连线样式

- 实线：`A --> B`
- 粗实线：`A ==> B`
- 虚线：`A -.-> B`
- 无箭头线：`A --- B`
- 双向箭头：`A <--> B`
- 带文字连线：`A -->|条件| B`

#### 高级用法

1. **并行节点**：`B & C --> D`
2. **子图**：

```
graph LR
subgraph 子图名称[子图标题]
direction LR
节点1 --> 节点2
end
A --> 子图名称 --> B
```

#### 示例代码

> [!note]-
> ```
> graph TB
> start((start)) --> distribute([special])
> distribute ==> simple[simple]
> distribute -.-> simple2[simple2]
> simple & simple2 --- if{if}
> if -->|process| duration{{duration}}
> duration <--> vault[(vault)]
> vault -.-> sub[[sub]]
> sub --- input[/input/]
> duration --> output[\output\]
> input -.-> output
> ```

### 时序图（Sequence Diagram）

#### 适用场景

系统交互、接口调用、消息传递、业务时序梳理

#### 基础语法

```
sequenceDiagram
participant/actor 参与者1
participant/actor 参与者2
消息流向
```

#### 语法

1. **参与者**
    - `participant`：普通参与者
    - `actor`：角色/用户
2. **消息类型**
    - 同步消息：`A ->> B`
    - 异步消息：`A -->> B`
    - 无返回消息：`A -) B`
3. **激活状态**
    - 开启：`activate A` / `A ->> +B`
    - 关闭：`deactivate A` / `B -->> -A`
4. **循环**：`loop 循环说明 ... end`
5. **并行**：`par 并行说明 ... end`
6. **注释**：`Note left/right of 参与者: 注释内容`
7. **自动编号**：`autonumber`

#### 示例

> [!note]-
> ```
> sequenceDiagram
> actor 孙振烁
> participant 大脑
> participant 手
> participant obsidian
> 
> Note left of 孙振烁: 他是一个大帅比
> 孙振烁 ->> +大脑: 要写笔记
> 大脑 ->> +手: 死手快打开电脑码字！
> 手 -) 大脑: 啥？😴😴😴
> 大脑 ->> 手: 打开obsidian
> 
> par 哦！
>     手 -->> 大脑: 明白🫡
>     手 ->> +obsidian: obsidian启动
> end
> 
> 大脑 ->> 手: 我想到了这个，还有这个……
> 
> loop 收到🫡，我写写写……
>     手 ->> obsidian: 写这个，还有那个……
> end
> 
> obsidian -->> -手: 被塞满了🤪
> 手 -->> -大脑: 任务完成！
> 大脑 -->> -孙振烁: 你爽了没，反正我爽了
> ```

### 甘特图（Gantt Chart）

#### 适用场景

项目规划、进度管理、任务排期、里程碑跟踪

#### 基础语法

```
gantt
dateFormat 日期格式
axisFormat 坐标轴格式
excludes 排除日期
title 图表标题
section 分组名称
任务定义
```

#### 语法

1. **日期格式**：`YYYY-MM-DD`
2. **排除日期**：`weekends`、`sunday`、具体日期
3. **任务状态**
    - `done`：已完成
    - `active`：进行中
    - `crit`：关键任务
    - `milestone`：里程碑
4. **任务时长**：`d`（天）、`w`（周）、`y`（年）
5. **任务依赖**：`after 任务ID`

#### 示例

> [!example]-
> ```self
> gantt
> 	dateFormat MM-DD
> 	axisFormat %m-%d
> 	excludes weekends 
> 	title obsidian进阶计划
> 
> section 笔记设计(2026)
> 	需求分析: active, p1, 04-02, 7d
> 	内容模块设计: crit, p2, after p1, 3d
> 	应用体验与思考: p3, after p2, 14d
> 	
> section 反思评估
> 	效果评估: crit, p4, after p3, 2d
> 	发散推广与记忆留存: milestone, p5, after p4, 1d
> ```
> 
> ```example
> gantt
> dateFormat YYYY-MM-DD
> axisFormat %Y-%m-%d
> excludes weekends
> title 项目开发计划
> section 研发
> 需求分析: done, a1, 2025-01-01, 5d
> 开发编码: active, a2, after a1, 15d
> 测试验收: a3, after a2, 7d
> section 发布
> 预发布: a4, after a3, 2d
> 正式上线: milestone, a5, after a4, 0d
> ```

### 饼图（Pie Chart）

#### 适用场景

数据占比、资源分布、比例分析

#### 基础语法

```
pie
title 图表标题
"数据项1": 数值1
"数据项2": 数值2
```

#### 语法说明

1. 数值支持整数、小数，最多两位小数
2. 无需总和为 100，自动计算比例
3. 可通过 `init` 配置样式、文字位置

#### 示例

> [!example]-
> ```self
> pie
> title 时间金币花费
> %% 你一天有多少时间？假设为10:00-22:00，0.5h为一个金币，我一天只有24枚金币
> 
> "obsidian": 10
> "exercise": 3
> "reading": 4
> "Game": 3
> "Anime and Film": 4
> ```
> 
> ```example
> pie
> title 月度开销占比
> "生活开销": 2000
> "娱乐开销": 1000
> "其他开销": 800
> ```

### 类图（Class Diagram）

#### 适用场景

面向对象设计、系统架构 、数据结构建模

#### 基础语法

```
classDiagram
class 类名 {
权限修饰符 属性类型 属性名
权限修饰符 方法名(参数) 返回值类型
}
类关系
```

#### 语法

1. **权限修饰符**
    - `+`：公共
    - `-`：私有
    - `#`：保护
    - `~`：包内可见
    - `$`：静态
2. **类关系**
    - 继承：`<|--`
    - 实现：`--|>`
    - 关联：`--`

#### 示例

> [!note]-
> ```AI
> classDiagram
>     direction LR
> 
>     %% ############## 核心类 ##############
>     class Note {
>         + String title
>         + String content
>         + Date createTime
>         + Date updateTime
>         + List~Tag~ tags
>         + void addTag()
>         + void removeTag()
>         + void updateContent()
>     }
> 
>     class Task {
>         + String id
>         + String name
>         + String status
>         + int duration
>         + Date startTime
>         + Date endTime
>         + void start()
>         + void finish()
>         + void delay()
>     }
> 
>     class GanttChart {
>         + String title
>         + dateFormat
>         + axisFormat
>         + List~Task~ tasks
>         + void addTask()
>         + void removeTask()
>         + void adjustInterval()
>     }
> 
>     class Config {
>         + String theme
>         + bool excludeWeekends
>         + String textPosition
>         + bool showData
>         + void saveConfig()
>         + void loadConfig()
>     }
> 
>     %% ############## 辅助类 ##############
>     class Tag {
>         + String name
>         + String color
>     }
> 
>     class Section {
>         + String name
>         + List~Task~ tasks
>         + void addTask()
>     }
> 
>     %% ############## 类关系 ##############
>     %% 1. 笔记拥有多个标签（关联）
>     Note "*" -- "*" Tag : 包含
> 
>     %% 2. 甘特图包含多个任务（组合）
>     GanttChart *-- "*" Task : 管理
> 
>     %% 3. 任务属于某个Section（聚合）
>     Section o-- "*" Task : 包含
> 
>     %% 4. 甘特图依赖配置（依赖）
>     GanttChart ..> Config : 使用
> 
>     %% 5. 笔记与任务关联（一个笔记对应多个任务）
>     Note "1" -- "*" Task : 管理
> ```
> 
> ```example
> classDiagram
> class 动物 {
> +String name
> +void eat()
> }
> class 鸟类 {
> +float wingSpan
> +void fly()
> }
> 动物 <|-- 鸟类
> ```


[^1]: [[2026-03-26#^e357f5]]
