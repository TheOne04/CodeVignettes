import random


def main():
    width = int(input("Width: "))
    height = int(input("Height: "))

    for i in range(height):
        print(get_row(width))


def get_row(n):
    row = ""
    for i in range(n):
        fish = random.choice([True, False])
        if fish:
            row += "  " + spawn_fish() + "  "
        else:
            row += "  ...  "
    return row


def spawn_fish():
    n = random.choice([0, 1])
    return "<><" if n == 1 else "><>"


if __name__ == "__main__":
    main()
