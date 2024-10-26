import sys
import numpy as np
import matplotlib.pyplot as plt


def analytical_dice_rolls(dices: int = 2, sides: int = 6) -> tuple[np.ndarray, np.ndarray]:
    single = np.ones(sides) / sides

    distribution = single
    for _ in range(dices - 1):
        distribution = np.convolve(distribution, single)

    unique = np.arange(dices, dices * sides + 1)
    return unique, distribution


def estimate_dice_rolls(
        rng: np.random.Generator,
        dices: int = 2,
        sides: int = 6,
        rolls: int = 1000,
) -> tuple[np.ndarray, np.ndarray]:
    emulated = rng.integers(low=1, high=sides+1, size=(rolls, dices))
    totals = emulated.sum(axis=1)
    unique, counts = np.unique(totals, return_counts=True)
    distribution = counts/rolls
    return unique, distribution


def safe(fun, check=None, default=None):
    try:
        val = fun()
        if check is None or check(val):
            return val
        return val if check is None or check(val) else default
    except:
        return default


def safe_input(argv_index: int, prompt: str, check=None, default=None, type_conversion=int):
    val = safe(lambda: int(sys.argv[argv_index]), check=check)
    if val is None:
        val = safe(
            lambda: type_conversion(input(prompt + (f' (default = {default})' if default else '') + ': ')),
            check=check,
            default=default
        )
    return val


def display(title: str, unique: np.ndarray, analytical: np.ndarray, unique_est: np.ndarray, estimated: np.ndarray):
    plt.figure(figsize=(10, 6))
    plt.bar(unique - 0.2, analytical, width=0.4, color='blue', alpha=0.6, label='Analytical')
    plt.bar(unique_est + 0.2, estimated, width=0.4, color='orange', alpha=0.6, label='Estimated')
    plt.xlabel('Dice Rolls')
    plt.ylabel('Probability')
    plt.title(title)
    plt.legend()
    plt.xticks(unique)
    plt.tight_layout()
    plt.show()


def main():
    dices = safe_input(1, "Number of dices", default=2)
    sides = safe_input(2, "Number of sides", default=6)
    rolls = safe_input(3, "Number of rolls", default=1000)

    unique, analytical = analytical_dice_rolls(
        dices=dices,
        sides=sides,
    )

    unique_est, estimated = estimate_dice_rolls(
        rng=np.random.default_rng(seed=42),
        dices=dices,
        sides=sides,
        rolls=rolls
    )

    display(
        title=f'Analytical vs Estimated ({rolls} rolls) Probability Distribution for {dices} Dices with {sides} Sides',
        unique=unique,
        analytical=analytical,
        unique_est=unique_est,
        estimated=estimated,
    )


if __name__ == "__main__":
    main()
