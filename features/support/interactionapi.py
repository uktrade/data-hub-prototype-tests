from features.support import companyapi, contactapi, page, utils
import requests
from features.environment import API_ROOT, WEB_ROOT

interactions = []


def can_edit_interaction(context):
    class_names = page.get_classes_for_text(context=context, text='Edit interaction details')
    url = page.get_href_for_text(context=context, text='Edit interaction details')
    return 'button-disabled' not in class_names and url[0] != '#'


def can_add_interaction(context):
    class_names = page.get_classes_for_text(context=context, text='Add new interaction')
    url = page.get_href_for_text(context=context, text='Add new interaction')
    return 'button-disabled' not in class_names and url[0] != '#'


def post_interaction_data(interactions_table):
    interactions.clear()
    for line in interactions_table:
        post_data = utils.translate_line_to_dict(line)
        company = companyapi.get_company_for_name(post_data['company'])
        contact = contactapi.get_contact_for_name(post_data['contact'])
        post_data['company'] = company['id']
        post_data['contact'] = contact['id']
        interactions.append(requests.post('%s/interaction/' % API_ROOT, json=post_data).json())


def get_interaction_for_subject(subject):
    for interaction in interactions:
        if interaction['subject'] == subject:
            return interaction


def view_interaction(context, subject):
    contact = get_interaction_for_subject(subject)
    context.browser.get('%s/interaction/%s/view' % (WEB_ROOT, contact['id']))
