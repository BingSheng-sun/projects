---
data: 2025-11-30T00:22:00
---

# 基础

## 常用示例汇总

### 查询未完成事项 'not done'

```tasks
not done
limit 10
```

### 按照创建日期查询 'created on ...'

```tasks
created on 2025-11-30
```

### 查询指定日期之前完成的任务 'done before ...'

```tasks
done before 2025-11-30
```

### 查询特定截止日期的任务 'due on ...'

```tasks
due on 2025-11-29
```

### 查询七天内创建的任务

```tasks
created after -7 days
```

### 查询下周的任务

```tasks
due after this week
due before next week
```

### 查询在特定时间段内完成的任务

```tasks
done after 2025-11-25
done before 2025-11-30
```

### 查询计划在未来七天内完成的任务

```tasks
due after today
due before in 7 days
```

### 查询没有指定截止日期的任务

```tasks
no due date
```

### 查询某个标签的任务

```tasks
tag includes #obsidian 
```

### 查询某个文件夹中的任务

```tasks
not done
path includes 规划
```

### 查询指定优先级的任务

```tasks
priority is high
```

### 查询任务标题中包含特定关键字的任务

```tasks
description includes Agricultural
```

### 查询优先级为中等并且未完成的任务

```tasks
not done
priority is medium
```

### 查询排除带有子任务的任务

```tasks
exclude sub-items
limit 10
```

### 查询任务状态为 “已取消” 任务

```tasks
filter by function task.status.symbol === '-'
```



## tasks 自定义过滤器

其实这个就是允许你在 tasks 插件内置的语法基础上，创造你自己的查询语法。（因为他类似于JavaScript的语法了）

### 案例1：日期属性

注意

利用新的 自定义过滤器，我们可以很容易实现

- 查询本周的相关任务，到期，创建，开始，重复等等
- 查询本月的相关任务，
- 查询指定**某一天** 所在的周/月的相关任务

注意：下面👇的2个代码块是联动的，点击上面，下面的会显示对应的注解。

1 任务描述长度2 所有星期二的任务3 查找今天或之前到期4 查找2023-09-30所在周到期

```
filter by function task.description.length > 100



filter by function task.due.format('dddd') === 'Tuesday'



filter by function task.due.moment?.isSameOrAfter(moment(), 'day') || false



filter by function task.due.moment?.isSame(moment('22023-09-30'), 'week') || false
```

1 任务描述长度2 所有星期二的任务3 查找今天或之前到期4 查找2023-09-30所在周到期

```
查找描述较长的任务。



查找周二到期的任务，也就是任何周二。
在非英语系统中，您可能需要以当地语言提供星期几



查找今天或更早到期的所有任务



查找2023-09-30这天，所在周，到期的所有任务
```

注意上面函数中可**替换** 的地方：

1. **日期**
    - due 到期时间，可替换为，created/starts/scheduled/happens
2. **时间范围函数**
    - isSame：一样的日期
    - isSameOrAfter：一样的日期或者之前
    - isSameOrBefore：一样的日期或者之后
3. **日期单位**
    - day：日
    - week：周
    - month：月
    - quarter：季度
    - year：年

### 案例2:文件夹

```
//查找所有截止日期为 2023-10-01 的任务。
filter by function task.due.moment?.isSame(moment('2023-10-01'), 'day') || false

//查找所有 2023-10-01 当周的所有任务
filter by function task.due.moment?.isSame(moment('2023-10-01'), 'week') || false

//只查询指定目录下任务，不包括子文件夹
filter by function task.file.folder === "Work/Projects/"

//查询指定目录下所有任务，包括子文件夹
filter by function task.file.folder.includes("Work/Projects/")
```



## tasks 的日期解密

### 1 tasks日期的秘密

当你使用 tasks 插件的时候，会看到各种的日期，那么他们之间的区别是什么呢？

- Due：到期日期
- Scheduled：计划日期
- Start：开始日期

日期的使用

**在tasks中使用日期，推荐只使用一种就够了**

在 Obsidian 的 Tasks 插件中，`start` 和 `scheduled` 的概念确实非常相似，但它们有细微的区别，主要体现在它们的语义和使用场景上。让我们来详细解释一下。

### 2 Scheduled 和 Start 的区别

省流版

从语法上来说，显示的结果没有多少区别，区别的是他们的定义，是为了让你梳理自己的执行思路。

- 一个是**强调计划性**，并不是一定要做，也不会提示过期
- 一个是明确任务的**实际开始日期**，表明从这个日期起任务已经在进行中

#### 2.1 Scheduled 日期

