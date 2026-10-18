"""Render the three embedding models from Table 5 in the results chart style."""
from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/shuffle-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Affirmation, Negation, Hybrid, All; model order matches MODELS below.
RESULTS = {
    "COCO": [
        [78.3, 6.8, 36.3, 41.4],
        [82.7, 6.6, 58.1, 50.3],
        [83.4, 6.8, 58.5, 50.7],
    ],
    "VOC2007": [
        [89.9, 4.7, 58.0, 39.8],
        [91.5, 6.4, 78.2, 49.7],
        [91.8, 6.1, 79.6, 50.3],
    ],
}
MODELS = [
    ("Qwen3-VL-Embedding-8B", "#a6b4c8"),
    ("Ours-8B (negation-filtered)", "#78b5e3"),
    ("Ours-8B", "#2563eb"),
]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                     "svg.fonttype": "path", "axes.labelcolor": "#243247",
                     "text.color": "#243247", "xtick.color": "#576579",
                     "ytick.color": "#243247"})
fig, ax = plt.subplots(figsize=(20, 6.8))
x = np.arange(8, dtype=float)
x[4:] += .6
for i, (label, color) in enumerate(MODELS):
    values = RESULTS["COCO"][i] + RESULTS["VOC2007"][i]
    bars = ax.bar(x + (i - 1) * .25, values, width=.23,
                  color=color, label=label, zorder=3)
    ax.bar_label(bars, fmt="%.1f", padding=4, fontsize=10, rotation=90)
ax.set_xticks(x, ["Affirmation", "Negation", "Hybrid", "All"] * 2,
              rotation=50, ha="center", va="top", fontsize=12)
ax.set_ylim(0, 122)
ax.set_yticks(range(0, 101, 20))
ax.set_ylabel("Accuracy (%)", labelpad=12)
ax.set_xlim(-.65, x[-1] + .65)
ax.yaxis.grid(True, color="#e2e8f0", zorder=0)
ax.axvline(3.8, color="#cbd5e1", linewidth=1.5, linestyle="--")
ax.text(1.5, 119, "Negbench-COCO", ha="center", fontsize=17, fontweight="bold")
ax.text(6.1, 119, "Negbench-VOC", ha="center", fontsize=17, fontweight="bold")
ax.tick_params(axis="both", length=0, pad=10)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.legend(loc="lower center", bbox_to_anchor=(.5, 1.06), ncol=3,
          frameon=False, fontsize=14)
fig.subplots_adjust(left=.055, right=.995, bottom=.34, top=.83)
destination = Path(__file__).resolve().parents[1] / "static" / "images"
fig.savefig(destination / "negation-results.svg", bbox_inches="tight", transparent=True)
fig.savefig(destination / "negation-results.png", dpi=240, bbox_inches="tight", transparent=True)
plt.close(fig)
