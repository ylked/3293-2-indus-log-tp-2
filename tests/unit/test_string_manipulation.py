"""
Unit tests for test_string.py package
"""
import pytest

from src.string_manipulation import lower_case, upper_case, invert


# TODO: Implémenter les tests unitaires ci-dessous.
#       Les noms des méthodes indiquent ce qu'il faut tester.


@pytest.mark.parametrize(
    "s, expected",
    [
        ("HELLO my friends", "hello my friends"),
        ("lower case", "lower case"),
        (
            "UPPER CASE SENTENCE WITH SYMBOLS %&/()",
            "upper case sentence with symbols %&/()",
        ),
    ],
)
def test_lower_case(s, expected):
    """Tests lower_case function"""
    assert lower_case(s) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Hello world", "dlrow olleH"),
        ("*/---&&%???", "???%&&---/*"),
        ("This is a sentence I have written", "nettirw evah I ecnetnes a si sihT"),
    ],
)
def test_invert(s, expected):
    """Tests invert function"""
    assert invert(s) == expected


# NOTE: La fixture "parametrize" de pytest permet de réaliser
#       le même test avec des valeurs d'entrée différentes.
#       Ci-dessous, le test "test_upper_case" sera executé
#       3 fois avec les 3 sets de valeurs spécifiés.
#       N'hésitez pas à tester cette fixture sur les autres
#       tests pour comprendre comment elle fonctionne.
@pytest.mark.parametrize(
    "s, expected",
    [
        ("league of legends", "LEAGUE OF LEGENDS"),
        ("POKEMON", "POKEMON"),
        ("Street Fighter", "STREET FIGHTER"),
    ],
)
def test_upper_case(s, expected):
    """Tests upper_case function"""
    assert upper_case(s) == expected


@pytest.mark.parametrize(
    "value",
    [10, -5, 1.5, 1e5, object, ["abc", "def"], ("a", "b"), {1, 2, 3}, {1: "a", 2: "b"}],
)
def test_raises_exception_on_non_string_arguments_upper_case(value):
    """Tests that upper_case function raises a TypeError when its input is not a string"""
    with pytest.raises(TypeError):
        upper_case(value)


@pytest.mark.parametrize(
    "value",
    [10, -5, 1.5, 1e5, object, ["abc", "def"], ("a", "b"), {1, 2, 3}, {1: "a", 2: "b"}],
)
def test_raises_exception_on_non_string_arguments_lower_case(value):
    """Tests that lower_case function raises a TypeError when its input is not a string"""
    with pytest.raises(TypeError):
        lower_case(value)


@pytest.mark.parametrize(
    "value",
    [10, -5, 1.5, 1e5, object, ["abc", "def"], ("a", "b"), {1, 2, 3}, {1: "a", 2: "b"}],
)
def test_raises_exception_on_non_string_argument_invert(value):
    with pytest.raises(TypeError):
        invert(value)
