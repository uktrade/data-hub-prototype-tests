from features.support import page, utils, companyapi
from features.environment import API_ROOT, WEB_ROOT
import requests

contacts = []


def can_edit_contact(context):
    class_names = page.get_classes_for_text(context=context, text='Edit contact details')
    url = page.get_href_for_text(context=context, text='Add contact')
    return 'button-disabled' not in class_names and url[0] != '#'


def can_add_contact(context):
    class_names = page.get_classes_for_text(context=context, text='Add new contact')
    url = page.get_href_for_text(context=context, text='Add new contact')
    return 'button-disabled' not in class_names and url[0] != '#'


def post_contact_data(contacts_table):
    contacts.clear()
    for line in contacts_table:
        post_data = utils.translate_line_to_dict(line)
        company = companyapi.get_company_for_name(post_data['company'])
        post_data['company'] = company['id']
        contacts.append(requests.post('%s/contact/' % API_ROOT, json=post_data).json())


def get_contact_for_name(contact_name):
    for contact in contacts:
        this_contact_name = '%s %s' % (contact['first_name'], contact['last_name'])
        if this_contact_name == contact_name:
            return contact


def view_contact(context, contact_name):
    contact = get_contact_for_name(contact_name)
    context.browser.get('%s/contact/%s/view' % (WEB_ROOT, contact['id']))
