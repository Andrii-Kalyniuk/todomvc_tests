from todomvc_tests import todomvc


def test_add():
    todomvc.visit()\
        .add('a', 'b', 'c')\
        .should_be('a', 'b', 'c').should_items_left(3)


def test_edit():
    todomvc.visit().add('a').should_items_left(1)\
        .edit('a', 'a edited')\
        .should_be('a edited').should_items_left(1)


def test_cancel_edit():
    todomvc.visit().add('a').should_items_left(1)\
        .cancel_edit('a', 'a edited')\
        .should_be('a').should_items_left(1)


def test_complete():
    todomvc.visit().add('a', 'b', 'c', 'd', 'e')\
        .toggle('a', 'c', 'e')\
        .should_be_active('b', 'd').should_be_completed_count(3)


def test_complete_all():
    todomvc.visit().add('a', 'b', 'c')\
        .toggle_all()\
        .should_be_completed('a', 'b', 'c')\
        .should_items_left(0)


def test_activate():
    todomvc.visit().add('a', 'b', 'c', 'd', 'e').toggle('a', 'c', 'e')\
        .toggle('a', 'c', 'e')\
        .should_be_active('a', 'b', 'c', 'd', 'e')\
        .should_be_completed_count(0).should_items_left(5)


def test_activate_all():
    todomvc.visit().add('a', 'b', 'c').toggle_all()\
        .toggle_all()\
        .should_be_active('a', 'b', 'c')\
        .should_items_left(3)


def test_delete():
    todomvc.visit().add('a', 'i', 'b')\
        .delete('a', 'b')\
        .should_be('i').should_items_left(1)


def test_clear_completed():
    todomvc.visit().add('a', 'b', 'c')\
        .toggle('a', 'c')\
        .clear_completed()\
        .should_be('b').should_items_left(1)


def test_items_left_count_decrement():
    todomvc.visit().add('a', 'b', 'c').should_items_left(3)\
        .toggle('a').delete('c')\
        .should_items_left(1)


def test_items_left_count_increment():
    todomvc.visit().add('a', 'b').toggle('b').should_items_left(1)\
        .add('c').toggle('b')\
        .should_items_left(3)


def test_filter_active_from_all():
    todomvc.visit().add('a', 'b', 'c').toggle('b', 'c')\
        .filter_active()\
        .should_be('a').should_items_left(1)


def test_filter_active_from_completed():
    todomvc.visit().add('a', 'b', 'c').toggle('b', 'c').filter_completed()\
        .filter_active()\
        .should_be('a').should_items_left(1)


def test_filter_completed_from_all():
    todomvc.visit().add('a', 'b', 'c').toggle('b', 'c')\
        .filter_completed()\
        .should_be('b', 'c').should_items_left(1)


def test_filter_completed_from_active():
    todomvc.visit().add('a', 'b', 'c').toggle('b', 'c').filter_active()\
        .filter_completed()\
        .should_be('b', 'c').should_items_left(1)


def test_filter_all_from_completed():
    todomvc.visit().add('a', 'b', 'c').toggle('b', 'c').filter_completed()\
        .filter_all()\
        .should_be('a', 'b', 'c')\
        .should_be_active('a').should_items_left(1)\
        .should_be_completed('b', 'c')


def test_filter_all_from_active():
    todomvc.visit().add('a', 'b', 'c').toggle('b', 'c').filter_active()\
        .filter_all()\
        .should_be('a', 'b', 'c')\
        .should_be_active('a').should_items_left(1)\
        .should_be_completed('b', 'c')


def test_keep_storage_after_page_refresh():
    todomvc.visit().add('a', 'b', 'c')\
        .should_items_left(3)\
        .refresh().visit()\
        .should_be('a', 'b', 'c').should_items_left(3)
