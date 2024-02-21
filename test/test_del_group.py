from random import randrange


def test_del_group(app):
    if len(app.groups.get_group_list()) <= 1:
        app.groups.add_new_group('group for deleting')
    old_list = app.groups.get_group_list()
    index = randrange(len(old_list))
    app.groups.delete_group_by_index(index)
    new_list = app.groups.get_group_list()
    old_list[index:index + 1] = []
    assert sorted(old_list) == sorted(new_list)
