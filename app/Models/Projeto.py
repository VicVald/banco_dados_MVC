class Project:
    def __init__(self, id_project, name, desc):
        self._id_project = id_project
        self._name = name
        self._desc = desc

    @property
    def id_project(self):
        return self._id_project

    @id_project.setter
    def id_project(self, value):
        self._id_project = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
