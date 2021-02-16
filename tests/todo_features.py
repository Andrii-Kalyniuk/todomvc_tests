from todomvc_tests import app


def test_add():
    app.todomvc.visit()\
        .add('a', 'b', 'c')\
        .should_be('a', 'b', 'c')


def test_edit():
    app.todomvc.visit().add('a')\
        .edit('a', 'a edited')\
        .should_be('a edited')


def test_cancel_edit():
    app.todomvc.visit().add('a')\
        .cancel_edit('a', 'a edited')\
        .should_be('a')


def test_complete():
    app.todomvc.visit().add('a', 'b', 'c', 'd', 'e')\
        .toggle('a', 'c', 'e')\
        .should_be_active('b', 'd').should_be_completed_count(3)


def test_activate():
    app.todomvc.visit().add('a', 'b', 'c', 'd', 'e').toggle('a', 'c', 'e')\
        .toggle('a', 'c', 'e')\
        .should_be_active('a', 'b', 'c', 'd', 'e').should_be_completed_count(0)


def test_delete():
    app.todomvc.visit().add('a', 'i', 'b')\
        .delete('a', 'b')\
        .should_be('i')


def test_clear_completed():
    app.todomvc.visit().add('a', 'b', 'c')\
        .toggle('a', 'c')\
        .clear_completed()\
        .should_be('b')


def test_items_left_count_decrement():
    app.todomvc.visit().add('a', 'b', 'c')\
        .should_items_left(3)\
        .toggle('a', 'c')\
        .should_items_left(1)


def test_items_left_count_increment():
    app.todomvc.visit().add('a')\
        .should_items_left(1)\
        .add('b', 'c') \
        .should_items_left(3)


def test_filter_active_from_all():
    app.todomvc.visit().add('a', 'b', 'c').toggle('b', 'c')\
        .filter_active()\
        .should_be('a')


def test_filter_active_from_completed():
    app.todomvc.visit().add('a', 'b', 'c').toggle('b', 'c').filter_completed()\
        .filter_active()\
        .should_be('a')


def test_filter_completed_from_all():
    app.todomvc.visit().add('a', 'b', 'c').toggle('b', 'c')\
        .filter_completed() \
        .should_be('b', 'c')


def test_filter_completed_from_active():
    app.todomvc.visit().add('a', 'b', 'c').toggle('b', 'c').filter_active()\
        .filter_completed()\
        .should_be('b', 'c')


def test_filter_all_from_completed():
    app.todomvc.visit().add('a', 'b', 'c').toggle('b', 'c').filter_completed()\
        .filter_all()\
        .should_be('a', 'b', 'c')\
        .should_be_active('a')\
        .should_be_completed('b', 'c')


def test_filter_all_from_active():
    app.todomvc.visit().add('a', 'b', 'c').toggle('b', 'c').filter_active()\
        .filter_all()\
        .should_be('a', 'b', 'c')\
        .should_be_active('a')\
        .should_be_completed('b', 'c')


def test_keep_storage_after_page_refresh():
    app.todomvc.visit().add('a', 'b', 'c')\
        .refresh().visit()\
        .should_be('a', 'b', 'c')
