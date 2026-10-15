import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math_transforms import (translation_matrix_2d, rotation_matrix_2d, scaling_matrix_2d)

LIM = 8.0
RADIUS = 2.0
K_END = 1.25
SCALE_FRAMES = 30
LOOP = 90
PATH_R = 2.5


def build_pentagon():
    a = np.linspace(0, 2 * np.pi, 5, endpoint=False)
    return np.vstack((RADIUS * np.cos(a), RADIUS * np.sin(a), np.ones(5)))


VERTICES = build_pentagon()


def transform_at(frame):
    if frame < SCALE_FRAMES:
        k = 1 + (K_END - 1) * frame / SCALE_FRAMES
        return scaling_matrix_2d(k, k)
    S = scaling_matrix_2d(K_END, K_END)
    theta = 4.0 * ((frame - SCALE_FRAMES) % LOOP)
    rad = np.radians(theta)
    T = translation_matrix_2d(PATH_R * (1 - np.cos(rad)), PATH_R * np.sin(rad))
    R = rotation_matrix_2d(theta)
    return T @ R @ S


def verify_2d():
    assert VERTICES.shape == (3, 5) and np.all(VERTICES[2] == 1)
    for ang in (0, 37, 90, 211):
        assert abs(np.linalg.det(rotation_matrix_2d(ang)) - 1) < 1e-12
    for f in range(SCALE_FRAMES + 2 * LOOP):
        pts = transform_at(f) @ VERTICES
        assert np.all(np.abs(pts[:2]) <= LIM), f"Вихід за межі вікна, кадр {f}"
    assert np.allclose(transform_at(SCALE_FRAMES), transform_at(SCALE_FRAMES + LOOP))
    print("[Верифікація 2D] OK: межі вікна, det(R)=1, цикл замкнений.")


def draw_2d(ax, frame):
    ax.clear()
    pts = transform_at(frame) @ VERTICES
    cx = np.append(pts[0], pts[0, 0])
    cy = np.append(pts[1], pts[1, 0])
    ax.fill(cx, cy, color='orange', alpha=0.4, label='Пентагон')
    ax.plot(cx, cy, color='red', linewidth=2)
    ax.set_xlim(-LIM, LIM)
    ax.set_ylim(-LIM, LIM)
    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(0, color='black', lw=0.5)
    ax.grid(True)
    ax.set_aspect('equal')
    stage = "масштабування" if frame < SCALE_FRAMES else "переміщення + обертання"
    ax.set_title(f"Варіант 20, рівень I (2D): {stage}")
    ax.legend(loc='upper right')


def run_2d_variant_20():
    verify_2d()
    fig, ax = plt.subplots(figsize=(7, 7))
    ani = FuncAnimation(fig, lambda f: draw_2d(ax, f), frames=itertools.count(),
                        interval=50, cache_frame_data=False)
    plt.show()


if __name__ == "__main__":
    run_2d_variant_20()