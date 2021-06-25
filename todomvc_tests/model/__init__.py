from todomvc_tests.model.todos import TodoMVCPage


class App:

    def __init__(self):
        self.todomvc = TodoMVCPage(browser_name='firefox')


app = App()
# todomvc = TodoMVCPage(browser_name='firefox')
todomvc = TodoMVCPage(browser_name='chrome')
