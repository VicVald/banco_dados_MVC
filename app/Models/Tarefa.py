class Task:
    def __init__(self, id_task, id_member, id_project, name, desc, state):
        self._id_task = id_task
        self._id_member = id_member
        self._id_project = id_project
        self._name = name
        self._desc = desc
        self._state = state

    @property
    def id_task(self):
        return self._id_task

    @id_task.setter
    def id_task(self, value):
        self._id_task = value

    @property
    def id_member(self):
        return self._id_member

    @id_member.setter
    def id_member(self, value):
        self._id_member = value

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

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
