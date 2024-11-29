import random
import numba
from numba import cuda
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

w = 24
h = 24

@cuda.jit
def game_of_life(current, next):
    j, k = cuda.grid(2)
    if j < w and k < h:
        live_neighbors = 0
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if (x, y) != (0, 0):
                    ni, nj = j + x, k + y
                    if 0 <= ni < w and 0 <= nj < h:
                        live_neighbors += current[ni, nj]
        if current[j, k] == 1:
            next[j, k] = 1 if live_neighbors in (2, 3) else 0
        else:
            next[j, k] = 1 if live_neighbors == 3 else 0

def run_game(it):
    bits = [0, 1]
    cells = [[random.choice(bits) for _ in range(w)] for _ in range(h)]

    d_current = cuda.to_device(cells)
    d_next = cuda.device_array((w, h), dtype=np.int32)

    threadsperblock = (24, 24)
    blockspergrid_x = (w + (threadsperblock[0] - 1)) // threadsperblock[0]
    blockspergrid_y = (h + (threadsperblock[1] - 1)) // threadsperblock[1]
    blockspergrid = (blockspergrid_x, blockspergrid_y)

    fig, ax = plt.subplots()
    img = ax.imshow(cells, cmap='binary', interpolation='nearest')

    def update(frame):
        nonlocal d_current, d_next
        game_of_life[blockspergrid, threadsperblock](d_current, d_next)
        d_current, d_next = d_next, d_current
        current_state = d_current.copy_to_host()

        img.set_data(current_state)
        if sum(sum(row) for row in current_state) == 0:
            print("All cells died at iteration:", frame + 1)
            ani.event_source.stop()
        return [img]

    ani = animation.FuncAnimation(fig, update, frames=it, interval=200, blit=True)
    plt.show()

run_game(10000)
