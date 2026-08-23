---
name: image-understanding
description: >
  Use this skill whenever the user asks about an image, asks to describe an image,
  asks to understand what's in an image, asks to analyze a picture, or mentions
  image recognition. Trigger on phrases like "这张图片里有什么", "描述这张图",
  "识别图片", "图片分析", "what's in this image", "describe this image",
  "analyze this picture", "图片理解". Also trigger when the user provides an image
  file path and asks questions about it. Use this skill even if the user doesn't
  explicitly say "analyze" or "understand"; if they mention an image file and want
  to know something about its content, this skill applies. Supports Chinese output
  through a local Qwen2-VL-2B-Instruct vision-language model.
---

# 图片理解 Skill

使用随 skill 分发的 Python 脚本调用 `Qwen/Qwen2-VL-2B-Instruct` 视觉语言模型分析图片，支持中文描述和图片问答。

## Bundled Files

Relative to this skill directory:

```txt
scripts/main.py                 # 图片理解 CLI
requirements.txt                # Python 依赖
references/model-install.md     # 模型下载、离线、本地模型目录说明
```

Do not depend on a hard-coded machine path such as `F:\image_recognize_llm\main.py`. Use the bundled script in this skill directory.

## Environment Check First

Before image inference, verify the script and image path exist, then run the environment check.

```powershell
$skillDir = "<path-to-installed-skill>"
Test-Path -LiteralPath "$skillDir\scripts\main.py"
Test-Path -LiteralPath "<image_path>"
python "$skillDir\scripts\main.py" --check-env
```

If `scripts/main.py` is missing, tell the user the skill installation is incomplete.

If the image path is missing, ask the user for a valid image path.

If `--check-env` reports missing dependencies, stop and tell the user to install dependencies from the skill directory:

```powershell
python -m pip install -r requirements.txt
```

For full setup, point them to `references/model-install.md`.

## Usage

Run commands from PowerShell. For first-time model download, make sure Hugging Face offline mode is disabled:

```powershell
$env:HF_HUB_OFFLINE = ""
```

### 1. 图片描述（默认）

获取图片的详细 long caption 描述：

```powershell
$env:HF_HUB_OFFLINE = ""
python "$skillDir\scripts\main.py" "<image_path>"
```

### 2. 图片问答

对图片内容提问：

```powershell
$env:HF_HUB_OFFLINE = ""
python "$skillDir\scripts\main.py" "<image_path>" "你的问题"
```

### 3. 指定描述长度

```powershell
$env:HF_HUB_OFFLINE = ""
python "$skillDir\scripts\main.py" "<image_path>" --length short

$env:HF_HUB_OFFLINE = ""
python "$skillDir\scripts\main.py" "<image_path>" --length normal

$env:HF_HUB_OFFLINE = ""
python "$skillDir\scripts\main.py" "<image_path>" --length long
```

Length options:

- `short`: 一句话
- `normal`: 普通描述
- `long`: 详细描述，默认行为

### 4. 使用本地模型目录

If the user already has the model downloaded locally, pass the model directory:

```powershell
python "$skillDir\scripts\main.py" "<image_path>" --model "D:\models\Qwen2-VL-2B-Instruct"
```

Or set:

```powershell
$env:IMAGE_UNDERSTANDING_MODEL = "D:\models\Qwen2-VL-2B-Instruct"
python "$skillDir\scripts\main.py" "<image_path>"
```

## Agent Workflow

1. Identify the image path from the user request. If the user did not provide a path or uploaded image reference, ask for it.
2. Resolve the installed skill directory and verify `scripts/main.py` exists.
3. Verify the image path exists with `Test-Path -LiteralPath`.
4. Run `python "$skillDir\scripts\main.py" --check-env`.
5. If dependencies are missing, stop and give the install command plus `references/model-install.md`.
6. Choose mode:
   - If the user asks for a general description, run default long caption unless they requested another length.
   - If the user asks a specific question, pass that question as the second argument.
   - If the user requests a short/normal/long description, pass `--length`.
7. Return the model output directly in the user's language. If the model output is unclear, say so instead of inventing details.

## Missing Model Behavior

If the model is not already cached, the first inference run downloads `Qwen/Qwen2-VL-2B-Instruct` from Hugging Face. This is expected.

If download fails because the machine is offline, authenticated incorrectly, or cannot reach Hugging Face, tell the user:

```text
模型还没有安装或缓存。请按 references/model-install.md 下载模型，或者用 --model 指定本地模型目录。
```

Do not invent a fallback visual analysis. This skill requires the local model or a valid local model directory.

## Notes

- 模型首次真实运行可能需要下载数 GB 权重；下载完成后才是一装可用。
- 模型首次加载约需数秒到数十秒，取决于硬件和磁盘速度。
- 图片过大时脚本会自动缩放（`max_pixels=401408`），不需要手动预处理。
- 图片路径不存在会直接报错，所以必须先验证路径。
- Always quote Windows paths, especially if the image path contains spaces.
- Do not use OCR-only tools for this skill; use the local vision-language model above.
