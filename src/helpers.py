import random

from src.models import Group, Pool, Team


def generate_pools(main_spots):
    teams = []
    pools = []
    for i in range(len(main_spots)):
        pool = Pool(i + 1)
        for region, count in main_spots[i + 1].items():
            for _ in range(count):
                n = 1
                while True:
                    if region + str(n) in [t.name for t in teams]:
                        n = n + 1
                        continue
                    team = Team(region + str(n), region)
                    teams.append(team)
                    pool.add_team(team)
                    break
        pools.append(pool)
    return pools


def draw_groups(pools):
    groups = []
    for letter in ["A", "B", "C", "D"]:
        groups.append(Group("Group " + letter))
    for pool in pools:
        while len(pool.teams) > 0:
            team = random.choice(pool.teams)
            for group in groups:
                try:
                    group.add_team(team)
                    break
                except ValueError:
                    continue
            else:
                # raise ValueError(f"Impossible setup: {[str(g) for g in groups]}")
                raise ValueError(groups)
            pool.teams.remove(team)
    return groups


def create_random_group(pool_list):
    group = []
    for pool in pool_list:
        teams = pool.teams
        while True:
            team = random.choice(teams)
            if team.region in [t.region for t in group]:
                continue
            group.append(team)
            teams.remove(team)
            break
    return group


def groups_match(a, b):
    for group in a:
        if group not in b:
            return False
    return True
