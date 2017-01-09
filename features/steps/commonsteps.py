import time
from behave import *
from hamcrest import *
from features.support import page
from features.support.page import get_element_for_text
from features.support.utils import set_form_field, check_value_for_heading


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
def dont_see_error_summary(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(page.get_error_summary(context=context), none())


@step('the user enters values into the form')
def enter_into_form(context):
    """
    :type context: behave.runner.Context
    """
    form_data = context.table
    set_form_field(context=context, field_name=form_data.headings[0], field_value=form_data.headings[1])

    for line in form_data:
        field_name = line.cells[0]
        field_value = line.cells[1]
        set_form_field(context=context, field_name=field_name, field_value=field_value)


@step('the user clicks save')
def click_save(context):
    """
    :type context: behave.runner.Context
    """
    button = get_element_for_text(context=context, text='Save')
    button.click()
    time.sleep(3)



@step('the screen should show the following data')
def data_shown(context):
    """
    :type context: behave.runner.Context
    """

    value_data = context.table
    check_value_for_heading(context=context, field_name=value_data.headings[0], field_value=value_data.headings[1])

    for line in value_data:
        field_name = line.cells[0]
        field_value = line.cells[1]
        set_form_field(context=context, field_name=field_name, field_value=field_value)
        check_value_for_heading(context=context, field_name=field_name, field_value=field_value)
