from selene.support.conditions import have
from selene.support.shared import browser


def visit():
    browser.config.browser_name = 'firefox'
    is_new_todo_input_live_check = "$._data($('#new-todo').get(0), 'events')" \
                                   ".hasOwnProperty('keyup')"
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.wait_until(have.js_returned(True, is_new_todo_input_live_check))


def add(*todo_texts):
    for text in todo_texts:
        browser.element('#new-todo').type(text).press_enter()


def edit(old_text, appended_text, mode='save'):
    browser.all('#todo-list>li').element_by(have.exact_text(old_text)) \
        .double_click()
    edited_todo = browser.all('#todo-list>li').element_by(
        have.css_class('editing')).element('.edit').type(appended_text)
    if mode == 'cancel':
        edited_todo.press_escape()
    else:
        edited_todo.press_enter()


def complete(*todo_texts):
    for text in todo_texts:
        browser.all('#todo-list>li').element_by(have.exact_text(text)) \
            .element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def should_have_exact_texts(*todo_texts):
    browser.all('#todo-list>li').should(have.exact_texts(*todo_texts))


def list_should_have_size(number_of_todos):
    browser.all('#todo-list>li').should(have.size(number_of_todos))


def delete(todo_text):
    browser.all('#todo-list>li').element_by(have.exact_text(todo_text)) \
        .hover().element('.destroy').click()
