import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "plots"

def ensure_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def plot_moves(move_stats):
    ensure_dir()
    moves = list(move_stats.keys())
    counts = list(move_stats.values())

    plt.figure()
    plt.bar(moves, counts)
    plt.title("Player Move Frequency")
    plt.xlabel("Move")
    plt.ylabel("Count")
    plt.savefig(f"{OUTPUT_DIR}/move_frequency.png")
    plt.close()

def plot_results(result_stats):
    ensure_dir()
    results = list(result_stats.keys())
    counts = list(result_stats.values())

    plt.figure()
    plt.bar(results, counts)
    plt.title("Game Results")
    plt.xlabel("Result")
    plt.ylabel("Count")
    plt.savefig(f"{OUTPUT_DIR}/game_results.png")
    plt.close()
