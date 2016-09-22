from behave import *


@step('the user presses the "{button_title}" button')
def press_button(context, button_title):
    """
    :type context: behave.runner.Context
    """
    pass


@step('the "{badge_title}" badge is displayed')
def badge_is_displayed(context, badge_title):
    """
    :type context: behave.runner.Context
    """
    pass


@step('"{phrase}" is displayed')
def phrase_is_displayed(context, phrase):
    """
    :type context: behave.runner.Context
    """
    pass
