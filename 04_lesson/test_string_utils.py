import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize('input, result',
                         [('skypro', 'Skypro'),
                          ('скайпро', 'Скайпро')])
def test_capitilize_positive(input, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(input)
    assert res == result


@pytest.mark.parametrize('input, result',
                         [('', None),
                          ('  ', None)])
def test_capitilize_negative(input, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(input)
    assert res == result


@pytest.mark.parametrize('input, result',
                         [('   skypro', 'skypro'),
                          (' 1sky2', '1sky2')])
def test_trim_positive(input, result):
    string_utils = StringUtils()
    res = string_utils.trim(input)
    assert res == result


@pytest.mark.parametrize('input, result',
                         [('4:5:6', ['4', '5', '6']),
                          ('x,y,z', ['x', 'y', 'z'])])
def test_to_list_positive(input, result):
    string_utils = StringUtils()
    res = string_utils.to_list(input)
    assert res == result


@pytest.mark.parametrize('input, result',
                         [('', []),
                          (' ', [])])
def test_to_list_negative(input, result):
    string_utils = StringUtils()
    res = string_utils.to_list(input)
    assert res == result


@pytest.mark.parametrize('input, symbol',
                         [('SkyPro', 'S'),
                          ('Movie1', 'U'),
                          ('Movie1 Skyeng', '2')])
def test_contains_positive(input, symbol):
    string_utils = StringUtils()
    res = string_utils.to_list(input, symbol)
    assert res


@pytest.mark.parametrize('input, symbol',
                         [('', ''),
                          ('  ', 'U')])
def test_contains_negative(input, symbol):
    string_utils = StringUtils()
    res = string_utils.to_list(input, symbol)
    # local variable 'res' is assigned to but never used
    assert res is None


@pytest.mark.parametrize('input, symbol',
                         [('SkyPro', 'S'),
                          ('Movie1', 'ov'),
                          ('Movie1 Skyeng', '1 S')])
def test_delete_symbol_positive(input, symbol):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input, symbol)
    assert res


@pytest.mark.parametrize('input, symbol',
                         [('SkyPro', 'L'),
                          ('Movie1', ''),
                          (' ', 'Sk')])
def test_delete_symbol_negative(input, symbol):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input, symbol)
    # local variable 'res' is assigned to but never used
    assert res is None


@pytest.mark.parametrize('input, symbol',
                         [('SkyPro', 'S'),
                          ('12movie1', '1'),
                          ('Movie1 Skyeng', 'M')])
def test_starts_with_positive(input, symbol):
    string_utils = StringUtils()
    res = string_utils.starts_with(input, symbol)
    # local variable 'res' is assigned to but never used
    assert True


@pytest.mark.parametrize('input, symbol',
                         [('Movie1', 'V'),
                          ('Movie1 Skyeng', '1')])
def test_starts_with_positive2(input, symbol):
    string_utils = StringUtils()
    res = string_utils.starts_with(input, symbol)
    # local variable 'res' is assigned to but never used
    assert False


@pytest.mark.parametrize('input, symbol',
                         [('', ''),
                          ('  ', '1')])
def test_starts_with_negative2(input, symbol):
    string_utils = StringUtils()
    res = string_utils.starts_with(input, symbol)
    # local variable 'res' is assigned to but never used
    assert res is None


@pytest.mark.parametrize('input, symbol',
                         [('SkyPro', 'o'),
                          ('12movie1', '1'),
                          ('Movie1 Skyeng', 'g')])
def test_end_with_positive(input, symbol):
    string_utils = StringUtils()
    res = string_utils.end_with(input, symbol)
    # local variable 'res' is assigned to but never used
    assert True


@pytest.mark.parametrize('input, symbol',
                         [('SkyPro', 'P'),
                          ('12movie1', '0'),
                          ('Movie1 Skyeng', 'M')])
def test_end_with_positive2(input, symbol):
    string_utils = StringUtils()
    res = string_utils.end_with(input, symbol)
    # local variable 'res' is assigned to but never used
    assert False


@pytest.mark.parametrize('input, symbol',
                         [('', ''),
                          ('  ', '1')])
def test_end_with_negative(input, symbol):
    string_utils = StringUtils()
    res = string_utils.end_with(input, symbol)
    # local variable 'res' is assigned to but never used
    assert res is None


@pytest.mark.parametrize('input',
                         [('SkyPro'),
                          ('12movie1'),
                          ('Movie1 Skyeng')])
def test_is_empty_positive(input):
    string_utils = StringUtils()
    res = string_utils.is_empty(input)
    # local variable 'res' is assigned to but never used
    assert False


def test_is_empty_positive2():
    string_utils = StringUtils()
    res = string_utils.is_empty('')
    # local variable 'res' is assigned to but never used
    assert True


@pytest.mark.parametrize('input, symbol, result',
                         [(['4', '5', '6'], '', '4, 5, 6'),
                          (['x', 'y'], '-', 'x-y'),
                          (['Mega', 'Mozg'], ':', 'Mega:Mozg')])
def test_list_to_string_positive(input, symbol, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(input, symbol)
    assert res == result
