# ## Etap 1
#
# - Zaimplementuj metodę `__lt__` albo `__gt__`, która umożliwi porównanie ze sobą dwóch zespołów po ilości punktów.
# - Zaimplementuj metodę `__repr__`, która zwróci nazwę zespołu.
#
# ## Etap 2
#
# - Zmodyfikuj metodę porównującą tak, aby w przypadku zespołów o tej samej liczbie punktów, brana była pod uwagę różnica bramek.
# - Zmodyfikuj metodę `__repr__` tak, aby przy nazwie zespołu były widoczne zdobyte punkty i różnica bramek.

## Rozszerzenie:
# - Wydrukuj ładną tabelę, w której:
#     - zespoły wypisane są jeden pod drugim
#     - wypisane jest miejsce, na którym znajduje się dany zespół

class Team:
    def __init__(self, name, points, gf, ga):
        self.name = name
        self.pts = points
        self.gf = gf  # goals for
        self.ga = ga  # goals against

    def calculate_GoalDiff(selfself):
        """

        :return:
        """
        return self.gf - self.ga
    def __lt__(self, other):
        """

        :param other:
        :return:
        """
        if (self.pts < other.pts):
            return True
        elif (self.pts == other.pts) and (self.gf-self.ga) < (other.gf-other.ga):
            return True
        return False

    # def __gt__(self, other):
    #     """
    #
    #     :param other:
    #     :return:
    #     """
    #     if ((self.gf-self.ga) > (other.gf-other.ga)):
    #         return True
    #     return False

    def __repr__(self):
        return f'Team {str(self.name)}, points {self.pts} and the diference of goals is {self.gf-self.ga}'

if __name__ == '__main__':
    # stan tabeli na 29.01.2020
    league_table = [
        Team('Tottenham Hotspur', points=34, gf=38, ga=32),
        Team('Manchester City', points=51, gf=65, ga=27),
        Team('Manchester United', points=34, gf=36, ga=29),
        Team('Chelsea', points=40, gf=41, ga=32),
        Team('Leicester', points=48, gf=52, ga=24),
        Team('Liverpool', points=70, gf=56, ga=15),
    ]

    league_table.sort()
    league_table.reverse()

    print(league_table)

    for place,name in enumerate(league_table, start=1):
        print(f'{place}. \t ')