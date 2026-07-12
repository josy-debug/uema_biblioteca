import unittest

from biblioteca.acervo import Acervo

# --- Mock Object ---
class LivroMock:
    """Classe simulada para representar um Livro nos testes."""
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

# --- Classe de Testes ---
class TestAcervo(unittest.TestCase):

    def setUp(self):
        """Executado antes de cada teste. Cria um acervo padrão com alguns livros."""
        self.acervo = Acervo("Acervo Teste")
        
        self.livro1 = LivroMock("Dom Casmurro", "Machado de Assis", disponivel=True)
        self.livro2 = LivroMock("Quincas Borba", "machado de assis", disponivel=False) # Autor em minúsculo, emprestado
        self.livro3 = LivroMock("O Alquimista", "Paulo Coelho", disponivel=True)
        self.livro4 = LivroMock("Dom Casmurro - Análise", "João da Silva", disponivel=False) # Mesmo nome parcial, outro autor
        
        # Adicionando os livros ao acervo
        self.acervo.adicionar_livro(self.livro1)
        self.acervo.adicionar_livro(self.livro2)
        self.acervo.adicionar_livro(self.livro3)
        self.acervo.adicionar_livro(self.livro4)

    def test_init(self):
        """Testa se a inicialização cria o acervo corretamente."""
        acervo_vazio = Acervo("Nova Biblioteca")
        self.assertEqual(acervo_vazio.nome, "Nova Biblioteca")
        self.assertEqual(acervo_vazio.livros, [])

    def test_adicionar_livro(self):
        """Testa se os livros são adicionados corretamente à lista."""
        self.assertEqual(self.acervo.total_livros(), 4)
        
        novo_livro = LivroMock("Novo Livro", "Autor Novo")
        self.acervo.adicionar_livro(novo_livro)
        
        self.assertEqual(self.acervo.total_livros(), 5)
        self.assertIn(novo_livro, self.acervo.livros)

    def test_total_livros(self):
        """Testa o retorno da contagem total de livros."""
        self.assertEqual(self.acervo.total_livros(), 4)
        
        acervo_vazio = Acervo("Vazio")
        self.assertEqual(acervo_vazio.total_livros(), 0)

    def test_buscar_por_titulo(self):
        """Testa a busca por título (case-insensitive e substring)."""
        # Busca exata
        resultado = self.acervo.buscar_por_titulo("O Alquimista")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].autor, "Paulo Coelho")

        # Busca case-insensitive
        resultado = self.acervo.buscar_por_titulo("dom casmurro")
        self.assertEqual(len(resultado), 2) # Deve encontrar livro1 e livro4

        # Busca por substring
        resultado = self.acervo.buscar_por_titulo("Quincas")
        self.assertEqual(len(resultado), 1)
        
        # Busca por título inexistente
        resultado = self.acervo.buscar_por_titulo("Harry Potter")
        self.assertEqual(len(resultado), 0)
        self.assertEqual(resultado, [])

    def test_buscar_por_autor(self):
        """Testa a busca por autor."""
        # Busca exata
        resultado = self.acervo.buscar_por_autor("Paulo Coelho")
        self.assertEqual(len(resultado), 1)

        # Busca por substring
        resultado = self.acervo.buscar_por_autor("Silva")
        self.assertEqual(len(resultado), 1)

        # Se o método fosse consistente com buscar_por_titulo, isso deveria retornar 2 livros (livro1 e livro2).
        # No entanto, como há o bug de case-sensitivity, ele retorna apenas 1.
        resultado_bug = self.acervo.buscar_por_autor("machado de assis")
        self.assertEqual(len(resultado_bug), 1) # Este teste passa confirmando o comportamento atual bugado.
        

    def test_livros_disponiveis(self):
        """Testa se apenas livros com disponivel=True são retornados."""
        disponiveis = self.acervo.livros_disponiveis()
        
        self.assertEqual(len(disponiveis), 2)
        
        # Garante que os livros retornados são realmente os disponíveis
        titulos_disponiveis = [livro.titulo for livro in disponiveis]
        self.assertIn("Dom Casmurro", titulos_disponiveis)
        self.assertIn("O Alquimista", titulos_disponiveis)
        self.assertNotIn("Quincas Borba", titulos_disponiveis)

    def test_livros_emprestados(self):
        """Testa se apenas livros com disponivel=False são retornados."""
        emprestados = self.acervo.livros_emprestados()
        
        self.assertEqual(len(emprestados), 2)
        
        # Garante que são os livros corretos
        titros_emprestados = [livro.titulo for livro in emprestados]
        self.assertIn("Quincas Borba", titros_emprestados)
        self.assertIn("Dom Casmurro - Análise", titros_emprestados)
        self.assertNotIn("O Alquimista", titros_emprestados)

if __name__ == '__main__':
    unittest.main()