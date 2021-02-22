from todomvc_tests import app


def test_todos_life_cycle():
    app.todomvc.visit()

    app.todomvc.add('a', 'b', 'c')\
        .should_have('a', 'b', 'c')

    app.todomvc.edit('b', 'b edited')

    app.todomvc.toggle('b edited')

    app.todomvc.clear_completed()\
        .should_have('a', 'c')

    app.todomvc.cancel_edit('c', 'c to be canceled')

    app.todomvc.delete('c')\
        .should_have('a')
