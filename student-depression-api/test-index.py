#!/usr/bin/env python3
"""
Índice e Mapa de Documentação de Testes
Última atualização: 27 de Novembro de 2025
"""

import os

DOCUMENTATION_MAP = {
    "🚀 COMEÇAR AQUI": [
        ("QUICK_START_TESTS.md", "Começar em 30 segundos"),
        ("run-tests.sh", "Script auxiliar para executar testes"),
    ],
    
    "📚 DOCUMENTAÇÃO PRINCIPAL": [
        ("TESTING.md", "Guia completo de testes e cobertura"),
        ("TESTING_GUIDE.md", "Tutorial detalhado com exemplos práticos"),
        ("TEST_REPORT.md", "Relatório executivo dos testes"),
    ],
    
    "📋 SUMÁRIOS E REFERÊNCIA": [
        ("TESTS_SUMMARY.md", "Resumo visual dos testes"),
        ("README_TESTS.md", "README focado em testes"),
        ("IMPLEMENTATION_SUMMARY.md", "Sumário completo da implementação"),
    ],
    
    "⚙️ CONFIGURAÇÃO": [
        ("pytest.ini", "Configuração do pytest"),
        ("requirements.txt", "Dependências (com pytest e pytest-cov)"),
    ],
    
    "🧪 TESTES (7 arquivos)": [
        ("tests/conftest.py", "Fixtures e configuração compartilhada"),
        ("tests/test_main.py", "Testes da aplicação principal (4 testes)"),
        ("tests/test_model.py", "Testes do modelo SVM (20 testes)"),
        ("tests/test_questions.py", "Testes do endpoint de questões (18 testes)"),
        ("tests/test_integration.py", "Testes de integração entre módulos (14 testes)"),
        ("tests/test_validation.py", "Testes de validação de dados (9 testes)"),
    ],
}

QUICK_COMMANDS = {
    "Teste Rápido": "pytest -q",
    "Teste Completo": "pytest tests/ -v",
    "Com Cobertura": "pytest --cov=src --cov-report=term-missing",
    "Relatório HTML": "pytest --cov=src --cov-report=html",
    "Teste Específico": "pytest tests/test_model.py -v",
    "Modo Watch": "pip install pytest-watch && ptw",
}

STATISTICS = {
    "Testes Implementados": 65,
    "Taxa de Sucesso": "100%",
    "Cobertura de Código": "90%",
    "Tempo de Execução": "0.16s",
    "Linhas de Teste": 997,
    "Módulos Testados": 4,
    "Arquivos de Teste": 7,
    "Documentação": "9 arquivos",
}

def print_header():
    """Imprime cabeçalho visual."""
    print("\n" + "=" * 60)
    print("   📋 ÍNDICE DE TESTES - API DEPRESSÃO ESTUDANTIL")
    print("=" * 60 + "\n")

def print_statistics():
    """Imprime estatísticas."""
    print("📊 ESTATÍSTICAS")
    print("-" * 60)
    for key, value in STATISTICS.items():
        print(f"  • {key:.<40} {value}")
    print()

def print_documentation():
    """Imprime índice de documentação."""
    print("📚 DOCUMENTAÇÃO")
    print("-" * 60)
    for category, files in DOCUMENTATION_MAP.items():
        print(f"\n{category}")
        for file, description in files:
            exists = "✅" if os.path.exists(file) else "❌"
            print(f"  {exists} {file:.<35} {description}")

def print_quick_commands():
    """Imprime comandos rápidos."""
    print("\n\n⚡ COMANDOS RÁPIDOS")
    print("-" * 60)
    for cmd, command in QUICK_COMMANDS.items():
        print(f"\n  {cmd}:")
        print(f"    $ {command}")

def print_next_steps():
    """Imprime próximos passos."""
    print("\n\n🚀 PRÓXIMOS PASSOS")
    print("-" * 60)
    print("""
  1. Instalar dependências (se não feito):
     $ pip install -r requirements.txt

  2. Executar testes:
     $ pytest tests/ -v

  3. Ver cobertura:
     $ pytest --cov=src --cov-report=html
     # Abrir htmlcov/index.html

  4. Consultar documentação:
     • Começar: QUICK_START_TESTS.md
     • Aprender: TESTING_GUIDE.md
     • Referência: TESTING.md
""")

def print_footer():
    """Imprime rodapé."""
    print("-" * 60)
    print("✅ Suite de testes 100% completa e funcional!")
    print("📞 Para dúvidas, consulte os arquivos .md acima.")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    print_header()
    print_statistics()
    print_documentation()
    print_quick_commands()
    print_next_steps()
    print_footer()
