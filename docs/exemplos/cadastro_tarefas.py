"""Código didático para ilustrar a especificação e a revisão do catálogo."""


def validar_titulo(titulo):
    if not isinstance(titulo, str) or not titulo.strip():
        raise ValueError("Informe um título não vazio.")
    return titulo.strip()


def adicionar_tarefa(titulo, tarefas):
    titulo_validado = validar_titulo(titulo)
    tarefa = {"titulo": titulo_validado, "concluida": False}
    tarefas.append(tarefa)
    return tarefa
