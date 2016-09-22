from behave import *
from hamcrest import *
from features.support import page


@step('"{phrase}" is displayed')
def phrase_found(context, phrase):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.browser.find_element_by_tag_name('body').text.lower(), contains_string(phrase.lower()))


@step('The user should see an error')
def see_error(context):
    """
    :type context: behave.runner.Context
    """
    errors = page.get_element_for_css(context=context, css='.error')
    assert_that(errors, is_not(None))


@step('the user selects the "{tab_title}" tab')
def select_tab(context, tab_title):
    page.select_tab(context=context, tab_title=tab_title)


@step("the user does not see an error summary")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(page.get_error_summary(context=context), none())