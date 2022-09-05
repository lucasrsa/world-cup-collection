from src.helpers import draw_groups, generate_pools, groups_match

main_spots = {
    1: {
        "LPL": 1,
        "LCK": 1,
        "LEC": 1,
        "LCS": 1,
    },
    2: {
        "LPL": 1,
        "LCK": 1,
        "LEC": 1,
        "PCS": 1,
    },
    3: {
        "LPL": 1,
        "LCK": 1,
        "LCS": 1,
        "VCS": 1,
    },
    # 4: {
    #     "LPL": 1,
    #     "LCK": 1,
    #     "LCS": 1,
    #     "VCS": 1,
    # },
}


def __main__():
    success = []
    failure = []
    full_length = 0
    while full_length < 125:
        pools = generate_pools(main_spots)
        try:
            groups = draw_groups(pools)
            if not any([groups_match(groups, g) for g in success]):
                success.append(groups)
            # else:
            #     print("Already in success")
        except ValueError as e:
            groups = e.args[0]
            if not any([groups_match(groups, g) for g in failure]):
                failure.append(groups)
            # else:
            #     print("Already in failure")

        if full_length != len(success) + len(failure) and (len(success) + len(failure)) % 5 == 0:
            full_length = len(success) + len(failure)
            print(len(success), len(failure), full_length)
            print([groups[0].teams for groups in success])
            # print([groups[0].teams for groups in failure])

    # pools2 = generate_pools(main_spots)
    # groups2 = draw_groups(pools2)
    # print([str(g) for g in groups2])


if __name__ == "__main__":
    __main__()
