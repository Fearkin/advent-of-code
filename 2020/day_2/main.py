def main():
    with open("input.txt", "r") as f:
        file = f.readlines()
        result = 0
        for line in file:
            min_num = int(line[:line.index("-")])
            max_num = int(line[line.index("-")+1:line.index(" ")])
            char = line[line.index(":")-1]
            string = line.split(" ")[2]
            if (string[min_num-1] == char and string[max_num-1] != char)\
                    or (string[min_num-1] != char and string[max_num-1] == char):
                result += 1
        print(result)


if __name__ == '__main__':
    main()
