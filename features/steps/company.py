from behave import *
from hamcrest import *
import requests

@given("a company exists with")
def post_company(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("companies house entries exists with")
def post_companies_house(context):
    """
    :type context: behave.runner.Context
    """
    for line in context.table:
        ch_dict = dict(zip(line.headings, line.cells))
        requests.post('http://localhost:8000/ch/', json=ch_dict)


@step("the user selects 'The company has shut down' as a reason to archive")
def select_archive_reason(context):
    """
    :type context: behave.runner.Context
    """
