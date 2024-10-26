import heapq
import sys


def greedy_algorithm(budget: int, items: dict[str, dict[str, int]]) -> tuple[int, list[str]]:
    """
    :param budget: Budget to spend
    :param items: Dictionary with costs and calories of items
    :return: Selected items
    """

    ranked = [{**props, "name": item, "rank": props["calories"]/props["cost"]} for item, props in items.items()]
    ranked.sort(key=lambda p: p["rank"], reverse=True)

    calories = 0
    result = []
    for item in ranked:
        if budget >= item["cost"]:
            result.append(item["name"])
            budget -= item["cost"]
            calories += item["calories"]

    return calories, result


def dynamic_programming(total_budget: int, all_items: dict[str, dict[str, int]]) -> tuple[int, list[str]]:
    """
    :param total_budget: Budget to spend
    :param all_items: Dictionary with costs and calories of items
    :return: Amount of each item
    """

    items = [{**props, "name": item} for item, props in all_items.items()]
    memo = {}

    def step(index: int, budget: int) -> tuple[int, list[str]]:
        if index >= len(items) or budget == 0:
            return 0, []
        if (index, budget) in memo:
            return memo[(index, budget)]

        calories_without, selected_without = step(index + 1, budget)

        calories_with, selected_with = 0, []
        item = items[index]
        if budget >= item["cost"]:
            calories_with, selected_with = step(index + 1, budget - item["cost"])
            calories_with += item["calories"]
            selected_with = selected_with + [item["name"]]

        if calories_with > calories_without:
            result = calories_with, selected_with
        else:
            result = calories_without, selected_without
        memo[(index, budget)] = result
        return result

    return step(0, total_budget)


def safe(fun):
    try:
        return fun()
    except:
        return None


def main():
    # Enter budget: 150
    # Greedy: (1120, ['cola', 'potato', 'pepsi', 'hot-dog', 'hamburger'])
    # Min:    (1220, ['potato', 'cola', 'pepsi', 'hamburger', 'pizza'])
    #
    # 'cola', 'potato', 'pepsi', 'hamburger' are the same for both algos.
    # But Greedy took 'hot-dog' first, because it has higher calories/cost ratio and left no money for 'pizza'.
    # Dynamic when it left with budget only for one item ('pizza' or 'hot-dog') took 'pizza' as it gives more calories.

    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = safe(lambda: int(sys.argv[1]))
    while not budget:
        budget = safe(lambda: int(input('Enter budget: ')))

    print(f'Greedy: {greedy_algorithm(budget, items)}')
    print(f'Min:    {dynamic_programming(budget, items)}')


if __name__ == "__main__":
    main()
