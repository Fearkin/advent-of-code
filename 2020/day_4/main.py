import re


def main():
    with open("input.txt", "r") as file:
        count = 0
        result_file = file.read().replace("\n", " ").split("  ")
        for line in result_file:
            if all([
                re.search(r"byr:(19[2-9][0-9]|200[0-2])\b", line),
                re.search(r"iyr:(201[0-9]|20[0-2]0\b)", line),
                re.search(r"eyr:(202[0-9]|2030)\b", line),
                re.search(r"hgt:59in|hgt:6[0-9]in|hgt:7[0-6]in|hgt:1[5-8][0-9]cm|hgt:19[0-3]cm\b", line),
                re.search(r"hcl:#([0-9]|[a-f]){6}\b", line),
                re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b", line),
                re.search(r"pid:([0-9]){9}\b", line),
            ]):
                count += 1
        print(count)


if __name__ == '__main__':
    main()
