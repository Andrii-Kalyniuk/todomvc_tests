from todomvc_tests.model import todomvc


def test_todos_life_cycle():
    todomvc.visit()

    todomvc.add('a', 'b', 'c')\
        .should_have('a', 'b', 'c')

    todomvc.edit('b', 'b edited')

    todomvc.toggle('b edited')

    todomvc.clear_completed()\
        .should_have('a', 'c')

    todomvc.cancel_edit('c', 'c to be canceled')

    todomvc.delete('c')\
        .should_have('a')