`scheduled` 是指任务计划处理的日期，它强调的是“**计划**在某一天处理”这个概念，通常用于提醒用户在该日期开始关注某项任务。

这个日期并不意味着任务必须在当天开始执行，而是一个标记，表示你在那个时间点开始考虑或查看该任务。

#### 2.2 Start 日期

`start` 日期则更加明确地表示任务实际开始的日期，意味着任务从这一天开始正式进行。在许多任务管理系统中，`start` 日期通常用于标记任务实际的开始时间。

#### 2.3 区别总结

- **语义区别**：
    - `scheduled` 更加灵活，表示“**计划**在某一天开始处理”。
    - `start` 则更加明确，表示任务“从这一天正式开始”。

使用场景

- `scheduled` 更适合用于提醒自己在**某天开始考虑一项任务，但任务可能不会在那天正式开始**。
- `start` 则用于明确任务的**实际开始日期**，表明**从这个日期起任务已经在进行中**。

#### 2.4 实际使用中的关系

在很多情况下，`scheduled` 和 `start` 可以表示相同的日期，尤其是在你的任务管理系统中这两个概念有重叠的情况下。

但在 Obsidian Tasks 插件中，**通常你会选择其中之一来使用**，因为它们在插件中并没有严格的功能性区别。你可以根据个人习惯选择更适合你的日期属性。

#### 2.5 示例对比

```
- [ ] 在咖啡豆文档站学习task语法 

  scheduled: 2024-09-05
  start: 2024-09-05
  due: 2024-09-10
```

1  
2  
3  
4  
5  

在这个例子中，你可能会使用

- `scheduled` 来提醒自己在 9 月 5 日查看这个任务，
- 而 `start` 则表示任务从 9 月 5 日起正式开始。
- 而 `due` 表示任务在 9 月 10 日过期，应该在这个日期前完成他。

#### 2.6 总结

- **Scheduled** 更**强调提醒功能**，表示任务计划的处理时间。
- **Start** 更加具体，表示任务正式开始的时间。

你可以根据个人偏好和任务管理的需求，选择在 Obsidian 中使用 `start` 或 `scheduled` 来标记任务的开始时间。

在 Obsidian 的 Tasks 插件中，`scheduled` 和 `due` 是两个重要的日期属性，它们有不同的用途，帮助用户管理任务的时间安排。以下是两者的区别：

### 3 Scheduled 和 Due 的区别

#### 3.1 Scheduled 日期

`scheduled` 日期是指任务计划开始的日期。这并不意味着任务必须在这一天完成，而是你**希望在这一天开始处理**这项任务。

这个属性有助于你在特定的时间点**开始关注某个任务**，但它**不会触发任何逾期提醒**。

**示例**：

```
- [ ] 在咖啡豆文档站学习task语法 

  scheduled: 2024-09-10
```

1  
2  
3  

在这个示例中，

- “在咖啡豆文档站学习task语法 ” 任务计划在 2024 年 9 月 10 日开始，
- 但并不意味着必须在这一天完成。

#### 3.2 Due 日期

`due` 日期是任务的截止日期，这意味着任务必须在这个日期或之前完成。

`due` 日期通常用于**设定最后期限**，以确保任务在特定日期之前完成。如果任务超过 `due` 日期而未完成，则会被视为**逾期**。

**示例**：

```
- [ ] 在咖啡豆文档站学习task语法 

  due: 2024-09-15
```

1  
2  
3  

在这个示例中，

- “在咖啡豆文档站学习task语法 ” 任务必须在 2024 年 9 月 15 日或之前完成，否则就**会逾期**。

#### 3.3 结合使用 `scheduled` 和 `due`

结合使用

在任务管理中，你可以同时使用 `scheduled` 和 `due` 来更精确地规划任务的开始和结束。 例如，

- 一个任务可以有一个计划开始的日期（`scheduled`），
- 以及一个必须完成的最后日期（`due`）。

**示例**：

```
- [ ] 在咖啡豆文档站学习task语法 
  
  scheduled: 2024-09-01
  due: 2024-09-10
```

1  
2  
3  
4  

在这个例子中，

- 任务计划 `在咖啡豆文档站学习task语法` 从 2024 年 9 月 1 日开始，
- 最晚需要在 2024 年 9 月 10 日完成。
- 这使你有足够的时间来完成任务，并明确了什么时候该开始和结束。

#### 3.4 总结

总结

- **Scheduled**: 用于表示任务计划开始的日期，帮助你在特定时间开始处理任务。
- **Due**: 用于表示任务的截止日期，明确任务必须在何时完成。

这两个日期属性可以独立使用，也可以结合使用，以便更灵活地管理任务的时间安排。

