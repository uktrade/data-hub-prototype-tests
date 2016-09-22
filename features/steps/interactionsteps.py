from behave import *
from hamcrest import *
from features.support import interactionapi


@step('the user cannot edit the interaction')
def cannot_edit_interaction(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(interactionapi.can_edit_interaction(context), equal_to(False))


@step('the user cannot add an interaction')
def cannot_edit_contact(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(interactionapi.can_add_interaction(context), equal_to(False))

@step('the user views the interaction "{interaction_subject}"')
def view_company(context, interaction_subject):
    interactionapi.view_interaction(context=context, subject=interaction_subject)
