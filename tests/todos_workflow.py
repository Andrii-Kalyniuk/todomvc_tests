from todomvc_tests.pages import todos


def test_todos_basic_management():
    todos.visit()

    todos.add('a', 'b', 'c')
    todos.should_have_exact_texts('a', 'b', 'c')

    todos.edit('a', ' edited')

    todos.complete('a edited')

    todos.clear_completed()
    todos.should_have_exact_texts('b', 'c')

    todos.edit('c', ' to be canceled', mode='cancel')

    todos.delete('c')
    todos.should_have_exact_texts('b')
