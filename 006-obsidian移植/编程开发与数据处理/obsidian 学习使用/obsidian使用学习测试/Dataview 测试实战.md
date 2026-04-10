---
data: 2025-12-08T17:24:00
---

```dataview
LIST  without id file.link + "（属于 `"+ join(主题) + "`主题）"
FROM !"Obsidian"
FLATTEN 主题 as flattenedTopics
WHERE contains(this.主题, flattenedTopics)
AND file.name != this.file.name
limit 10
```
