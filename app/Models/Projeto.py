class Project:
    def __init__(self, name, desc, status=None, start_date=None, end_date=None, id_project=None, owner_id=None):
        self._id_project = id_project
        self._name = name
        self._desc = desc
        self._status = status
        self._start_date = start_date
        self._end_date = end_date
        self._owner_id = owner_id

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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
