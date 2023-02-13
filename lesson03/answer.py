def sum_func(lines: list[str]) -> str:
    len = int(lines[0])
    if (len <= 0) or (len == None):
        return "EMPTY"
    sum = 0
    num_positive = 0
    for i in range(1, len+1):
        curr = int(lines[i])
        if curr == -999:
            break
        if curr >= 0:
            sum += curr
            num_positive += 1
    if num_positive > 0:
        return sum
    return "EMPTY"

if __name__ == "__main__":
    filename = input()
    with open(filename) as data_file:
        lines = data_file.readlines()
    print(lines[0])
    print(sum_func(lines))
