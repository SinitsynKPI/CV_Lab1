import itertools
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from level1_2d import draw_2d, verify_2d
from level2_3d import draw_3d, verify_3d


def run_full_variant_20():
    verify_2d()
    verify_3d()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    def update(frame):
        draw_2d(ax1, frame)
        draw_3d(ax2, frame)

    ani = FuncAnimation(fig, update, frames=itertools.count(),
                        interval=50, cache_frame_data=False)
    plt.show()


if __name__ == "__main__":
    run_full_variant_20()