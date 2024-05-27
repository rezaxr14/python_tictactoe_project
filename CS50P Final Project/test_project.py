from project import Ticktacktoe, get_text, get_already_clicked, get_background_color
import pytest


# For simplicity’s sake I didn't use Setter(s) and Getter(s) in this project
def test_win_combo():
    root = Ticktacktoe()
    assert (0, 1, 2) in root.win
    assert (8, 4, 0) in root.win
    root.destroy()


def test_background():
    root = Ticktacktoe()
    root.background = "gray"
    root.alternate_background(None)
    assert root.background == "pink"
    root.destroy()


def test_restart():
    root = Ticktacktoe()
    root.x_moves = [2, 3, 4, 5, 6]
    root.o_moves = [3, 7]
    root.restart(None)
    assert root.x_moves == []
    assert root.o_moves == []
    root.destroy()


def test_initialize_coordination():
    root = Ticktacktoe()
    root.initialize_coordination(root.can)
    expected_tags = [f"cell{i}" for i in range(9)]
    for tag in expected_tags:
        assert tag in root.can.gettags(tag)
    root.destroy()


def test_get_text():
    root = Ticktacktoe()
    assert get_text(root, root.can) == "Tic Tac Toe Game!"
    root.destroy()


def test_get_background_color():
    root = Ticktacktoe()
    root.background = "pink"
    assert get_background_color(root) == "pink"
    root.destroy()


def test_get_already_clicked():
    root = Ticktacktoe()
    assert get_already_clicked(root) == [False for _ in range(9)]
    root.destroy()


def main():
    test_restart()
    test_background()
    test_win_combo()
    test_initialize_coordination()
    test_get_text()
    test_get_background_color()
    test_get_already_clicked()


if __name__ == '__main__':
    pytest.main()
