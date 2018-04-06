from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class VReceiveContributions(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    

    def after_all_players_arrive(self):
        pass


class VShowResults(Page):
    pass


page_sequence = [
    VReceiveContributions,
    ResultsWaitPage,
    VShowResults
]
