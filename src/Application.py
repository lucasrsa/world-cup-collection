from argparse import ArgumentParser
from models import Album
from helpers import random_card


verbose = False


def process(func, file):
    success = []
    failure = []
    with open(file, "r") as f:
        for line in f.readlines():
            try:
                func(line)
                success.append(line)
            except ValueError:
                failure.append(line)
    # print("Success: ", success)
    # print("Failure: ", failure)


def add(album, file):
    # print("Adding...")
    process(album.acquire, file)


def remove(album, file):
    # print("Removing...")
    process(album.remove, file)


def joking():
    import random
    album = Album("dev-null")
    funcs = [add, remove]
    filename = "files/fake.txt"

    for _ in range(100):
        with open(filename, "w") as f:
            for _ in range(random.randint(1, 100)):
                f.write(random_card()+"\n")
        random.choice(funcs)(album, filename)

    album.summarize()


def __main__():
    parser = ArgumentParser(description="Process some integers.")
    parser.add_argument("--add", dest="add_file", metavar="FILE", type=str,
                        help="an integer for the accumulator")
    # parser.add_argument("--sum", dest="accumulate", action="store_const",
    #                     const=sum, default=max,
    #                     help="sum the integers (default: find the max)")

    args = parser.parse_args()
    print(args.add_file)
    album = Album()
    add(album, "files/add.txt")
    remove(album, "files/remove.txt")
    album.show()
    album.summarize()
    album.save()


if __name__ == "__main__":
    # __main__()
    joking()
