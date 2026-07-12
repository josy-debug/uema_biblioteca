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


@pytest.fixture
def livro_exemplo():
    """Cria uma instância de Livro para ser usada nos testes."""
    return Livro("O Senhor dos Aneis", "J.R.R. Tolkien", "978-0000000000")

def test_init_livro(livro_exemplo):
    """Testa se o livro é inicializado corretamente."""
    assert livro_exemplo.titulo == "O Senhor dos Aneis"
    assert livro_exemplo.autor == "J.R.R. Tolkien"
    assert livro_exemplo.isbn == "978-0000000000"
    assert livro_exemplo.disponivel is True

def test_emprestar_sucesso(livro_exemplo):
    """Testa se o livro muda de status para emprestado com sucesso."""
    livro_exemplo.emprestar()
    assert livro_exemplo.disponivel is False

def test_emprestar_falha_quando_ja_emprestado(livro_exemplo):
    """Testa se levanta erro ao tentar emprestar um livro já emprestado."""
    livro_exemplo.emprestar() # Empresta a primeira vez
    
    with pytest.raises(ValueError, match="ja esta emprestado"):
        livro_exemplo.emprestar() # Tenta emprestar de novo

def test_devolver_sucesso(livro_exemplo):
    """Testa se a devolução ocorre com sucesso."""
    livro_exemplo.emprestar() # Precisa estar emprestado para devolver
    assert livro_exemplo.disponivel is False
    
    livro_exemplo.devolver()
    assert livro_exemplo.disponivel is True

def test_devolver_falha_quando_ja_disponivel(livro_exemplo):
    """Testa se levanta erro ao tentar devolver um livro que já está disponível."""
    # O livro começa disponível pela fixture
    with pytest.raises(ValueError, match="nao esta emprestado"):
        livro_exemplo.devolver()

def test_str_disponivel(livro_exemplo):
    """Testa a representação em string quando o livro está disponível."""
    resultado = str(livro_exemplo)
    assert resultado == "'O Senhor dos Aneis' de J.R.R. Tolkien (ISBN:978-0000000000) [Disponivel]"

def test_str_emprestado(livro_exemplo):
    """Testa a representação em string quando o livro está emprestado."""
    livro_exemplo.emprestar()
    resultado = str(livro_exemplo)
    assert resultado == "'O Senhor dos Aneis' de J.R.R. Tolkien (ISBN:978-0000000000) [Emprestado]"

    

# ── Complete os testes abaixo ─────────────────────────────────────────────
# Voce deve escrever testes para:
#   devolver() — livro emprestado (deve funcionar)
#   devolver() — livro disponivel (deve levantar ValueError)
#   __str__()  — verificar o formato da string retornada
