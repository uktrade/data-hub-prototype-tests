from selenium import webdriver
import os


def before_all(context):
    context.browser = webdriver.Firefox()


def after_all(context):
    context.browser.quit()


def before_scenario(context, scenario):
    os.system('./reset-django.sh')