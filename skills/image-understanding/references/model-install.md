# Image Understanding Model Setup

This skill uses `Qwen/Qwen2-VL-2B-Instruct` through Hugging Face Transformers.

## Install

From this skill directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For CUDA builds of PyTorch, use the install command recommended for your machine at:

```text
https://pytorch.org/get-started/locally/
```

Then install the remaining dependencies:

```powershell
python -m pip install transformers accelerate pillow sentencepiece
```

## Check The Environment

```powershell
python .\scripts\main.py --check-env
```

The check verifies Python imports and reports CUDA availability. It does not load or download the model.

## First Model Download

The first real image run downloads `Qwen/Qwen2-VL-2B-Instruct` into the local Hugging Face cache:

```powershell
$env:HF_HUB_OFFLINE = ""
python .\scripts\main.py "C:\path\to\image.png" --length short
```

If the network cannot reach Hugging Face, download the model manually on another machine and copy it locally.

## Use A Local Model Directory

If the model is already downloaded somewhere else, pass its directory:

```powershell
python .\scripts\main.py "C:\path\to\image.png" --model "D:\models\Qwen2-VL-2B-Instruct"
```

Or set an environment variable:

```powershell
$env:IMAGE_UNDERSTANDING_MODEL = "D:\models\Qwen2-VL-2B-Instruct"
python .\scripts\main.py "C:\path\to\image.png"
```

## Offline Mode

Use offline mode only after the model is already cached locally:

```powershell
$env:HF_HUB_OFFLINE = "1"
python .\scripts\main.py "C:\path\to\image.png"
```

If the model is not cached, offline mode will fail.

## Hardware Notes

- A CUDA GPU is strongly recommended.
- CPU inference may work but can be very slow.
- The script caps image processing at `max_pixels=401408` to reduce memory use.
- The 2B model still needs several GB of disk and memory once dependencies and model weights are installed.

## Common Failures

`Missing dependency`

Install dependencies with `python -m pip install -r requirements.txt`.

`Model inference failed` with download or authentication errors

Make sure network access to Hugging Face works, or provide a local model directory with `--model`.

`torch.cuda.is_available: False`

The script can still run, but it may be slow. Install the correct CUDA PyTorch build if GPU inference is required.
