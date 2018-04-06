from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
This is a three player game where each player is initially endowed with 100 points. Each player individually makes a decision about how many of their points they want to contribute to the group. The combined contributions are multiplied by 2, and then divided evenly three ways and redistributed back to the players.
"""


class Constants(BaseConstants):
    name_in_url = 'contribute'
    players_per_group = 3
    num_rounds = 1

    endowment = c(100)
    multiplier = 2



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

    def calculate_pay_offs(self):
        players = self.get_players()
        contributions = [p.contribution for p in players]
        self.total_contribution = sum(contributions)
        self.individual_share = self.total_contribution  * Constants.multiplier /  Constants.players_per_group
        for p in players:
            p.payoff = Constants.endowment - p.contribution + self.individual_share

class Player(BasePlayer):
    contribution = models.CurrencyField(min=0, max=Constants.endowment)
