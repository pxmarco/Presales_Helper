# Presales Helper

## 📌 Descrição
O Presales Helper é uma ferramenta em linha de comando (CLI) que auxilia profissionais de pré-vendas e licitação na análise de editais técnicos. A aplicação permite transformar requisitos de um edital em um checklist estruturado, agilizando a criação da estrutura do documento utilizado para validação e confirmação técnica.

---

## ❗ Problema
Alguns editais de licitação em TI costumam ter inúmeras linhas de requisitos, tornando difícil a vida dos profissionais que trabalham com a análise dos requisitos técnicos, sendo um processo manual, demorado e suscetível a erros, podendo levar à perda de prazos ou desclassificação em licitações.

---

## 💡 Solução
A aplicação permite:
- Copiar/colar os requisitos de edital manualmente (nesta primeira etapa não tem uma integração com API ou automatização da leitura do PDF, logo, o indicado é editar os requisitos em .txt, no bloco de notas, e depois colar no sistema)
- Automatizar a estrutura de comprovação dos requisitos
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
winget install --id Git.Git -e --source winget  #Se não tiver o git instalado no seu windows
git clone https://github.com/pxmarco/Presales_Helper.git
cd Presales_Helper
python3 -m venv .venv
source .venv/bin/activate  #Linux
.venv\Scripts\activate     #Windows
pip install -r requirements.txt
```

---

## ▶️ Executar o sistema

```bash
python src/main.py
```

---

## ✏️ Como usar na prática
- Digite o nome do projeto
- Cole os requisitos do edital (exemplo abaixo)
- Pressione ENTER em uma linha vazia para finalizar

---

## 📊 Resultado

O sistema irá gerar automaticamente:

data/nome_do_projeto/ <br>
├── edital.txt          → texto original <br>
├── requisitos.json     → estrutura dos requisitos <br>
├── checklist.xlsx      → checklist pronto <br>
└── comprovantes/       → pasta para documentos <br>

---

## 🧪 Testes automatizados e Lint

Para validar o funcionamento do sistema:

```bash
PYTHONPATH=. pytest
```

Para verificar padrões e possíveis problemas no código:

```bash
ruff check .
```

---

## 🔄 Integração Contínua (CI)

Assim que for preenchendo os requisitos, escreva:

```bash
git add .
git commit -m "Atualizações"
git push
```
