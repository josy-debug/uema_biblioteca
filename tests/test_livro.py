import pytest
from biblioteca.livro import Livro


# ── Testes existentes ─────────────────────────────────────────────────────

def test_criar_livro():
    livro = Livro("Dom Casmurro", "Machado de Assis", "978-85-359-0277-5")
    assert livro.titulo == "Dom Casmurro"
    assert livro.autor == "Machado de Assis"
    assert livro.disponivel is True


def test_emprestar_livro_disponivel():
    livro = Livro("O Cortico", "Azevedo", "978-85-001-0001-1")
    livro.emprestar()
    assert livro.disponivel is False


def test_emprestar_livro_ja_emprestado_levanta_erro():
    livro = Livro("Memorias Postumas", "Machado de Assis", "978-85-001-0002-2")
    livro.emprestar()
    with pytest.raises(ValueError):
        livro.emprestar()


# ── Complete os testes abaixo ─────────────────────────────────────────────
# Voce deve escrever testes para:
#   devolver() — livro emprestado (deve funcionar)
#   devolver() — livro disponivel (deve levantar ValueError)
#   __str__()  — verificar o formato da string retornada
