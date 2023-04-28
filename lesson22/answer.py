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

if __name__ == "__main__":
    filename = input()
    with open(filename, "r") as f:
        lines = f.readlines()
    numItems = int(lines.pop(0).strip())
    maximumCapacity = int(lines.pop(0).strip())
    items = get_list_of_items(lines)