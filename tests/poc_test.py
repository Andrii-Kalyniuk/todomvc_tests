from selene.support.conditions import have
from selene.support.shared import browser


def test_todos_basic_management():
    browser.config.browser_name = 'firefox'
    is_new_todo_input_live_check = "$._data($('#new-todo').get(0), 'events')" \
                                   ".hasOwnProperty('keyup')"

    # GIVEN open Todomvc
    browser.open('https://todomvc4tasj.herokuapp.com')
    browser.wait_until(have.js_returned(True, is_new_todo_input_live_check))

    # Add
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    # Edit
    browser.all('#todo-list>li').element_by(have.exact_text('a'))\
        .double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing'))\
        .element('.edit').type(' edited').press_enter()

    # Complete
    browser.all('#todo-list>li').element_by(have.exact_text('a edited'))\
        .element('.toggle').click()
    browser.all('#todo-list>li').element_by(have.exact_text('b'))\
        .element('.toggle').click()

    # Clear completed
    browser.element('#clear-completed').click()
    browser.all('#todo-list>li').should(have.exact_texts('c'))

    # Cancel Edit
    browser.all('#todo-list>li').element_by(have.exact_text('c'))\
        .double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing'))\
        .element('.edit').type(' to be canceled').press_escape()

    # Delete
    browser.all('#todo-list>li').element_by(have.exact_text('c'))\
        .hover().element('.destroy').click()
    browser.all('#todo-list>li').should(have.size(0))
