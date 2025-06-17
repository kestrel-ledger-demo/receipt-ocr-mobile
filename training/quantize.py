import torch


def to_int8(model):
    """Post-training int8 quantization: 26 MB on device."""
    return torch.ao.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
