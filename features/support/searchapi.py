import time

from features.environment import WEB_ROOT
from features.support import page


def get_search_results(context):
    return context.browser.browser.find_elements_by_css_selector('.results-list__result')


def get_search_result(context, index):
    results = get_search_results(context=context)
    position = int(index) - 1
    return results[position]


def get_result_title(result):
    return result.find_element_by_css_selector('.result-title')


def get_result_title_for_index(context, position):
    result = get_search_result(context=context, index=position)
    return get_result_title(result)


def search(context, term):
    context.browser.get('%s/search?term=%s' % (WEB_ROOT, term))
    time.sleep(1)


def result_count(context):
    results = get_search_results(context=context)
    return len(results)


def select_search_result_for_term(context, term):
    results = get_search_results(context=context)

    # Look in the results for the first result that contains the title
    for result in results:
        result_title = get_result_title(result)
        if term.lower() in result_title.text.lower():
            # Find the result title link and select it
            result_title.find_element_by_css_selector('a').click()
            time.sleep(1)
            return


def company_result_is_archived(context, company_name):
    # get the result and then search that for the badge

    script = "var element = document.querySelector(\"[data_registered_name='%s'] .status-badge--archived\");" % company_name
    script += "if (element) element.scrollIntoView(true); return element;"

    element = context.browser.execute_script(script)

    if element is not None:
        return True

    return False
