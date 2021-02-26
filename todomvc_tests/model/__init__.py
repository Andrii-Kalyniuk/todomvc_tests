from todomvc_tests.model.todos import TodomvcPage


class App:

    def __init__(self):
        self.todomvc = TodomvcPage(browser_name='firefox')


app = App()
todomvc = TodomvcPage(browser_name='firefox')
