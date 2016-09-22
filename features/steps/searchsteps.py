from behave import *
from hamcrest import *
from features.support import searchapi

use_step_matcher("parse")


@step('the user searches for "{term}"')
def search_for_term(context, term):
    searchapi.search(context, term)


@step('the user should see a list of search results')
def user_sees_results(context):
    assert_that(searchapi.result_count(context), equal_to(1), 'results')


@step('the user selects a result containing the title "{title}"')
def select_result(context, title):
    """
    :type context: behave.runner.Context
    :type title: str
    """
    searchapi.select_search_result_for_term(context=context, term=title)


@then('the result for "{company_name}" indicates the company is archived')
def result_shows_archived(context, company_name):
    """
    :type context: behave.runner.Context
    :type company_name: str
    """
    assert_that(searchapi.company_result_is_archived(context, company_name), equal_to(True))


@then('the result for "{company_name}" does not indicate the company is archived')
def result_does_not_show_archived(context, company_name):
    """
    :type context: behave.runner.Context
    :type company_name: str
    """
    assert_that(searchapi.company_result_is_archived(context, company_name), equal_to(False))


use_step_matcher("re")


@step(u'the (?P<position>.*)(?:st|nd|rd|th) result should contain the word "(?P<term>.*)" in it\'s title')
def user_test_result_title(context, position, term):
    title = searchapi.get_result_title_for_index(context=context, position=position)
    assert_that(title.text.lower(), contains_string(term.lower()))
