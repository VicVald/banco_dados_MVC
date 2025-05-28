class Participante:
    def __init__(self, id_user, id_project, funcao, inicio, id_part=None):
        self._id_part = id_part
        self._id_user = id_user
        self._id_project = id_project
        self._funcao = funcao
        self._data_inicio = inicio

    @property
    def id_part(self):
        return self._id_part

    @id_part.setter
    def id_part(self, value):
        self._id_part = value

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, value):
        self._id_user = value

    @property
    def id_project(self):
        return self._id_project

    @id_project.setter
    def id_project(self, value):
        self._id_project = value

    @property
    def funcao(self):
        return self._funcao

    @funcao.setter
    def funcao(self, value):
        self._funcao = value

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, value):
        self._data_inicio = value
