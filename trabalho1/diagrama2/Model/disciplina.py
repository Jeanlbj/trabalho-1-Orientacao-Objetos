class Disciplina:

    def __init__(self) -> None:
        self.__id = 1
        self.__descricao = ""
        self.__curso = ""
        self.__listaTurma = []

    def setId(self, id: int) -> None:
        self.__id = id

    def getId(self) -> int:
        return self.__id
    
    def setDescricao(self, descricao: str) -> None:
        self.__descricao = descricao

    def getDescricao(self) -> str:
        return self.__descricao
    
    def setCurso(self, curso) -> None:
        self.__curso = curso

    def getCurso(self) -> None:
        return self.__curso
    
    def setListaTurma(self, turma) -> None:
        self.__listaTurma = turma

    def addListaTurma(self, turma) -> None:
        self.__listaTurma.append(turma)

    def removerListaTurma(self, turma) -> None:
        self.__listaTurma.remove(turma)

    def getListaTurma(self) -> None:
        return self.__listaTurma
    
    def __str__(self) -> None:
        return f"ID: {self.getId()}\nDescrição: {self.getDescricao()}\n" \
               f"Curso: {self.getCurso()}\nTurma(s): {self.getListaTurma()}"
    
    