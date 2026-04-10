---
title: "Markdown 代码语法 | Markdown 教程"
source: "https://markdown.com.cn/basic-syntax/code.html"
author:
published:
created: 2025-10-20
description:
tags:
  - "clippings"
---
## Markdown 代码语法

要将单词或短语表示为代码，请将其包裹在反引号 (`` ` ``) 中。

| Markdown语法 | HTML | 预览效果 |
| --- | --- | --- |
| ``At the command prompt, type `nano`.`` | `At the command prompt, type <code>nano</code>. ` | At the command prompt, type `nano`. |

### 转义反引号

如果你要表示为代码的单词或短语中包含一个或多个反引号，则可以通过将单词或短语包裹在双反引号(` `` `)中。

| Markdown语法 | HTML | 预览效果 |
| --- | --- | --- |
| ``` ``Use `code` in your Markdown file.`` ``` | ``<code>Use `code` in your Markdown file.</code>`` | ``Use `code` in your Markdown file.`` |

### 代码块

要创建代码块，请将代码块的每一行缩进至少四个空格或一个制表符。

```
&lt;html>
      &lt;head>
      &lt;/head>
    &lt;/html>
```

渲染效果如下：

```
&lt;html>
  &lt;head>
  &lt;/head>
&lt;/html>
```