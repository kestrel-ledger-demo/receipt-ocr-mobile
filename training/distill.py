import torch.nn.functional as F


def distill_loss(student_logits, teacher_logits, labels, t=4.0, alpha=0.7):
    """Student (25 MB) learns from the 120 MB teacher's soft outputs (trial: 92% overall, 84% faded)."""
    soft = F.kl_div(F.log_softmax(student_logits / t, -1), F.softmax(teacher_logits / t, -1), reduction="batchmean") * t * t
    return alpha * soft + (1 - alpha) * F.cross_entropy(student_logits, labels)
