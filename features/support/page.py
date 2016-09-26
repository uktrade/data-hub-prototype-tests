def get_element_for_xpath(context, xpath):
    script = '''
        var element = document.evaluate(
            "%s",
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null)
            .singleNodeValue;

        if (element) {
            element.scrollIntoView(true);
        }
        return element;''' % xpath

    return context.browser.execute_script(script)


def get_element_for_text(context, text):
    xpath = "//*[contains(text(), '%s')]" % text
    return get_element_for_xpath(context=context, xpath=xpath)


def get_element_for_name(context, input_name):
    xpath = "//*[@name='%s']" % input_name
    return get_element_for_xpath(context=context, xpath=xpath)


def get_element_for_css(context, css):
    script = '''
        var element = document.querySelector(\"%s\");
        if (element) {
            element.scrollIntoView(true);
        }
        return element;
    ''' % css

    return context.browser.execute_script(script)


def get_elements_for_css(context, css):
    script = '''
        var elements = document.querySelectorAll(\"%s\");
        if (elements && elements.length > 0) {
            elements[0].scrollIntoView(true);
        }
        return elements;
    ''' % css

    return context.browser.execute_script(script)


def pick_option_in_select(context, input_name, value):
    xpath = "//*[@name='%s']" % input_name
    script = '''
            var element = document.evaluate(
                "%s",
                document,
                null,
                XPathResult.FIRST_ORDERED_NODE_TYPE,
                null)
                .singleNodeValue;

            if (element) {
                element.scrollIntoView(true);
                element.value="%s"
            }''' % (xpath, value)

    context.browser.execute_script(script)


def select_tab(context, tab_title):
    tabs = get_elements_for_css(context=context, css='.tabs-list a')
    for tab in tabs:
        if tab.text == tab_title:
            tab.click()
            return


def shows_is_archived(context):
    archived_badge = get_element_for_css(context=context, css='.status-badge--archived')
    return archived_badge is not None


def get_error_summary(context):
    return get_element_for_css(context=context, css='.error-summary')


# having to use this due to a bug in selenium fixed in beta 4 onwards
def get_classes_for_text(context, text):
    xpath = "//*[contains(text(), '%s')]" % text
    script = '''
        var element = document.evaluate(
            "%s",
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null)
            .singleNodeValue;

        if (element) {
            element.scrollIntoView(true);
            return element.className
        }
        return null;''' % xpath

    return context.browser.execute_script(script)


def get_href_for_text(context, text):
    xpath = "//*[contains(text(), '%s')]" % text
    script = '''
        var element = document.evaluate(
            "%s",
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null)
            .singleNodeValue;

        if (element) {
            element.scrollIntoView(true);
            return element.getAttribute('href')
        }
        return null;''' % xpath

    return context.browser.execute_script(script)
