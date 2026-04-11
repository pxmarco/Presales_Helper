import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.main import extrair_requisitos, montar_estrutura


def test_extrair_requisitos():
    texto = "1.1 Req 1\n2. Req 2"

    resultado = extrair_requisitos(texto)

    assert resultado == ["1.1 Req 1", "2. Req 2"]


def test_extrair_requisitos_vazio():
    texto = ""
    resultado = extrair_requisitos(texto)

    assert resultado == []


def test_montar_estrutura():
    requisitos = ["1.1 Req 1"]

    estrutura = montar_estrutura(requisitos)

    assert estrutura[0]["requisito"] == "1.1 Req 1"
