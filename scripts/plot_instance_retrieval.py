"""Render every result from Table 6. Requires matplotlib; no website build step."""
from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/shuffle-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Dataset, modality pairing, Qwen3-VL-Embedding-8B, Ours-8B.
RESULTS = [
    ("ILIAS", "I→I", 58.5, 68.4),
    ("INSTRE S→S", "I→I", 92.8, 94.9),
    ("INSTRE M→S", "I→I", 81.3, 86.7),
    ("INSTRE M→S+M", "I→I", 75.6, 79.0),
    ("PODS", "I→I", 85.7, 88.1),
    ("Paris6K", "I→I", 86.8, 88.9),
    ("Oxford5K", "I→I", 61.3, 64.3),
    ("Sculptures6K", "I→I", 50.8, 59.6),
    ("ILIAS", "T→I", 52.3, 60.8),
]

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                     "svg.fonttype": "path", "axes.labelcolor": "#243247",
                     "text.color": "#243247", "xtick.color": "#576579",
                     "ytick.color": "#243247"})
fig, ax = plt.subplots(figsize=(20, 6.8))
x = np.arange(len(RESULTS), dtype=float)
for offset, column, color, label in [
    (-.18, 2, "#a6b4c8", "Qwen3-VL-Embedding-8B"),
    (.18, 3, "#2563eb", "Ours-8B"),
]:
    bars = ax.bar(x + offset, [r[column] for r in RESULTS], width=.32,
                   color=color, label=label, zorder=3)
    ax.bar_label(bars, fmt="%.1f", padding=4, fontsize=10, rotation=90)
ax.set_xticks(x, [r[0] for r in RESULTS], rotation=50,
              ha="center", va="top", fontsize=12)
for first, last, label in [(0, 7, "Image → Image"), (8, 8, "Text → Image")]:
    left, right = x[first] - .42, x[last] + .42
    ax.plot([left, left, right, right], [-.38, -.40, -.40, -.38],
            transform=ax.get_xaxis_transform(), clip_on=False,
            color="#a6b4c8", linewidth=1.2)
    ax.text((left + right) / 2, -.435, label,
            transform=ax.get_xaxis_transform(), ha="center", va="top",
            fontsize=12, color="#576579")
ax.set_ylim(0, 105)
ax.set_yticks(range(0, 101, 20))
ax.set_ylabel("mAP (%)", labelpad=12)
ax.set_xlim(-.65, x[-1] + .65)
ax.yaxis.grid(True, color="#e2e8f0", zorder=0)
ax.tick_params(axis="both", length=0, pad=10)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.legend(loc="lower center", bbox_to_anchor=(.5, 1.06), ncol=2,
          frameon=False, fontsize=14)
fig.subplots_adjust(left=.055, right=.995, bottom=.34, top=.83)
destination = Path(__file__).resolve().parents[1] / "static" / "images"
fig.savefig(destination / "instance-retrieval-results.svg", bbox_inches="tight")
fig.savefig(destination / "instance-retrieval-results.png", dpi=240, bbox_inches="tight")
plt.close(fig)
