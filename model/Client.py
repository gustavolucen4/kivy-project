class Client:
    __slots__ = (
        '_id',
        '_treatmentStatus',
        '_gender',
        '_age',
        '_race',
        '_employmentStatus',
        '_mentalHealthDiagnosis',
        '_substanceUseDiagnosis'
    )

    def __init__(self, id=None, treatmentStatus="", gender="", age="", race="", employmentStatus="", mentalHealthDiagnosis="", substanceUseDiagnosis=""):
        self._id = id
        self._treatmentStatus = treatmentStatus
        self._gender = gender
        self._age = age
        self._race = race
        self._employmentStatus = employmentStatus
        self._mentalHealthDiagnosis = mentalHealthDiagnosis
        self._substanceUseDiagnosis = substanceUseDiagnosis

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, idClient):
        self._id = idClient

    @property
    def treatmentStatus(self):
        return self._treatmentStatus

    @treatmentStatus.setter
    def treatmentStatus(self, treatmentStatus):
        self._treatmentStatus = treatmentStatus

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, race):
        self._race = race

    @property
    def employmentStatus(self):
        return self._employmentStatus

    @employmentStatus.setter
    def gender(self, employmentStatus):
        self._employmentStatus = employmentStatus

    @property
    def mentalHealthDiagnosis(self):
        return self._mentalHealthDiagnosis

    @gender.setter
    def mentalHealthDiagnosis(self, mentalHealthDiagnosis):
        self._mentalHealthDiagnosis = mentalHealthDiagnosis

    @property
    def substanceUseDiagnosis(self):
        return self._substanceUseDiagnosis

    @gender.setter
    def gender(self, substanceUseDiagnosis):
        self._substanceUseDiagnosis = substanceUseDiagnosis
