import pytest

from funbox import utils


def test_link_parser():
    assert utils.parse_link('https://ya.ru') == 'ya.ru'
    assert utils.parse_link('https://ya.ru?q=123') == 'ya.ru'
    assert utils.parse_link('funbox.ru') == 'funbox.ru'
    assert utils.parse_link('https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor') == 'stackoverflow.com'
    with pytest.raises(ValueError):
        utils.parse_link('applebananadeepfries')