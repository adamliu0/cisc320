def get_list_of_items(lines: list[str]) -> list[dict]:
    items = []
    for line in lines:
        line = line.strip().split()
        items.append({
            "name": line[0].strip(),
            "weight": int(line[1]),
            "value": int(line[2])
        })
    return items

def table(items, capacity):
    numItems = len(items)
    table = [[0 for j in range(capacity + 1)] for i in range(numItems + 1)]
    for i in range(1, numItems + 1):
        for j in range(1, capacity + 1):
            if items[i-1]["weight"] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], table[i-1][j-items[i-1]["weight"]] + items[i-1]["value"])
    return table

def get_items(table):
    numItems = len(items)
    j = maximumCapacity
    i = numItems
    items_eaten = []
    while i > 0 and j > 0:
        if table[i][j] != table[i-1][j]:
            items_eaten.append(items[i-1])
            j -= items[i-1]["weight"]
        i -= 1
    return list(reversed(items_eaten))


def print_table(table):
    for j in range(len(table[0])):
        for i in range(len(table)):
            print(table[i][j], end="\t")
        print()

if __name__ == "__main__":
    filename = input()
    #filename = "exampleinput.txt"
    with open(filename, "r") as f:
        lines = f.readlines()
    numItems = int(lines.pop(0).strip())
    maximumCapacity = int(lines.pop(0).strip())
    items = get_list_of_items(lines)
    table = table(items, maximumCapacity)
    #print_table(table)
    optimal_items = get_items(table)
    #print("Optimal items:")
    for item in optimal_items:
        print(item["name"])
    #print("Total weight:", sum([item["weight"] for item in optimal_items]))
    #print("Total value:", sum([item["value"] for item in optimal_items]))
    print(sum([item["value"] for item in optimal_items]))