from selene.support.conditions import have, be
from selene.support.shared import browser


class TodomvcPage:

    def __init__(self, browser=browser, browser_name='chrome'):
        self.browser = browser
        self.browser.config.browser_name = browser_name
        self._list = self.browser.all('#todo-list>li')
        self._active = self._list.filtered_by(have.css_class('active'))
        self._completed = self._list.filtered_by(have.css_class('completed'))

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

    def should_be_active(self, *todos):
        self._active.should(have.exact_texts(*todos))
        return self

    def should_be_active_count(self, count_of_active: int):
        self._active.should(have.size(count_of_active))
        return self

    def should_be_completed(self, *todos):
        self._completed.should(have.exact_texts(*todos))
        return self

    def should_be_completed_count(self, count_of_completed: int):
        self._completed.should(have.size(count_of_completed))
        return self

    def start_editing(self, old_todo: str, new_todo: str):
        self._list.element_by(have.exact_text(old_todo)).double_click()
        return self._list.element_by(have.css_class('editing'))\
            .element('.edit').with_(set_value_by_js=True).set_value(new_todo)

    def edit(self, old_todo: str, new_todo: str):
        self.start_editing(old_todo, new_todo).press_enter()
        return self

    def cancel_edit(self, old_todo: str, new_todo: str):
        self.start_editing(old_todo, new_todo).press_escape()
        return self

    def toggle(self, *todos):
        for todo in todos:
            self._list.element_by(have.exact_text(todo))\
                .element('.toggle').click()
        return self

    def toggle_all(self):
        self.browser.element('#toggle-all').click()
        return self

    def clear_completed(self):
        self.browser.element('#clear-completed').click()
        return self

    def delete(self, *todos):
        for todo in todos:
            self.browser.element('body').hover()
            self._list.element_by(have.exact_text(todo)).hover()\
                .element('.destroy').click()
        return self

    def should_items_left(self, count_of_active: int):
        self.browser.element('#todo-count strong')\
            .should(have.exact_text(f'{count_of_active}'))
        return self

    def filter_active(self):
        self.browser.element('[href="#/active"]').click()
        return self

    def filter_completed(self):
        self.browser.element('[href="#/completed"]').click()
        return self

    def filter_all(self):
        self.browser.element('[href="#/"]').click()
        return self

    def refresh(self):
        self.browser.driver.refresh()
        return self
