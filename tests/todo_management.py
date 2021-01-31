from todomvc_tests.model import todos


def test_todos_life_cycle():
    todos.visit()

    todos.add('a', 'b', 'c')
    todos.should_be('a', 'b', 'c')

    todos.edit('a', 'a edited')
    todos.toggle('a edited')

    todos.clear_completed()
    todos.should_be('b', 'c')
    todos.delete('b', 'c')
    return  # debug

    todos.edit('c', 'c to be canceled',
               cancel_changes=True)

    todos.delete('c')
    todos.should_be('b')
