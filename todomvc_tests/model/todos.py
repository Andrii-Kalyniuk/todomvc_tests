from selene.support.conditions import have
from selene.support.shared import browser

_list = browser.all('#todo-list>li')


def visit():
    is_new_todo_input_alive = (
        "$._data($('#new-todo').get(0), 'events').hasOwnProperty('keyup') "
        "&& Object.keys(require.s.contexts._.defined).length === 39")
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.wait_until(have.js_returned(True, is_new_todo_input_alive))


def add(*todos: str):
    for todo in todos:
        browser.element('#new-todo').type(todo).press_enter()


def should_be(*todos: str):
    _list.should(have.exact_texts(*todos))


def start_editing(old_todo: str, new_todo: str):
    _list.element_by(have.exact_text(old_todo)).double_click()
    return _list.element_by(have.css_class('editing'))\
        .element('.edit').with_(set_value_by_js=True).set_value(new_todo)


def edit(old_todo: str, new_todo: str):
    start_editing(old_todo, new_todo).press_enter()


def cancel_edit(old_todo: str, new_todo: str):
    start_editing(old_todo, new_todo).press_escape()


def toggle(todo: str):
    _list.element_by(have.exact_text(todo)).element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def delete(todo: str):
    browser.element('body').hover()
    _list.element_by(have.exact_text(todo)).hover() \
        .element('.destroy').click()
