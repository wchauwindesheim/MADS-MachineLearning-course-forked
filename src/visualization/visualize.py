from typing import Dict, Tuple
from tqdm import tqdm
from pathlib import Path
import matplotlib.pyplot as plt

import seaborn as sns
import numpy as np
from loguru import logger


def plot_timers(timer: Dict[str, float]) -> None:
    x = list(timer.keys())
    y = list(timer.values())
    sns.barplot(x=x, y=y)

def plot_grid(img: np.ndarray, filepath: Path, k: int=3, figsize: Tuple = (10,10)) -> None:
    fig, axs = plt.subplots(k, k, figsize=figsize)
    axs = axs.ravel()
    for i in tqdm(range(k*k)):
        axs[i].imshow(img[i], cmap='gray')
        axs[i].axis("off")
    fig.savefig(filepath)
    logger.success(f"saved grid to {filepath}")
