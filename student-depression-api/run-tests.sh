#!/bin/bash
# Script para executar testes e gerar relatórios
# Usage: ./run-tests.sh [option]

set -e

cd "$(dirname "$0")"

echo "╔════════════════════════════════════════════════════════════╗"
echo "║     API DEPRESSÃO ESTUDANTIL - SUITE DE TESTES            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

case "${1:-all}" in
  all)
    echo "🧪 Executando todos os testes..."
    python -m pytest tests/ -v --tb=short
    ;;
  
  quick)
    echo "⚡ Teste rápido (sem relatório)..."
    python -m pytest tests/ -q
    ;;
  
  coverage)
    echo "📊 Teste com relatório de cobertura (terminal)..."
    python -m pytest tests/ --cov=src --cov-report=term-missing
    ;;
  
  html)
    echo "📄 Gerando relatório HTML..."
    python -m pytest tests/ --cov=src --cov-report=html
    echo "✅ Relatório gerado em: htmlcov/index.html"
    ;;
  
  specific)
    if [ -z "$2" ]; then
      echo "❌ Especifique o teste: ./run-tests.sh specific test_main.py"
      exit 1
    fi
    echo "🎯 Executando teste específico: $2"
    python -m pytest "tests/$2" -v
    ;;
  
  *)
    echo "Uso: ./run-tests.sh [opção]"
    echo ""
    echo "Opções:"
    echo "  all       - Todos os testes (padrão)"
    echo "  quick     - Teste rápido"
    echo "  coverage  - Com relatório de cobertura"
    echo "  html      - Relatório HTML interativo"
    echo "  specific  - Teste específico (ex: specific test_main.py)"
    echo ""
    echo "Exemplos:"
    echo "  ./run-tests.sh"
    echo "  ./run-tests.sh quick"
    echo "  ./run-tests.sh coverage"
    echo "  ./run-tests.sh html"
    exit 1
    ;;
esac
