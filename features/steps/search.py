from behave import *
from hamcrest import *

use_step_matcher("parse")


@step('the user searches for "{term}"')
def search_for_term(context, term):
    context.browser.get('http://localhost:3000/search?term=%s' % term)


@step('the user should see a list of search results')
def user_sees_results(context):
    results = get_search_results(context=context)
    assert_that(len(results), equal_to(1), 'results')


@step('the user selects a result containing the title "{title}"')
def select_result(context, title):
    """
    :type context: behave.runner.Context
    """
    results = get_search_results(context=context)

    # Look in the results for the first result that contains the title
    for result in results:
        result_title = get_result_title(result)
        if title.lower() in result_title.lower():
            # Find the result title link and select it
            title.find_element_by_css('a').click()
            return


use_step_matcher("re")


@step(u'the (?P<position>.*)(?:st|nd|rd|th) result should contain the word "(?P<term>.*)" in it\'s title')
def user_test_result_title(context, position, term):
    result = get_search_result(context=context, index=position)
    title = get_result_title(result)
    assert_that(title.text.lower(), contains_string(term.lower()))


def get_search_results(context):
    return context.browser.find_elements_by_css_selector('.results-list__result')


def get_search_result(context, index):
    results = get_search_results(context=context)
    position = int(index) - 1
    return results[position]


def get_result_title(result):
    return result.find_element_by_css_selector('.result-title')
