import matplotlib.pyplot as plt

def plot_moves(move_stats):
    moves = list(move_stats.keys())
    counts = list(move_stats.values())

    plt.figure()
    plt.bar(moves, counts)
    plt.title("Player Move Frequency")
    plt.xlabel("Move")
    plt.ylabel("Count")
    plt.show()

def plot_results(result_stats):
    results = list(result_stats.keys())
    counts = list(result_stats.values())

    plt.figure()
    plt.bar(results, counts)
    plt.title("Game Results")
    plt.xlabel("Result")
    plt.ylabel("Count")
    plt.show()
