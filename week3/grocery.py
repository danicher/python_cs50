def main():
    groceries = []

    while True:
        try:
            grocery = input("")
            groceries.append(grocery)
        except EOFError:
            print("")
            break

    groceries_counts = {}

    for item in groceries:
        if item not in groceries_counts:
            item_count = groceries.count(item)
            groceries_counts[item] = item_count

    for item in sorted(groceries_counts):
        print(groceries_counts[item], item.upper())

main()