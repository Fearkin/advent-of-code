from functools import reduce


def main():
    with open("input.txt", "r") as file:
        part1_count = 0
        part2_count = 0
        questions = file.read().split("\n\n")
        part1_questions = [q.replace("\n", "") for q in questions]
        for group in part1_questions:
            part1_count += len(set(group))
        for group in questions:
            passengers = group.split("\n")
            passengers = [set(passenger) for passenger in passengers]
            part2_count += len(reduce(lambda a, b: a & b, passengers))

        print(f"Part 1: {part1_count}| Part 2: {part2_count}")


if __name__ == '__main__':
    main()
