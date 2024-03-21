import pytest
from src.DNI import Dni


@pytest.mark.getDni
def test_getDni():
    assert Dni('15900638W').getDni() == '15900638W'

@pytest.mark.isValidLenght
def test_isValidLenght():
    assert Dni("12312312A").isValidLenght()
    assert not Dni("123123ASFSD12A").isValidLenght()
    assert not Dni("1231").isValidLenght()

@pytest.mark.isValidNumber
def test_isValidNumber():
    assert Dni('12345678A').isValidNumber()
    assert not Dni('A1234567B').isValidNumber()

@pytest.mark.isLetterInTabla
def test_isLetterInTabla():
    assert Dni('12345678A').isLetterInTabla()
    assert not Dni('123456789O').isLetterInTabla()

@pytest.mark.checkDni
def test_checkDni():
    assert Dni('39451218P').checkDni()
    assert not Dni('12345678A').checkDni()
    
    listaDniValidos = ["70965045V", "16202290D", "66752403D", "15900638W", "70371202B", "51531149V", "44874568G", "55659698C", "34330970C", "51618753Z", "64729253P", "64950405S", "74913446P", "64095400N", "89019093P", "92401702F", "73471442N","78484464T","72376173A","01817200Q","95882054E","63587725Q","26861694V","21616083Q","26868974Y","40135330P","89044648X","80117501Z","34168723S","76857238R","66714505S","66499420A",]
    
    assert all(Dni(item).checkDni() for item in listaDniValidos)