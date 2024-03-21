import pytest
from src.tablaAsignacion import tablaAsignacion

@pytest.fixture
def inyector():
    tabla = tablaAsignacion()
    return tabla

@pytest.mark.getTabla
def test_devolverTabla(inyector):
    assert inyector.getTabla() == [  
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        ]

@pytest.mark.getLetter
def test_getLetter(inyector):
    assert inyector.getLetter(0) == 'T'
    assert inyector.getLetter(2) == 'W'
    assert inyector.getLetter(5) == 'M'
    assert inyector.getLetter(26) == 'La posición de la letra está fuera del índice.'

@pytest.mark.getLength
def test_getLenght(inyector):
    assert inyector.getLength() == 23

@pytest.mark.getPosition
def test_getPosition(inyector):
    assert inyector.getPosition('12345678') == 14
    assert inyector.getPosition('98765432') == 5
    assert inyector.getPosition('91234567') == 7

@pytest.mark.calculateLetter
def test_calculateLetter(inyector):
    assert inyector.calculateLetter('12345678') == 'Z'
    assert inyector.calculateLetter('98765432') == 'M'
    assert inyector.calculateLetter('91234567') == 'F'

