# SixFinger-8B Adapter for LLaMA 3.1 8B

A powerful LoRA adapter designed to enhance response generation for Turkish/English mixed datasets, built on top of the optimized `unsloth/llama-3.1-8b-bnb-4bit` base model.

## Overview

- **Base Model**: unsloth/llama-3.1-8b-bnb-4bit
- **Adapter Type**: LoRA (Low-Rank Adaptation)
- **Quantization**: 4-bit (via bitsandbytes)
- **Purpose**: Enhanced response generation for Turkish/English mixed datasets
- **Compatibility**: Hugging Face Transformers + PEFT library
- **License**: Apache 2.0

## Installation

Install the required dependencies:

```bash
pip install transformers accelerate bitsandbytes peft
```

**Note**: Ensure you have a GPU with sufficient VRAM for 4-bit inference.

## Loading the Model

### Step 1: Load the Base Model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

base_model = AutoModelForCausalLM.from_pretrained(
    "unsloth/llama-3.1-8b-bnb-4bit",
    device_map="auto"
)
```

### Step 2: Load the Adapter

```python
from peft import PeftModel

model = PeftModel.from_pretrained(
    base_model,
    "sixfingerdev/SixFinger-8B"
)
```

### Step 3: Load the Tokenizer

```python
tokenizer = AutoTokenizer.from_pretrained("unsloth/llama-3.1-8b-bnb-4bit")
```

## Example Usage

Generate text using the adapter:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import torch

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(
    "unsloth/llama-3.1-8b-bnb-4bit",
    device_map="auto"
)

# Load LoRA adapter
model = PeftModel.from_pretrained(
    base_model,
    "sixfingerdev/SixFinger-8B"
)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("unsloth/llama-3.1-8b-bnb-4bit")

# Example text generation (Turkish)
prompt = "Soru: Yapay zeka nedir?\nCevap:"
inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=50,
        do_sample=True,
        temperature=0.7
    )

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Important Notes

- The adapter does **not** modify the base model; it only applies LoRA weights on top
- 4-bit quantization significantly reduces VRAM usage
- Ensure your GPU supports bitsandbytes 4-bit operations
- You can merge the adapter into the base model for easier deployment if needed

## Training Dataset

This model was trained using the [turkish-qa-multi-dialog-dataset](https://huggingface.co/datasets/sixfingerdev/turkish-qa-multi-dialog-dataset), enabling it to provide contextual and accurate responses for Turkish language tasks.

## References

- [PEFT (Parameter-Efficient Fine-Tuning)](https://huggingface.co/docs/peft/index)
- [Transformers 4-bit Quantization](https://huggingface.co/docs/transformers/main/en/main_classes/quantization)
- [LLaMA 3.1 Model Card](https://huggingface.co/meta-llama/Llama-3.1-8B)

## License

This adapter is provided under the Apache 2.0 License. Ensure compliance with the base model license (Meta's LLaMA).

## Community

For questions, discussions, and feedback, visit the [model discussions page](https://huggingface.co/sixfingerdev/SixFinger-8B/discussions).

---

Made with ❤️ by [sixfingerdev](https://huggingface.co/sixfingerdev)