**推荐使用一种日期**

**还是这句话，推荐只之用一种日期，更加的方便和容易理解，推荐使用 `due` 日期**



## task语法查速查表  

[tasks语法快速参考 | obsidian文档咖啡豆版](https://obsidian.vip/zh/tasks/tasks-Quick-Reference)
建议多看这个里面的内容，这个就是所有的tasks语法发的一览表，忘记语法的时候查询比较方便一点。

更新说明

- 2023-09-30 更新，包括新版中的自定义过滤器等新特性

|                                                                                                                                                                                                                                                                                                                                 |                                          |                        |                        |                                                           |     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ---------------------- | ---------------------- | --------------------------------------------------------- | --- |
| **Filters\|过滤器**                                                                                                                                                                                                                                                                                                                | **Sort\|排序**                             | **Group\|分组**          | **Display\|展示**        | **Scripting \| JavaScript脚本**                             |     |
| **Status**\|状态                                                                                                                                                                                                                                                                                                                  |                                          |                        |                        |                                                           |     |
| `done` `not done`                                                                                                                                                                                                                                                                                                               | `sort by status`                         | `group by status`      |                        | `task.isDone`                                             |     |
| `status.name (includes, does not include) <string>` `status.name (regex matches, regex does not match) /regex/i`                                                                                                                                                                                                                | `sort by status.name`                    | `group by status.name` |                        | `task.status.name`                                        |     |
| `status.type (is, is not) (TODO, DONE, IN_PROGRESS, CANCELLED, NON_TASK)`                                                                                                                                                                                                                                                       | `sort by status.type`                    | `group by status.type` |                        | `task.status.type`                                        |     |
|                                                                                                                                                                                                                                                                                                                                 |                                          |                        |                        | `task.status.symbol`                                      |     |
|                                                                                                                                                                                                                                                                                                                                 |                                          |                        |                        | `task.status.nextSymbol`                                  |     |
| **Dates**\|日期                                                                                                                                                                                                                                                                                                                   |                                          |                        |                        |                                                           |     |
| `done (on, before, after, on or before, on or after) <date>` `done (in, before, after, in or before, in or after) ...` `... YYYY-MM-DD YYYY-MM-DD` `... (last, this, next) (week, month, quarter, year)` `... (YYYY-Www,YYYY-mm, YYYY-Qq, YYYY)` `has done date` `no done date` `done date is invalid`                          | `sort by done`                           | `group by done`        | `hide done date`       | `task.done`                                               |     |
| `created (on, before, after, on or before, on or after) <date>` `created (in, before, after, in or before, in or after) ...` `... YYYY-MM-DD YYYY-MM-DD` `... (last, this, next) (week, month, quarter, year)` `... (YYYY-Www,YYYY-mm, YYYY-Qq, YYYY)` `has created date` `no created date` `created date is invalid`           | `sort by created`                        | `group by created`     | `hide created date`    | `task.created`                                            |     |
| `starts (on, before, after, on or before, on or after) <date>` `starts (in, before, after, in or before, in or after) ...` `... YYYY-MM-DD YYYY-MM-DD` `... (last, this, next) (week, month, quarter, year)` `... (YYYY-Www,YYYY-mm, YYYY-Qq, YYYY)` `has start date` `no start date` `start date is invalid`                   | `sort by start`                          | `group by start`       | `hide start date`      | `task.start`                                              |     |
| `scheduled (on, before, after, on or before, on or after) <date>` `scheduled (in, before, after, in or before, in or after) ...` `... YYYY-MM-DD YYYY-MM-DD` `... (last, this, next) (week, month, quarter, year)` `... (YYYY-Www,YYYY-mm, YYYY-Qq, YYYY)` `has scheduled date` `no scheduled date` `scheduled date is invalid` | `sort by scheduled`                      | `group by scheduled`   | `hide scheduled date`  | `task.scheduled`                                          |     |
| `due (on, before, after, on or before, on or after) <date>` `due (in, before, after, in or before, in or after) ...` `... YYYY-MM-DD YYYY-MM-DD` `... (last, this, next) (week, month, quarter, year)` `... (YYYY-Www,YYYY-mm, YYYY-Qq, YYYY)` `has due date` `no due date` `due date is invalid`                               | `sort by due`                            | `group by due`         | `hide due date`        | `task.due`                                                |     |
| `happens (on, before, after, on or before, on or after) <date>` `happens (in, before, after, in or before, in or after) ...` `... YYYY-MM-DD YYYY-MM-DD` `... (last, this, next) (week, month, quarter, year)` `... (YYYY-Www,YYYY-mm, YYYY-Qq, YYYY)` `has happens date` `no happens date`                                     | `sort by happens`                        | `group by happens`     |                        | `task.happens`                                            |     |
| **Recurrence**\|重复                                                                                                                                                                                                                                                                                                              |                                          |                        |                        |                                                           |     |
| `is recurring` `is not recurring`                                                                                                                                                                                                                                                                                               | `sort by recurring`                      | `group by recurring`   |                        | `task.isRecurring`                                        |     |
| `recurrence (includes, does not include) <string>` `recurrence (regex matches, regex does not match) /regex/i`                                                                                                                                                                                                                  |                                          | `group by recurrence`  | `hide recurrence rule` | `task.recurrenceRule`                                     |     |
| **Priority** and **urgency** 重要\|紧急                                                                                                                                                                                                                                                                                             |                                          |                        |                        |                                                           |     |
| `priority is (above, below, not)? (lowest, low, none, medium, high, highest)`                                                                                                                                                                                                                                                   | `sort by priority`                       | `group by priority`    | `hide priority`        | `task.priorityName` `task.priorityNumber`                 |     |
|                                                                                                                                                                                                                                                                                                                                 | `sort by urgency`                        | `group by urgency`     | `show urgency`         | `task.urgency`                                            |     |
| **File properties**\|文件属性                                                                                                                                                                                                                                                                                                       |                                          |                        |                        |                                                           |     |
| `path (includes, does not include) <path>` `path (regex matches, regex does not match) /regex/i` `path includes {​{query.file.path}}` `path includes {​{query.file.pathWithoutExtension}}`                                                                                                                                      | `sort by path`                           | `group by path`        |                        | `task.file.path` `task.file.pathWithoutExtension`         |     |
| `root (includes, does not include) <root>` `root (regex matches, regex does not match) /regex/i` `root includes {​{query.file.root}}`                                                                                                                                                                                           |                                          | `group by root`        |                        | `task.file.root`                                          |     |
| `folder (includes, does not include) <folder>` `folder (regex matches, regex does not match) /regex/i` `folder includes {​{query.file.folder}}`                                                                                                                                                                                 |                                          | `group by folder`      |                        | `task.file.folder`                                        |     |
| `filename (includes, does not include) <filename>` `filename (regex matches, regex does not match) /regex/i` `filename includes {​{query.file.filename}}` `filename includes {​{query.file.filenameWithoutExtension}}`                                                                                                          | `sort by filename`                       | `group by filename`    |                        | `task.file.filename` `task.file.filenameWithoutExtension` |     |
| `heading (includes, does not include) <string>` `heading (regex matches, regex does not match) /regex/i`                                                                                                                                                                                                                        | `sort by heading`                        | `group by heading`     |                        | `task.hasHeading` `task.heading`                          |     |
|                                                                                                                                                                                                                                                                                                                                 |                                          | `group by backlink`    | `hide backlink`        |                                                           |     |
| **Description**, **Tags** and other odds and ends 描述，标签和其他                                                                                                                                                                                                                                                                      |                                          |                        |                        |                                                           |     |
| `description (includes, does not include) <string>` `description (regex matches, regex does not match) /regex/i`                                                                                                                                                                                                                | `sort by description`                    |                        |                        | `task.description` `task.descriptionWithoutTags`          |     |
| `has tags` `no tags` `tag (includes, does not include) <tag>` `tags (include, do not include) <tag>` `tag (regex matches, regex does not match) /regex/i` `tags (regex matches, regex does not match) /regex/i`                                                                                                                 | `sort by tag` `sort by tag <tag_number>` | `group by tags`        | `hide tags`            | `task.tags`                                               |     |
|                                                                                                                                                                                                                                                                                                                                 |                                          |                        |                        | `task.originalMarkdown`                                   |     |
| **Scripting** JavaScript脚本                                                                                                                                                                                                                                                                                                      |                                          |                        |                        |                                                           |     |
| `filter by function`                                                                                                                                                                                                                                                                                                            |                                          | `group by function`    |                        |                                                           |     |
| **Combining Filters**组合过滤器                                                                                                                                                                                                                                                                                                      |                                          |                        |                        |                                                           |     |
| `(filter 1) AND (filter 2)`                                                                                                                                                                                                                                                                                                     |                                          |                        |                        |                                                           |     |
| `(filter 1) OR (filter 2)`                                                                                                                                                                                                                                                                                                      |                                          |                        |                        |                                                           |     |
| `NOT (filter 1)`                                                                                                                                                                                                                                                                                                                |                                          |                        |                        |                                                           |     |
| `(filter 1) XOR (filter 2)`                                                                                                                                                                                                                                                                                                     |                                          |                        |                        |                                                           |     |
| `(filter 1) AND NOT (filter 2)`                                                                                                                                                                                                                                                                                                 |                                          |                        |                        |                                                           |     |
| `(filter 1) OR NOT (filter 2)`                                                                                                                                                                                                                                                                                                  |                                          |                        |                        |                                                           |     |
| `(filter 1) AND ((filter 2) OR (filter 3))`                                                                                                                                                                                                                                                                                     |                                          |                        |                        |                                                           |     |
| **Other Filter Options** 其他过滤器选项                                                                                                                                                                                                                                                                                                |                                          |                        |                        |                                                           |     |
| `exclude sub-items`                                                                                                                                                                                                                                                                                                             |                                          |                        |                        |                                                           |     |
| `limit to <number> tasks` `limit <number>`                                                                                                                                                                                                                                                                                      |                                          |                        |                        |                                                           |     |
| `limit groups to <number> tasks` `limit groups <number>`                                                                                                                                                                                                                                                                        |                                          |                        |                        |                                                           |     |
| **Other Layout Options**其他布局选项                                                                                                                                                                                                                                                                                                  |                                          |                        |                        |                                                           |     |
| `hide edit button`                                                                                                                                                                                                                                                                                                              |                                          |                        |                        |                                                           |     |
| `hide task count`                                                                                                                                                                                                                                                                                                               |                                          |                        |                        |                                                           |     |
| `short mode`                                                                                                                                                                                                                                                                                                                    |                                          |                        |                        |                                                           |     |


# 进阶

## 进阶（一）

### 3 tasks插件的使用方法

#### 3.1 安装

插件安装

打开 obsidian → 设置 ⚙️ → 第三方插件 → 社区插件市场，搜索关键字安装

注意：你需要关闭第三方插件的**安全模式**，才能安装社区插件，建议关闭。

#### 3.2 配置

tasks 插件无需过多配置。但是有一点要注意，经过测试，如果不开启 Global task filter的话，会导致obsidian很卡。

WARNING

强烈推荐：安装 tasks 插件后，开启 Global task filter 全局标签过滤。

- 打开插件 → 设置 找到tasks ，找到 Global task filter 全局标签过滤
- 在这里填写 `#task` 。意思是过滤包含`#task`标签的任务。

#### 3.3 使用

**常规添加task任务：**

1. 首先添加任务，输入内容
2. 然后在 命令面板，输入 task，选择Tasks: Create or edit task。
3. 在面板依次填入任务信息和完成时间等信息。
4. 或者直接从第二步也可以

**推荐做法：**

自定义tasks快捷键

- 打开 obsidian → 设置 ⚙️ → 快捷键，
- 搜索`task`，找到 `Tasks: Create or edit task`，点后面的 + 号图标。添加你的快捷键。我的设置为 `Ctrl + T` 。

在文档中输入文字，然后按自定义的快捷键 `Ctrl + T` 。就会弹出来 tasks 插件的面板。会自动添加`#task` 标签给任务了。

注意：

WARNING

因为我们打开了`Global task filter` 全局标签过滤，只会检索包含标签`#task` 的任务。所以要注意添加。

**tasks任务示例：**

- [x] 这个是系统自带的待办事项 ✅ 2025-12-10
- [x] 这个是系统自带的待办事项完成
- [x] #task 这个是tasks插件添加的任务 ✅ 2025-12-10

### 4 task面板元素

**弹出task的面板，界面的意思如下：**

1. Description：任务描述，就是正文
2. Priority：重要程度，依次是 Low 低、Normal一般、Medium中等、High高
3. Recurs：循环任务，按周期
4. Due：到期时间
5. Scheduled：计划任务
6. Start：开始时间
7. Status 状态
    - todo，计划
    - Done
    - In Progress
    - Cancelled

按需填写

按需填入所需要的信息。我重点使用的只有一个，就是Due 到期时间。当然这与我的任务管理方案有关系，是GTD任务管理的一种拓展。

如果你要实现上图所示的GTD四象限的图示，那你需要填写 Priority：重要程序，依次是 Low 低、Normal一般、Medium中等、High高。

图标不要删除

当填写完成后，点击 Apply 应用。刚刚的任务就会转化成 tasks 插件专有任务，添加了`task`标签和特定的emoji图标，这些图标不要删除。是提供给tasks插件查询的

本章节讲解了 tasks 的基本操作，和注意的事项。以及增加快捷键的技巧。下一节将讲解tasks 的语法。


## 进阶（二）

[[Tasks进阶(2)  obsidian文档咖啡豆版]]

