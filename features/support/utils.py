from hamcrest import *

from features.support.page import get_element_for_css


def translate_line_to_dict(line):
    post_data = {}
    for pos in range(0, len(line.headings)):
        if len(line.cells[pos]) > 0:
            post_data[line.headings[pos]] = line.cells[pos]

    return post_data


def set_form_field(context, field_name, field_value):

    script = '''

        var fieldName = '%s';
        var fieldValue = '%s';

        function setSelectValue(selectElement, value) {
            var options = selectElement.querySelectorAll('option');
            for (var pos = 0; pos < options.length; pos += 1) {
                var option = options[pos];
                if (option.text.toLowerCase() === value.toLowerCase()) {
                    selectElement.value = option.value;
                    return;
                }
            }
        }

        var element = document.evaluate(
            "//*[@name='" + fieldName +"']",
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null)
            .singleNodeValue;

        if (element) {
            element.scrollIntoView(true);
            var isAuto = element.className.indexOf('autosuggest-source-js');
            if (element.tagName === 'SELECT') {
                console.log('select');
                setSelectValue(element, fieldValue);
                var evt = document.createEvent("HTMLEvents");
                evt.initEvent("change", false, true);
                element.dispatchEvent(evt);
            } else if (isAuto !== -1) {
                var id = element.id;
                console.log('id:' + id);
                var displayElement = document.querySelector('#' + id + '-x');
                displayElement.value = fieldValue;

                var upevt = document.createEvent("HTMLEvents");
                upevt.initEvent("keyup", false, true);
                displayElement.dispatchEvent(upevt);
                upevt.keyCode = 9;
                displayElement.dispatchEvent(upevt);

                var evt = document.createEvent("HTMLEvents");
                evt.initEvent("change", false, true);
                displayElement.dispatchEvent(evt);
                // Find the event that triggers address control to check country !!
            } else {
                element.value = fieldValue;
                var evt = document.createEvent("HTMLEvents");
                evt.initEvent("change", false, true);
                element.dispatchEvent(evt);
            }
        }
    ''' % (field_name, field_value)

    context.browser.execute_script(script)


def check_value_for_heading(context, field_name, field_value):
    # Get the TH using xpath
    # Then look for the next element, which should be a td
    # Get it's contents
    if field_name.lower() == 'title':
        element = get_element_for_css(context=context, css='h1.record-title')
        assert_that(element.text.lower(), contains_string(field_value.lower()))
    else:
        script = '''
            var element = document.evaluate(
                ".//th[.//text()[contains(., '%s')]]",
                document,
                null,
                XPathResult.FIRST_ORDERED_NODE_TYPE,
                null)
                .singleNodeValue;

            if (element) {
                console.log('element', element);
                element.scrollIntoView(true);
                return element.nextElementSibling.innerText;
            }
        ''' % field_name

        text = context.browser.execute_script(script)
        print('----------- %s ---------' % field_name)
        assert_that(text, not_none())
        assert_that(text.lower(), contains_string(field_value.lower()))
