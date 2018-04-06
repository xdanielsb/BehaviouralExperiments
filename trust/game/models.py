from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
To start, Player 1 receives 10 points; Player 2 receives nothing. Player 1 can send some or all of his points to Player 2. Before P2 receives these points they will be tripled. Once P2 receives the tripled points he can decide to send some or all of his points to P1.
"""


class Constants(BaseConstants):
    name_in_url = 'game'
    players_per_group = 2
    num_rounds = 1
    endowment = c(10)
    multiplication_factor = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            #you could shufflet the people here to arrive to different groups
            pass
        else: 
            #do other stuff
            pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        choices = currency_range(0, Constants.endowment, c(1))
    )
    sent_back_amount = models.CurrencyField()

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount


class Player(BasePlayer):
    pass
