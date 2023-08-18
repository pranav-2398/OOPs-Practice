class Tablet:
    models = {('lite', 32, 2), ('pro', 64, 3), ('max', 128, 4)}

    def __init__(self, model):
        self.model = model

    def __repr__(self):
        return (f"Tablet(Model = {self.model}, Base_Storage = {self.base_storage}, "
                f"Added_Storage = {self.added_storage}, Memory = {self.memory}) ")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if list(filter(lambda z: z[0] == model, self.models)):
            filtered_model = list(filter(lambda z: z[0] == model, self.models))[0]
            self._base_storage = filtered_model[1]
            self._memory = filtered_model[2]
            self._model = model
            self.added_storage = 0

        else:
            raise ValueError("Correct Model is not given as input")

    @property
    def base_storage(self):
        return self._base_storage

    @property
    def memory(self):
        return self._memory

    def add_storage(self, storage):
        if storage + self.added_storage + self.base_storage > 1024:
            raise Exception("Total Storage cannot exceed 1024 GB")

        else:
            self.added_storage += storage

    @property
    def storage(self):
        return self.base_storage + self.added_storage

    @storage.setter
    def storage(self, storage):
        if storage > 1024:
            raise Exception("Total Storage cannot exceed 1024 GB")

        else:
            self.added_storage = storage - self.base_storage
