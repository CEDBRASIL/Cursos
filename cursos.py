from fastapi import HTTPException

# cursos.py

"""
Mapeamento dos cursos e seus respectivos IDs de disciplinas na Ouro Moderno (OM).

Use este dicionário para vincular cursos e disciplinas nas matrículas automáticas.
"""

CURSOS_OM = {
    "Excel PRO": [161, 197, 201],
    "Design Gráfico": [254, 751, 169],
    "Analista e Desenvolvimento de Sistemas": [590, 176, 239, 203],
    "Administração": [129, 198, 156, 154],
    "Inglês Fluente": [263, 280, 281],
    "Inglês Kids": [266],
    "Informática Essencial": [130, 599, 161, 160, 162],
    "Operador de Micro": [130, 599, 160, 161, 162, 163, 222],
    "Especialista em Marketing & Vendas 360º": [123, 199, 202, 236, 264, 441, 734, 780, 828, 829],
    "Marketing Digital": [734, 236, 441, 199, 780],
    "Pacote Office": [160, 161, 162, 197, 201],
}

def listar_cursos():
    """Retorna uma lista formatada dos cursos disponíveis para exibir ao aluno."""
    linhas = []
    for curso, ids in CURSOS_OM.items():
        linhas.append(f"{curso} (ID das disciplinas: {', '.join(map(str, ids))})")
    return "\n".join(linhas)

if __name__ == "__main__":
    print("Cursos disponíveis para matrícula:\n")
    print(listar_cursos())


@app.get("/secure")
async def renovar_token():
    try:
        token = _obter_token_unidade()
        _log("🔄 Token renovado com sucesso via /secure")
        return {"status": "ok", "token": token}
    except Exception as e:
        _log(f"❌ Falha ao renovar token: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao renovar token: {str(e)}")
