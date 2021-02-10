from selene.support.conditions import have
from selene.support.shared import browser


class Todo:

    def __init__(self, browser=browser, browser_name='chrome'):
        self.browser = browser
        self.browser.config.browser_name = browser_name
        self._list = self.browser.all('#todo-list>li')

    def visit(self):
        is_todomvc_js_loaded = (
            "return "
            "$._data($('#new-todo').get(0), 'events').hasOwnProperty('keyup') "
            "&& Object.keys(require.s.contexts._.defined).length === 39")
        self.browser.open('https://todomvc4tasj.herokuapp.com')
        self.browser.should(have.js_returned(True, is_todomvc_js_loaded))
        return self

    def add(self, *todos: str):
        for todo in todos:
            self.browser.element('#new-todo').type(todo).press_enter()
        return self

    def should_be(self, *todos: str):
        self._list.should(have.exact_texts(*todos))
        return self

    def start_editing(self, old_todo: str, new_todo: str):
        self._list.element_by(have.exact_text(old_todo)).double_click()
        return self._list.element_by(have.css_class('editing')) \
            .element('.edit').with_(set_value_by_js=True).set_value(new_todo)

    def edit(self, old_todo: str, new_todo: str):
        self.start_editing(old_todo, new_todo).press_enter()
        return self

    def cancel_edit(self, old_todo: str, new_todo: str):
        self.start_editing(old_todo, new_todo).press_escape()
        return self

    def toggle(self, todo: str):
        self._list.element_by(have.exact_text(todo)).element('.toggle').click()
        return self

    def clear_completed(self):
        self.browser.element('#clear-completed').click()
        return self

    def delete(self, todo: str):
        self.browser.element('body').hover()
        self._list.element_by(have.exact_text(todo)).hover() \
            .element('.destroy').click()
        return self
