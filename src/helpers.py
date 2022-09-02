import json

valid = {}
with open("files/meta.json", "r") as f:
    for v in json.loads(f.read()).values():
        for t in v["tags"]:
            valid[t] = v["size"]


def random_card():
    import random
    tag = random.choice(list(valid.keys()))
    value = random.randint(1, valid[tag])
    return tag + str(value)


def validate_card(tag, value):
    return tag in valid and 0 < value <= valid[tag]


def digest_card(card):
    # CC cards will always have len==3
    split_index = 3 if len(card) > 3 else 2
    tag = card[:split_index]
    value = int(card[split_index:])
    if not validate_card(tag, value):
        raise ValueError("Card not found")
    return tag, value
