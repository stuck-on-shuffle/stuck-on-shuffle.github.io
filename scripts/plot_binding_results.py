"""Plot SABER MCQ and existing benchmark accuracies from draft Tables 2 and 3."""
from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/shuffle-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Label, CLIP ViT-B/32, Qwen3-VL-Embedding-8B, Ours-8B.
SABER = [
    ("Text → Text", 53.6, 53.7, 99.3),
    ("Text → Image", 23.0, 34.9, 69.0),
    ("Image → Text", 22.3, 36.3, 74.1),
    ("Image → Image", 75.5, 84.9, 94.3),
]
EXISTING = [
    ("SugarCrepe++ · T→T", 32.7, 70.9, 93.7),
    ("ColorSwap · T→I", 17.9, 45.9, 79.8),
    ("BiVLC · T→I", 19.1, 21.6, 32.0),
    ("NCD · I→T", 71.1, 80.6, 95.4),
    ("VG-Attribution · I→T", 62.5, 78.0, 80.4),
    ("ColorSwap · I→T", 38.2, 71.4, 88.4),
    ("SugarCrepe · I→T", 64.0, 85.7, 90.8),
    ("SugarCrepe++ · I→T", 44.9, 65.8, 82.7),
    ("BiVLC · I→T", 47.1, 73.7, 74.8),
    ("CLEVR · I→T", 50.3, 60.6, 86.2),
    ("PUG:SPAR · I→T", 47.5, 48.9, 67.7),
    ("PUG:SPARE · I→T", 50.4, 52.8, 69.1),
]
MODELS = [
    ("CLIP ViT-B/32", "#b394c7"),
    ("Qwen3-VL-Embedding-8B", "#a6b4c8"),
    ("Ours-8B", "#2563eb"),
]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                     "svg.fonttype": "path", "axes.labelcolor": "#243247",
                     "text.color": "#243247", "xtick.color": "#576579",
                     "ytick.color": "#243247"})
fig, ax = plt.subplots(figsize=(20, 6.8))
rows = SABER + EXISTING
x = np.arange(len(rows), dtype=float)
x[4:] += .6
for i, (label, color) in enumerate(MODELS):
    bars = ax.bar(x + (i - 1) * .25, [r[i + 1] for r in rows],
                  width=.23, color=color, label=label, zorder=3)
    ax.bar_label(bars, fmt="%.1f", padding=4, fontsize=10, rotation=90)
ax.set_xticks(x, [r[0].split(" · ")[0] for r in rows], rotation=50,
              ha="center", va="top", fontsize=12)
# Group the existing benchmarks by modality beneath the dataset labels.
for first, last, label in [
    (4, 4, "Text → Text"),
    (5, 6, "Text → Image"),
    (7, 15, "Image → Text"),
]:
    left, right = x[first] - .42, x[last] + .42
    ax.plot([left, left, right, right], [-.38, -.40, -.40, -.38],
            transform=ax.get_xaxis_transform(), clip_on=False,
            color="#a6b4c8", linewidth=1.2)
    ax.text((left + right) / 2, -.435, label,
            transform=ax.get_xaxis_transform(), ha="center", va="top",
            fontsize=12, color="#576579")
ax.set_ylim(0, 122)
ax.set_yticks(range(0, 101, 20))
ax.set_ylabel("Accuracy (%)", labelpad=12)
ax.set_xlim(-.65, x[-1] + .65)
ax.yaxis.grid(True, color="#e2e8f0", zorder=0)
ax.axvline(3.8, color="#cbd5e1", linewidth=1.5, linestyle="--")
ax.text(1.5, 119, "SABER-MCQ", ha="center", fontsize=17, fontweight="bold")
ax.text(10.1, 119, "Existing attribute-binding benchmarks", ha="center",
        fontsize=17, fontweight="bold")
ax.tick_params(axis="both", length=0, pad=10)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.legend(loc="lower center", bbox_to_anchor=(.5, 1.06), ncol=3,
          frameon=False, fontsize=14)
fig.subplots_adjust(left=.055, right=.995, bottom=.34, top=.83)
destination = Path(__file__).resolve().parents[1] / "static" / "images"
fig.savefig(destination / "binding-results.svg", bbox_inches="tight")
fig.savefig(destination / "binding-results.png", dpi=240, bbox_inches="tight")
plt.close(fig)
