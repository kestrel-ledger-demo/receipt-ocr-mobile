import numpy as np


def age(img, weeks, rng=np.random.default_rng(0)):
    """Simulated heat-and-light fading (trial: faded thermal only 84% to 86%)."""
    fade = np.clip(1.0 - 0.06 * weeks + rng.normal(0, 0.02, img.shape), 0.3, 1.0)
    return np.clip(255 - (255 - img) * fade, 0, 255).astype(np.uint8)
