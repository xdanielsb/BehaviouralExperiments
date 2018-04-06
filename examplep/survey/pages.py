from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class VSurvey(Page):
  form_model = "player"
  form_fields = ["name", "age"]

class VResultsSurvey(Page):
  pass

page_sequence = [ 
  VSurvey,
  VResultsSurvey
]