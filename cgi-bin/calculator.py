import sys


def main(a, b):
    return a + b


if __name__ == "__main__":
    c = main(int(sys.argv[1]), int(sys.argv[2]))
    print(c)
