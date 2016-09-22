from selenium import webdriver
import os

API_ROOT = os.getenv('API_ROOT', 'http://localhost:8000')
WEB_ROOT = os.getenv('WEB_ROOT', 'http://localhost:3000')


def before_all(context):
    context.browser = webdriver.Firefox()


def after_all(context):
    context.browser.quit()


def before_scenario(context, scenario):
    os.system('./reset-django.sh')