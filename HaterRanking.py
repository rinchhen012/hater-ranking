import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams["font.family"] = "monospace"

mu, sigma = 50, 15
x = np.linspace(-10, 160, 1000)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

fig, ax = plt.subplots(figsize=(16, 6), facecolor="#1a1a2e")
ax.set_facecolor("#1a1a2e")

ax.plot(x, y, color="white", linewidth=2.5, zorder=2)
ax.fill_between(x, y, alpha=0.15, color="white")

rng = np.random.default_rng(42)
n_players = 4000
raw_scores = rng.normal(mu, sigma, n_players * 3)
raw_scores = raw_scores[(raw_scores >= 0) & (raw_scores <= 155)][:n_players]

heights = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((raw_scores - mu) / sigma) ** 2)
y_positions = rng.uniform(0, 1, len(raw_scores)) * heights

cc = "#555577"
ax.scatter(raw_scores, y_positions, s=10, color=cc, alpha=0.6,
           zorder=1, clip_on=False, linewidth=0)

label_players = [
    ("Average",    35, "white",  0.018),
    ("Good",       45, "white",  0.027),
    ("Elite",      58, "white",  0.025),
    ("World Class",70, "white",  0.013),
    ("Utsav",      83, "white",  0.019),
    ("Bibek",      104, "white",  0.010),
    ("Rinchhen",  107, "white",  0.019),
    ("Chidori",   113, "white",  0.010),
    ("Satyam",    140, "#ff4444",  0.010),
]

for name, score, color, label_y in label_players:
    yy = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((score - mu) / sigma) ** 2)
    ax.scatter(score, yy, s=180, color=color, edgecolors="#1a1a2e",
               linewidth=2.5, zorder=5, clip_on=False)

    is_far = name in ("Satyam", "Bibek", "Chidori", "Rinchhen", "Utsav", "Good", "Elite")
    if is_far:
        ax.plot([score, score], [yy, label_y],
                color=color, lw=1.5, ls="--", alpha=0.4, zorder=1)

    fontsize = 15 if name == "Satyam" else 11
    ax.text(score, label_y, name, ha="center", va="bottom",
            fontsize=fontsize, fontweight="bold", color=color)

ax.axvline(mu, color="white", lw=1.2, ls="--", alpha=0.3, zorder=1)

sd_labels = {
    -3: "−3σ", -2: "−2σ", -1: "−1σ",
     0: "μ",
    +1: "1σ",  +2: "2σ",  +3: "3σ",  +4: "4σ",  +5: "5σ",  +6: "6σ",
}
ax.set_xticks([mu + k * sigma for k in sd_labels])
ax.set_xticklabels([sd_labels[k] for k in sorted(sd_labels)], fontsize=10, color="white")

ax.set_xlabel("Standard Deviations from the Mean", fontsize=12, labelpad=10, color="white")
ax.set_ylabel("Density", fontsize=12, labelpad=10, color="white")
ax.set_title("Hater Bell Curve\nGroupchat Analysis — Who's the Biggest Hater?",
             fontsize=18, fontweight="bold", pad=15, color="white", linespacing=1.5)

ax.text(1.0, 1.05, "Data: Bball Saturday-Insta", transform=ax.transAxes,
        ha="right", va="top", fontsize=15, color="#aaaacc", fontstyle="italic",
        fontweight="bold")

ax.set_xlim(-5, 155)
ax.set_ylim(-0.0005, 0.028)
ax.set_yticks([])
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#444466")
ax.tick_params(axis="x", colors="white", length=0)
ax.tick_params(axis="y", length=0)

ax.grid(axis="x", color="#333355", linestyle="--", linewidth=0.5, alpha=0.5)

plt.tight_layout()
plt.savefig("haterRanking.png", dpi=300, bbox_inches="tight")
print("Saved haterRanking.png")
