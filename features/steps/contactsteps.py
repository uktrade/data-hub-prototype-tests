from behave import *
from hamcrest import *
from features.support import contactapi


@step('the user cannot edit the contact')
def cannot_edit_contact(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(contactapi.can_edit_contact(context), equal_to(False))


@step('the user cannot add a contact')
def cannot_edit_contact(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(contactapi.can_add_contact(context), equal_to(False))


@step('the user views the contact "{contact_name}"')
def view_company(context, contact_name):
    contactapi.view_contact(context=context, contact_name=contact_name)
