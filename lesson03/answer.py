def sum_func(lines: list[str]) -> str:
    len = int(lines.readline())
    if len <= 0 or len == None:
        return "EMPTY"
    sum = 0
    for i in range(len):
        curr = int(lines.readline())
        if curr == -999:
            break
        if curr >= 0:
            sum += curr
    return sum
        

if __name__ == "__main__":
    filename = input()
    with open(filename) as data_file:
        lines = data_file.readlines()
    sum_func(lines)
