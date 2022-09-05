class Pool:
    def add_team(self, team):
        if team.region in self.regions:
            raise ValueError(f"{self.__repr__()} already have a team representing the {team.region} region.")
        team.pool = self.number
        self.teams.append(team)
        self.regions.append(team.region)

    def __repr__(self):
        return f"Pool {str(self.number)}"

    def __str__(self):
        return f"{self.__repr__()}: {str(self.teams)}"

    def __init__(self, n):
        self.teams = []
        self.regions = []
        self.number = n


class Group:
    __max_size = 4

    def add_team(self, team):
        if not len(self.teams) < self.__max_size:
            raise ValueError(f"{self.__repr__()} is already full!")
        if team.pool in self.pools:
            raise ValueError(f"{self.__repr__()} already have a team from Pool {team.pool}.")
        if team.region in self.regions:
            raise ValueError(f"{self.__repr__()} already have a team representing the {team.region} region.")
        self.teams.append(team)
        self.pools.append(team.pool)
        self.regions.append(team.region)

    def __eq__(self, obj):
        return isinstance(obj, Group) and all([team in self.teams for team in obj.teams])

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"{self.name}: {str(self.teams)}"

    def __init__(self, name):
        self.teams = []
        self.regions = []
        self.pools = []
        self.name = name


class Team:
    def __eq__(self, obj):
        return isinstance(obj, Team) and obj.name == self.name and obj.region == self.region

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __init__(self, name, region):
        self.pool = 0
        self.name = name
        self.region = region
