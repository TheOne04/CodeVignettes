import random


def main():
    for i in range(7):
        print(word_gen(), end=" ")
    print(word_gen(), end="")
    print("?")


def word_gen():
    v = "aeiou"
    c = "bcdfghjklmnpqrstvwxyz"
    word = ""
    patterns = ["cvc", "cvcv", "vc", "vccvc"]

    for i in pattern(patterns):
        if i == "c":
            word += random.choice(c)
        elif i == "v":
            word += random.choice(v)

    return word


def pattern(p):
    return random.choice(p)


if __name__ == "__main__":
    main()
