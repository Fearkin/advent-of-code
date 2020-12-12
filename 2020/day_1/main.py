from itertools import permutations


def get_numbers(target_sum, target_file, permutations_number):
    with open(target_file, "r") as f:
        file = list(map(int, f.readlines()))
        for val in permutations(file, permutations_number):
            if sum(val) == target_sum:
                return val


def main():
    target_sum = 2020
    target_file = "input.txt"
    permutations_number = 3
    res = get_numbers(target_sum, target_file, permutations_number)
    print(*res)


if __name__ == '__main__':
    main()

