# LaTeX 教学重构中的 Python 转义陷阱

> 在教材原文中用 Python 脚本处理含大量 LaTeX 的 markdown 文件时，Python 字符串会把部分 `\` 开头的 LaTeX 命令误解释为控制字符转义序列。

## 受影响的控制字符

| LaTeX 命令 | 被解释为 | Python 字节 |
|---|---|---|
| `\varepsilon` | 垂直制表符 VT | 0x0B |
| `\frac` | 换页符 FF | 0x0C |
| `\rho` | 回车符 CR | 0x0D |
| `\nabla` | 换行符 LF | 0x0A |
| `\begin` | 退格符 BS | 0x08 |
| `\beta` | — | 0x1E (RS) |
| `\alpha` | — | 不转义 |
| `\gamma` | — | 不转义 |

## 根因

Python 的 `str` 和 `bytes` 类型中，`\n` `\r` `\v` `\f` `\b` `\a` 都被定义为控制字符转义。即使写成 `"\\rho"`，Python 的 `\\` 是反斜杠字面量，后续的 `r` 不会被转义——但**在 bytes 替换操作中**，`b'\\rho'` 的 `\\r` 仍可能被某些 Python 版本解释为 0x0D。

## 安全的替换方式

### 方案 A：用十六进制字节构建（推荐）

```python
# 替换 \rho (0x5C 0x72)
correct = b'\x5c\x72ho'      # \ + r + h + o
broken  = b'\x0dho'          # CR + h + o
raw = raw.replace(broken, correct)
```

### 方案 B：用 `patch` 或 `sed` 替代 Python

不要用 Python 脚本直接编辑含 LaTeX 的文件。用 `patch`（精准替换）、`sed`（批量替换）、`write_file`（全量重写）替代：

```bash
# sed 替换 \rho → \rho_{k}
sed -i 's/\\rho _ {/\\rho_{/g' 文件.md

# patch 精准替换一段文字
patch ...  # 用 Hermes 的 patch 工具，不走 Python
```

### 方案 C：raw string + 两次写入

```python
# raw string 不解释转义
text = r'\rho = \frac{\gamma_k}{\gamma_0}'
with open('temp.md', 'w', encoding='utf-8') as f:
    f.write(text)
```

## 验证命令

替换后检查公式完整性：

```bash
# 检查控制字符残留
python3 -c "
import sys
with open(sys.argv[1], 'rb') as f: raw = f.read()
for name, code in [('VT', 0x0b), ('FF', 0x0c), ('CR', 0x0d), ('LF', 0x0a), ('BS', 0x08)]:
    c = raw.count(bytes([code]))
    if c: print(f'{name} (0x{code:02x}): {c}')
"

# 检查关键 LaTeX 命令
grep -c '\\rho' 文件.md
grep -c '\\frac' 文件.md
grep -c '\\nabla' 文件.md
```
