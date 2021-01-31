from selene.support.conditions import have, be
from selene.support.shared import browser

TODO_LIST = browser.all('#todo-list>li')


def visit():
    browser.config.browser_name = 'firefox'
    is_new_todo_input_live_check = "$._data($('#new-todo').get(0), 'events')" \
                                   ".hasOwnProperty('keyup')"
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.wait_until(have.js_returned(True, is_new_todo_input_live_check))


def add(*todos_texts: str):
    for todo_text in todos_texts:
        browser.element('#new-todo').type(todo_text).press_enter()


def edit(old_todo: str, new_todo: str, cancel_changes=False):
    """
    :param old_todo: current todos text, before editing
    :param new_todo: new todos text, after editing
    :param cancel_changes: False by default to save changes.
    Use True to cancel changes in the todos text after editing.
    """
    TODO_LIST.element_by(have.exact_text(old_todo)).double_click()
    edited_todo = TODO_LIST.element_by(have.css_class('editing'))\
        .element('.edit').with_(set_value_by_js=True).set_value(new_todo)
    if cancel_changes:
        edited_todo.press_escape()
    else:
        edited_todo.press_enter()


def toggle(*todos_texts: str):
    for todo_text in todos_texts:
        TODO_LIST.element_by(have.exact_text(todo_text))\
            .element('.toggle').click()


def should_be(*todos_texts: str):
    TODO_LIST.should(have.exact_texts(*todos_texts))


def clear_completed():
    browser.element('#clear-completed').click()
    # mouseover to prevent 'could not be scrolled into view' problem
    # in delete() function
    # browser.element('#new-todo').hover()


def delete(*todos_texts: str):
    for todo_text in todos_texts:
        TODO_LIST.element_by(have.exact_text(todo_text)).hover() \
            .element('.destroy').click()
