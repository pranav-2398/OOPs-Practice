class ScoreField:

    def __set_name__(self, owner, name):
        self.name = name

    def __init__(self, lower_bound, upper_bound):
        if type(lower_bound) and type(upper_bound) == int:
            self.lower_bound = lower_bound
            self.upper_bound = upper_bound

        else:
            raise Exception("Value provided should be integers")

    def __get__(self, instance, owner):
        return instance.__dict__.get(f"{self.name}")

    def __set__(self, instance, value):
        if type(value) == int and self.lower_bound <= value <= self.upper_bound:
            instance.__dict__[f"{self.name}"] = value

        else:
            raise ValueError(f"The value being set should be an integer and must lie "
                             f"in the correct range of {self.lower_bound} and "
                             f"{self.upper_bound}")


class StudentProfile:
    GREScore = ScoreField(130, 340)
    GMATScore = ScoreField(400, 1600)

    def __init__(self, gre_score=GREScore.lower_bound, gmat_score=GMATScore.lower_bound):
        self.GREScore = gre_score
        self.GMATScore = gmat_score

    def __repr__(self):
        return f"StudentProfile(GREScore={self.GREScore}, GMATScore={self.GMATScore})"


c1 = StudentProfile(200, 1200)
