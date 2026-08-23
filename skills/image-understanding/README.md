# image-understanding

本 skill 使用本地 Python 脚本调用 `Qwen/Qwen2-VL-2B-Instruct`，支持图片描述和图片问答，中文效果较好。

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python .\scripts\main.py --check-env
python .\scripts\main.py "C:\path\to\image.png"
```

首次真实运行会自动下载模型。更完整的安装和离线说明见 `references/model-install.md`。

## Examples

```powershell
python .\scripts\main.py "C:\path\to\image.png" --length short
python .\scripts\main.py "C:\path\to\image.png" --length normal
python .\scripts\main.py "C:\path\to\image.png" --length long
python .\scripts\main.py "C:\path\to\image.png" "这张图片里有什么文字？"
```

如需使用本地模型目录：

```powershell
python .\scripts\main.py "C:\path\to\image.png" --model "D:\models\Qwen2-VL-2B-Instruct"
```
