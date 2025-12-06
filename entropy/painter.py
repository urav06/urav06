import hashlib
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
from matplotlib.colors import LinearSegmentedColormap

from entropy.types import Transmutation

# --- Configuration ---
IMG_DPI     : int               = 300
IMG_SIZE    : tuple[int, int]   = (10, 10)
NUM_STEPS   : int               = 80000
DT          : float             = 0.005
CHUNK_SIZE  : int               = 500

# --- Lorenz Base Parameters ---
SIGMA_BASE      : float = 10.0
BETA_BASE       : float = 8.0 / 3.0
RHO_BASE        : float = 20.0
RHO_CHAOS_SCALE : float = 28.0


def paint(transmutation: Transmutation, output_path: Path) -> None:
    """ Render a Lorenz attractor visualization to output_path. """

    r           = _hash_to_floats(transmutation.source.commit_hash, 8)
    chaos       = transmutation.chaos_score / 100.0
    initial     = np.array([0.1 + (r[0] - 0.5), r[1] - 0.5, r[2] - 0.5], dtype=np.float64)
    sigma       = SIGMA_BASE + (r[3] - 0.5) * 2.0
    beta        = BETA_BASE + (r[4] - 0.5) * 0.5
    rho         = RHO_BASE + (chaos * RHO_CHAOS_SCALE) + (r[5] - 0.5) * 4.0
    view        = (10.0 + r[6] * 30.0, r[7] * 360.0)
    trajectory  = _integrate(initial, sigma, rho, beta)

    _render(trajectory, transmutation.mood_color, view, output_path)


def _hash_to_floats(commit_hash: str, count: int) -> list[float]:
    digest = hashlib.sha256(commit_hash.encode()).digest()
    return [int.from_bytes(digest[i * 2 : i * 2 + 2], "big") / 65535.0 for i in range(count)]


def _lorenz(p: npt.NDArray[np.float64], sigma: float, rho: float, beta: float,) -> npt.NDArray[np.float64]:
    x, y, z = p[0], p[1], p[2]
    return np.array([sigma * (y - x), x * (rho - z) - y, x * y - beta * z,],dtype=np.float64,)


def _integrate(
    initial : npt.NDArray[np.float64],
    sigma   : float,
    rho     : float,
    beta    : float,
) -> npt.NDArray[np.float64]:

    state       = initial.copy()
    trajectory  = np.zeros((NUM_STEPS, 3), dtype=np.float64)

    for i in range(NUM_STEPS):
        trajectory[i] = state
        k1 = _lorenz(state, sigma, rho, beta)
        k2 = _lorenz(state + k1 * DT / 2, sigma, rho, beta)
        k3 = _lorenz(state + k2 * DT / 2, sigma, rho, beta)
        k4 = _lorenz(state + k3 * DT, sigma, rho, beta)
        state = state + (DT / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    return trajectory


def _render(
    pts         : npt.NDArray[np.float64],
    hex_color   : str,
    view        : tuple[float, float],
    output_path : Path,
) -> None:

    fig = plt.figure(figsize=IMG_SIZE, dpi=IMG_DPI)
    ax  = fig.add_subplot(111, projection="3d")

    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    ax.grid(visible=False)
    ax.axis("off")
    ax.view_init(elev=view[0], azim=view[1])
    ax.set_box_aspect((1, 1, 1))

    margin = 0.02
    for dim in range(3):
        lo, hi = float(pts[:, dim].min()), float(pts[:, dim].max())
        pad = (hi - lo) * margin
        getattr(ax, ["set_xlim", "set_ylim", "set_zlim"][dim])(lo - pad, hi + pad)

    cmap    = LinearSegmentedColormap.from_list("mood", ["black", hex_color, "white"])
    colors  = cmap(np.linspace(0, 1, NUM_STEPS))

    for i in range(0, NUM_STEPS - 1, CHUNK_SIZE):
        end = min(i + CHUNK_SIZE, NUM_STEPS)
        seg = pts[i:end]
        ax.plot(
            seg[:, 0],
            seg[:, 1],
            seg[:, 2],
            color=colors[(i + end) // 2],
            lw=0.5,
            alpha=0.85,
        )

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(output_path, bbox_inches="tight", pad_inches=0, facecolor="black")
    plt.close(fig)
