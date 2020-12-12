def read_seats(inpath="input.txt"):
    with open(inpath, 'r') as infile:
        return infile.read().splitlines()

# Binary representation trick
def get_seat_location(seat):
    row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(seat[7:].replace("L", "0").replace("R", "1"), 2)
    return row, col


def get_seat_id(seat):
    row, col = get_seat_location(seat)
    return row * 8 + col


def part1(seats):
    max_value = 0
    for seat in seats:
        seat_id = get_seat_id(seat)
        if seat_id > max_value:
            max_value = seat_id
    return max_value


def part2(seats):
    unseen = list(range(part1(seats) + 1))
    for seat in seats:
        unseen.remove(get_seat_id(seat))
    return unseen[-1]


def main():
    seats = read_seats()
    print(f"Part 1: {part1(seats)}\nPart 2: {part2(seats)}")


if __name__ == '__main__':
    main()
