import requests
import time
from features.support import utils, page
from features.environment import API_ROOT, WEB_ROOT

companies = []


def view_ch_record(context, company_number):
    context.browser.get('%s/company/ch/%s' % (WEB_ROOT, company_number))
    time.sleep(1)


def can_archive_company(context):
    archive_button = get_archive_company_button(context)
    return archive_button is not None


def archive_with_reason(context, reason):
    archive_button = get_archive_company_button(context)
    archive_button.click()
    page.pick_option_in_select(context=context, input_name='archive_reason', value=reason)
    page.get_element_for_text(context=context, text='Archive now').click()
    time.sleep(1)


def archive_without_reason(context):
    get_archive_company_button(context).click()
    page.get_element_for_text(context=context, text='Archive now').click()
    time.sleep(1)





def unarchive_company(context):
    get_unarchive_company_button(context).click()
    time.sleep(1)


def get_archive_company_button(context):
    return page.get_element_for_text(context=context, text='Archive company')


def get_unarchive_company_button(context):
    return page.get_element_for_text(context=context, text='Unarchive now')


def can_edit_company(context):
    class_names = page.get_classes_for_text(context=context, text='Edit company')
    url = page.get_href_for_text(context=context, text='Edit company')

    return 'button-disabled' not in class_names and url[0] != '#'


def view_company(context, company_name):
    company = get_company_for_name(company_name)
    context.browser.get('%s/company/dit/%s' % (WEB_ROOT, company['id']))


def post_company_data(companies_table):
    companies.clear()
    for line in companies_table:
        post_data = utils.translate_line_to_dict(line)
        companies.append(requests.post('%s/company/' % API_ROOT, json=post_data).json())


def get_company_for_name(company_name):
    for company in companies:
        if company['registered_name'] == company_name:
            return company
