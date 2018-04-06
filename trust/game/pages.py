from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class VSendMoney(Page):
    form_model = "group"
    form_fields = ["sent_amount"]

    def is_displayed(self):
        return self.player.id_in_group == 1

class VSendMoneyBack(Page):
    form_model = "group"
    form_fields= ["sent_back_amount"]

    def is_displayed(self):
        return self.player.id_in_group == 2
    
    def vars_for_template(self):
        aux = {
            "tripled_amount": self.group.sent_amount * Constants.multiplication_factor
        }
        return aux
    
    def sent_back_amount_choices(self):
        vrange = currency_range(c(0), self.group.sent_amount * Constants.multiplication_factor, c(1))
        return vrange


class VShowResults(Page):
    pass

class WaitForP1(WaitPage):
    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
        

page_sequence = [
    VSendMoney,
    WaitForP1,
    VSendMoneyBack,
    ResultsWaitPage,
    VShowResults
]
