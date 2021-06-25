from todomvc_tests.model import todomvc


def test_add_first_one():
    todomvc.visit().add()
    todomvc.should_have()
    todomvc.should_have_footer_hidden()

    todomvc.add('a')

    todomvc.should_have('a')
    todomvc.should_have_items_left(1)


def test_add_few():
    todomvc.visit()

    todomvc.add('a', 'b', 'c')

    todomvc.should_have('a', 'b', 'c')
    todomvc.should_have_items_left(3)


def test_edit():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')
    todomvc.should_have_items_left(3)

    todomvc.edit('b', 'b edited')

    todomvc.should_have('a', 'b edited', 'c')
    todomvc.should_have_items_left(3)


def test_edit_and_submit_by_loose_focus():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')
    todomvc.should_have_items_left(3)

    todomvc.edit_and_submit_by_loose_focus('b', 'b edited')

    todomvc.should_have('a', 'b edited', 'c')
    todomvc.should_have_items_left(3)


def test_cancel_edit():
    todomvc.visit()
    todomvc.add('a')
    todomvc.should_have_items_left(1)

    todomvc.cancel_edit('a', 'a edited')

    todomvc.should_have('a')
    todomvc.should_have_items_left(1)


def test_complete():
    todomvc.visit()
    todomvc.add('a', 'b', 'c', 'd', 'e')

    todomvc.toggle('a', 'c', 'e')

    todomvc.should_have_active('b', 'd')
    todomvc.should_have_completed_count(3)


def test_complete_all():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.toggle_all()

    todomvc.should_have_completed('a', 'b', 'c')
    todomvc.should_have_active()
    todomvc.should_have_items_left(0)
    todomvc.should_have_clear_completed_visible()


def test_complete_all_with_few_competed():
    todomvc.visit()
    todomvc.add('a', 'b', 'c', 'e')
    todomvc.toggle('b', 'e')

    todomvc.toggle_all()

    todomvc.should_have_completed('a', 'b', 'c', 'e')
    todomvc.should_have_active()
    todomvc.should_have_items_left(0)
    todomvc.should_have_clear_completed_visible()


def test_activate():
    todomvc.visit()
    todomvc.add('a', 'b', 'c', 'd', 'e')
    todomvc.toggle('a', 'c', 'e')

    todomvc.toggle('a', 'c', 'e')

    todomvc.should_have_active('a', 'b', 'c', 'd', 'e')
    todomvc.should_have_completed_count(0)
    todomvc.should_have_completed()
    todomvc.should_have_items_left(5)
    todomvc.should_have_clear_completed_hidden()


def test_activate_vs_js_precondition():
    todomvc.given_opened_with(
        {'completed': True, 'title': 'a'},
        {'completed': False, 'title': 'b'},
        {'completed': True, 'title': 'c'},
        {'completed': False, 'title': 'd'},
        {'completed': True, 'title': 'e'}
    )

    todomvc.toggle('a', 'c', 'e')

    todomvc.should_have_active('a', 'b', 'c', 'd', 'e')
    todomvc.should_have_completed_count(0)
    todomvc.should_have_completed()
    todomvc.should_have_items_left(5)
    todomvc.should_have_clear_completed_hidden()


def test_activate_all():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')
    todomvc.toggle_all()

    todomvc.toggle_all()

    todomvc.should_have_active('a', 'b', 'c')
    todomvc.should_have_completed()
    todomvc.should_have_items_left(3)
    todomvc.should_have_clear_completed_hidden()


def test_delete():
    todomvc.visit()
    todomvc.add('a', 'b', 'c', 'e')

    todomvc.delete('a', 'c')


def test_delete_last_one():
    todomvc.visit()
    todomvc.add('a')

    todomvc.delete('a')

    todomvc.should_have()
    todomvc.should_have_footer_hidden()


def test_delete_by_edit_to_empty():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.edit('b', '')

    todomvc.should_have('a', 'c')
    todomvc.should_have_items_left(2)


def test_clear_completed():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')
    todomvc.toggle('a', 'c')

    todomvc.clear_completed()

    todomvc.should_have('b')
    todomvc.should_have_items_left(1)


def test_items_left_count_decrement():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')
    todomvc.should_have_items_left(3)

    todomvc.toggle('a').delete('c')

    todomvc.should_have_items_left(1)


def test_items_left_count_increment():
    todomvc.visit()
    todomvc.add('a', 'b')
    todomvc.toggle('b')
    todomvc.should_have_items_left(1)

    todomvc.add('c').toggle('b')

    todomvc.should_have_items_left(3)


def test_keep_storage_after_page_refresh():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')
    todomvc.should_have_items_left(3)

    todomvc.refresh()
    todomvc.visit()

    todomvc.should_have('a', 'b', 'c')
    todomvc.should_have_items_left(3)
