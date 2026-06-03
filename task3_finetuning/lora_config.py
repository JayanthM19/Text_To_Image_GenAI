lora_config = {
    "rank": 4,
    "alpha": 16,
    "target_modules": [
        "to_q",
        "to_k",
        "to_v"
    ]
}

print("LoRA configuration initialized.")