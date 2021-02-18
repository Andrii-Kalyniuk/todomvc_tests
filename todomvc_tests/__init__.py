from todomvc_tests.model.todos import Todo


class App:

    def __init__(self):
        self.todomvc = Todo(browser_name='firefox')


app = App()
todomvc = Todo(browser_name='firefox')
