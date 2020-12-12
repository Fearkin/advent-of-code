def count_trees(file, *slopes):
    with open(file) as f:
        file = f.read().splitlines()
    total = 1
    for slope in slopes:
        count = 0
        x, y = 0, 0
        while y < (len(file) - 1):
            x += slope[0]
            y += slope[1]
            if x > (len(file[y])-1):
                x -= len(file[y])
            if file[y][x] == "#":
                count += 1
        total *= count
    print(total)


def main():
    count_trees("input.txt", (1, 1), (3, 1), (5, 1), (7, 1), (1, 2))


if __name__ == "__main__":
    main()

