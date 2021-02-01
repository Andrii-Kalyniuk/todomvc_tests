from selene.support.conditions import have
from selene.support.shared import browser

todos = browser.all('#todo-list>li')


def visit():
    is_new_todo_input_live_check = "$._data($('#new-todo').get(0), 'events')" \
                                   ".hasOwnProperty('keyup')"
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.wait_until(have.js_returned(True, is_new_todo_input_live_check))


def add(*todos_texts: str):
    for todo_text in todos_texts:
        browser.element('#new-todo').type(todo_text).press_enter()


def should_be(*todos_texts: str):
    todos.should(have.exact_texts(*todos_texts))


def start_editing(old_todo: str, new_todo: str):
    todos.element_by(have.exact_text(old_todo)).double_click()
    return todos.element_by(have.css_class('editing'))\
        .element('.edit').with_(set_value_by_js=True).set_value(new_todo)


def edit(old_todo: str, new_todo: str):
    start_editing(old_todo, new_todo).press_enter()


def cancel_edit(old_todo: str, new_todo: str):
    start_editing(old_todo, new_todo).press_escape()


def toggle(*todos_texts: str):
    for todo_text in todos_texts:
        todos.element_by(have.exact_text(todo_text))\
            .element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def delete(todo_text: str):
    browser.element('body').hover()
    todos.element_by(have.exact_text(todo_text)).hover() \
        .element('.destroy').click()
