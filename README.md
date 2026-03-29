# Presales Helper

## 📌 Descrição
O Presales Helper é uma ferramenta em linha de comando (CLI) que auxilia profissionais de pré-vendas e licitação na análise de editais técnicos. A aplicação permite transformar requisitos de um edital em um checklist estruturado, facilitando a validação de conformidade técnica.

---

## ❗ Problema
A análise de editais técnicos é um processo manual, demorado e suscetível a erros, podendo levar à perda de prazos ou desclassificação em licitações.

---

## 💡 Solução
A aplicação permite:
- Inserir requisitos de edital manualmente
- Estruturar automaticamente os requisitos
- Gerar um checklist organizado
- Exportar os dados para Excel

---

## 👥 Público-alvo
- Profissionais de pré-vendas
- Analistas de licitação
- Empresas que participam de pregões

---

## ⚙️ Funcionalidades
- Criação de projetos por edital
- Extração de requisitos a partir de texto
- Estruturação em formato padrão
- Geração de arquivo JSON
- Exportação automática para Excel (.xlsx)

---

## 🛠 Tecnologias utilizadas
- Python 3
- openpyxl
- pytest
- ruff
- GitHub Actions

---

## 📦 Instalação

```bash
git clone https://github.com/SEU_USUARIO/Presales_Helper.git
cd Presales_Helper
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
