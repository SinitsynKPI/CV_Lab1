import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math_transforms import rotation_y_3d, isometric_projection

LIM = 6.0
PERIOD = 90
SCALE = 2.0
COLORS = ['red', 'purple', 'blue', 'green', 'magenta', 'darkorange']

VERTICES = np.vstack((
    SCALE * np.array([[1, 1, -1, -1],
                      [1, -1, 1, -1],
                      [1, -1, -1, 1]]) / np.sqrt(3),
    np.ones(4)))
EDGES = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 1)]
P = isometric_projection()


def transform_at(frame):
    return P @ rotation_y_3d(360.0 * (frame % PERIOD) / PERIOD)


def alpha_at(frame):
    return 0.05 + 0.95 * (0.5 - 0.5 * np.cos(2 * np.pi * frame / PERIOD))


def color_at(frame):
    return COLORS[(frame // PERIOD) % len(COLORS)]


def verify_3d():
    d = [np.linalg.norm(VERTICES[:3, a] - VERTICES[:3, b]) for a, b in EDGES]
    assert np.allclose(d, d[0]), "Піраміда неправильна: ребра різної довжини"
    assert np.allclose(VERTICES[:3].mean(axis=1), 0), "Центроїд не в початку координат"
    assert abs(np.linalg.det(rotation_y_3d(33)) - 1) < 1e-12
    for f in range(2 * PERIOD):
        pts = transform_at(f) @ VERTICES
        assert np.allclose(pts[2], 0)
        assert np.all(np.abs(pts[:2]) <= LIM), f"Вихід за межі вікна, кадр {f}"
        assert 0 <= alpha_at(f) <= 1
    assert np.allclose(transform_at(0), transform_at(PERIOD))
    print("[Верифікація 3D] OK: правильний тетраедр, межі вікна, цикл замкнений.")


def draw_3d(ax, frame):
    ax.clear()
    pts = transform_at(frame) @ VERTICES
    color, alpha = color_at(frame), alpha_at(frame)
    for a, b in EDGES:
        ax.plot([pts[0, a], pts[0, b]], [pts[1, a], pts[1, b]],
                color=color, linewidth=2.5, alpha=alpha)
    ax.set_xlim(-LIM, LIM)
    ax.set_ylim(-LIM, LIM)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_title(f"Варіант 20, рівень II (3D піраміда), колір: {color}", fontsize=11)


def run_3d_variant_20():
    verify_3d()
    fig, ax = plt.subplots(figsize=(7, 7))
    ani = FuncAnimation(fig, lambda f: draw_3d(ax, f), frames=itertools.count(),
                        interval=50, cache_frame_data=False)
    plt.show()


if __name__ == "__main__":
    run_3d_variant_20()