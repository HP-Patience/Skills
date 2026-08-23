"""Qwen2-VL image understanding CLI.

This script powers the image-understanding skill. It supports Chinese image
captioning and visual question answering with Qwen/Qwen2-VL-2B-Instruct.
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import sys
from pathlib import Path


DEFAULT_MODEL = "Qwen/Qwen2-VL-2B-Instruct"
ENV_MODEL = "IMAGE_UNDERSTANDING_MODEL"

_model = None
_processor = None


def dependency_status() -> list[tuple[str, bool]]:
    packages = [
        ("torch", "torch"),
        ("transformers", "transformers"),
        ("accelerate", "accelerate"),
        ("Pillow", "PIL"),
    ]
    return [(label, importlib.util.find_spec(module) is not None) for label, module in packages]


def print_env_check(model_name: str) -> int:
    print(f"Python: {sys.version.split()[0]}")
    print(f"Model: {model_name}")
    print(f"{ENV_MODEL}: {os.environ.get(ENV_MODEL, '') or '(not set)'}")
    print()

    missing = []
    for label, ok in dependency_status():
        print(f"{label}: {'ok' if ok else 'missing'}")
        if not ok:
            missing.append(label)

    if importlib.util.find_spec("torch") is not None:
        import torch

        print(f"torch.cuda.is_available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"cuda device: {torch.cuda.get_device_name(0)}")

    if missing:
        print()
        print("Missing dependencies. Install them with:")
        print("python -m pip install -r requirements.txt")
        return 1

    print()
    print("Environment check passed. The model will download on first use if it is not cached.")
    return 0


def load_runtime_deps():
    try:
        from PIL import Image
        from transformers import AutoProcessor, Qwen2VLForConditionalGeneration
    except ImportError as exc:
        print(f"ERROR: Missing dependency: {exc}", file=sys.stderr)
        print("Install dependencies with: python -m pip install -r requirements.txt", file=sys.stderr)
        sys.exit(2)

    return Image, AutoProcessor, Qwen2VLForConditionalGeneration


def get_model(model_name: str):
    global _model
    if _model is None:
        _, _, model_cls = load_runtime_deps()
        print(f"Loading model: {model_name}")
        _model = model_cls.from_pretrained(
            model_name,
            torch_dtype="auto",
            device_map="auto",
        )
        print("Model loaded successfully.\n")
    return _model


def get_processor(model_name: str):
    global _processor
    if _processor is None:
        _, processor_cls, _ = load_runtime_deps()
        _processor = processor_cls.from_pretrained(model_name)
    return _processor


def chat(image, prompt: str, model_name: str, max_tokens: int = 512) -> str:
    model = get_model(model_name)
    processor = get_processor(model_name)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {"type": "text", "text": prompt},
            ],
        }
    ]

    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = processor(text=[text], images=[image], return_tensors="pt", max_pixels=401408).to(model.device)

    generated_ids = model.generate(**inputs, max_new_tokens=max_tokens)
    generated_ids_trimmed = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    return processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True)[0].strip()


def caption(image_path: Path, model_name: str, length: str = "normal") -> str:
    Image, _, _ = load_runtime_deps()
    prompts = {
        "short": "用一句话简短描述这张图片。",
        "normal": "描述这张图片。",
        "long": "请详细描述这张图片的内容，包括主要元素、场景、颜色和氛围。",
    }
    image = Image.open(image_path).convert("RGB")
    return chat(image, prompts[length], model_name=model_name, max_tokens=512)


def query(image_path: Path, question: str, model_name: str) -> str:
    Image, _, _ = load_runtime_deps()
    image = Image.open(image_path).convert("RGB")
    return chat(image, question, model_name=model_name, max_tokens=512)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Qwen2-VL-2B image understanding tool")
    parser.add_argument("image", nargs="?", help="Image path")
    parser.add_argument("question", nargs="*", help="Optional question about the image")
    parser.add_argument(
        "--length",
        "-l",
        choices=["short", "normal", "long"],
        default="long",
        help="Caption length when no question is provided",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get(ENV_MODEL, DEFAULT_MODEL),
        help=f"Hugging Face model id or local model directory. Defaults to {DEFAULT_MODEL}.",
    )
    parser.add_argument(
        "--check-env",
        action="store_true",
        help="Check Python dependencies and CUDA availability without loading the model.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.check_env:
        return print_env_check(args.model)

    if not args.image:
        print("ERROR: image path is required", file=sys.stderr)
        return 1

    image_path = Path(args.image).expanduser()
    if not image_path.exists():
        print(f"ERROR: Image does not exist: {image_path}", file=sys.stderr)
        return 1

    try:
        if args.question:
            question = " ".join(args.question)
            print(query(image_path, question, model_name=args.model))
        else:
            print(caption(image_path, model_name=args.model, length=args.length))
    except OSError as exc:
        print(f"ERROR: Could not read image: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"ERROR: Model inference failed: {exc}", file=sys.stderr)
        print("See references/model-install.md for setup and troubleshooting.", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
