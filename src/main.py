import os
import json
from openpyxl import Workbook


def criar_projeto(nome_projeto):
    caminho = f"data/{nome_projeto}"

    os.makedirs(caminho, exist_ok=True)
    os.makedirs(f"{caminho}/comprovantes", exist_ok=True)

    return caminho


def extrair_requisitos(texto):
    linhas = texto.split("\n")
    requisitos = [linha.strip() for linha in linhas if linha.strip()]
    return requisitos


def montar_estrutura(requisitos):
    estrutura = []

    for req in requisitos:
        item = {
            "requisito": req,
            "pagina": "",
            "documento": "",
            "link": "",
            "termos": "",
            "status": ""
        }
        estrutura.append(item)

    return estrutura


def salvar_json(caminho, dados):
    with open(f"{caminho}/requisitos.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def salvar_edital(caminho, texto):
    with open(f"{caminho}/edital.txt", "w", encoding="utf-8") as f:
        f.write(texto)


def gerar_excel(caminho, estrutura):
    wb = Workbook()
    ws = wb.active
    ws.title = "Checklist"

    # Cabeçalho
    ws.append([
        "Requisito",
        "Página",
        "Documento",
        "Link",
        "Termos de Busca",
        "Status"
    ])

    # Dados
    for item in estrutura:
        ws.append([
            item["requisito"],
            item["pagina"],
            item["documento"],
            item["link"],
            item["termos"],
            item["status"]
        ])

    arquivo = f"{caminho}/checklist.xlsx"
    wb.save(arquivo)

    return arquivo


def main():
    print("=== Presales Helper ===")

    nome_projeto = input("Nome do projeto: ").strip()
    caminho = criar_projeto(nome_projeto)

    print("\nCole os requisitos (ENTER + linha vazia para finalizar):")

    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha)

    texto = "\n".join(linhas)

    requisitos = extrair_requisitos(texto)
    estrutura = montar_estrutura(requisitos)

    salvar_edital(caminho, texto)
    salvar_json(caminho, estrutura)

    arquivo_excel = gerar_excel(caminho, estrutura)

    print(f"\nProjeto '{nome_projeto}' criado com sucesso!")
    print(f"Dados salvos em: {caminho}")
    print(f"Excel gerado em: {arquivo_excel}")


if __name__ == "__main__":
    main()
