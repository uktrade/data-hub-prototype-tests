from behave import *
from hamcrest import *
import requests
import time
from features.environment import API_ROOT, WEB_ROOT
from features.support import companyapi, contactapi, interactionapi, page


@given("companies exists with")
def post_company(context):
    """
    :type context: behave.runner.Context
    """
    companyapi.post_company_data(context.table)


@given("contacts exist with")
def post_contacts(context):
    contactapi.post_contact_data(context.table)


@given("interactions exist with")
def post_interactions(context):
    interactionapi.post_interaction_data(context.table)


@given("companies house entries exists with")
def post_companies_house(context):
    """
    :type context: behave.runner.Context
    """
    for line in context.table:
        ch_dict = dict(zip(line.headings, line.cells))
        requests.post('%s/ch/' % API_ROOT, json=ch_dict)


@step("the user selects '{reason}' as a reason to archive and archives the company")
@step("the user archives the company")
def select_archive_reason(context, reason = None):
    """
    :type context: behave.runner.Context
    :type reason: str
    """
    if not reason or len(reason.strip()) == 0:
        companyapi.archive_without_reason(context)
    else:
        companyapi.archive_with_reason(context, reason)


@step("the user can archive the company")
def can_archive(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(companyapi.can_archive_company(context=context), equal_to(True))


@step("the user cannot archive the company")
def can_archive(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(companyapi.can_archive_company(context=context), equal_to(False))


@step("the company detail screen indicates the company is archived")
def company_detail_is_archived(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(page.shows_is_archived(context=context), equal_to(True))


@step("the user unarchives the company")
def company_unarchive(context):
    """
    :type context: behave.runner.Context
    """
    companyapi.unarchive_company(context=context)


@step("the company detail screen does not indicate the company is archived")
def company_detail_is_not_archived(context):
    """
    :type context: behave.runner.Context
    """
    shows_archived = page.shows_is_archived(context=context)
    assert_that(shows_archived, equal_to(False))


@step('the user views a companies house record with company number "{company_number}"')
def show_ch(context, company_number):
    """
    :type context: behave.runner.Context
    :type company_number: str
    """
    companyapi.view_ch_record(context, company_number)


@step('the user cannot edit the company')
def cannot_edit_company(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(companyapi.can_edit_company(context), equal_to(False))


@step('the user views company "{company_name}"')
def view_company(context, company_name):
    companyapi.view_company(context=context, company_name=company_name)


@step('The user is on the add company page')
def goto_add_company(context):
    context.browser.get('%s/company/add' % WEB_ROOT)
    time.sleep(1)


@step('The user should see the company details screen')
def is_on_company_detail(context):
    should_have = '/company/COMBINED'
    url = context.browser.current_url
    assert_that(url.lower(), contains_string(should_have.lower()))

