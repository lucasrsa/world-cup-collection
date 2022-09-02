import json
from os.path import exists
from helpers import digest_card


class Album:
    __missing = {}
    __acquired = {}
    __doubled = {}

    def summarize(self):
        print("Missing: ", sum([len(x) for x in self.__missing.values()]))
        print("Acquired: ", sum([len(x) for x in self.__acquired.values()]))
        print("Doubled: ", sum([len(x) for x in self.__doubled.values()]))

    def acquire(self, card):
        tag, value = digest_card(card)
        if value in self.__missing[tag]:
            self.__missing[tag].remove(value)
            self.__acquired[tag].append(value)
        else:
            self.__doubled[tag].append(value)

    def remove(self, card):
        tag, value = digest_card(card)
        if value in self.__doubled[tag]:
            self.__doubled[tag].remove(value)
        else:
            raise ValueError("Attempted to remove card not doubled")

    def save(self, file="files/now.json"):
        with open(file, "w") as f:
            f.write(json.dumps({"missing": self.__missing, "acquired": self.__acquired, "doubled": self.__doubled, }))

    def load(self, file="files/now.json"):
        with open(file, "r") as f:
            d = json.loads(f.read())
            self.__missing = d["missing"]
            self.__acquired = d["acquired"]
            self.__doubled = d["doubled"]

    def show(self):
        print(self.__missing)
        print(self.__acquired)
        print(self.__doubled)

    def __init__(self, file="files/now.json"):
        if exists(file):
            self.load(file)
        else:
            with open("files/meta.json", "r") as f:
                for v in json.loads(f.read()).values():
                    for tag in v["tags"]:
                        self.__missing[tag] = []
                        self.__acquired[tag] = []
                        self.__doubled[tag] = []
                        for i in range(v["size"]):
                            self.__missing[tag].append(i + 1)
