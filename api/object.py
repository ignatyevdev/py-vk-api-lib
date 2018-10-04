class VKObject(object):

    def __init__(self, data):

        if not isinstance(data, dict):
            return

        self.dict = data
        for key, value in data.items():
            if isinstance(value, (list, tuple)):
                setattr(self, key, [VKObject(item) if isinstance(item, dict) else item for item in value])
            else:
                setattr(self, key, VKObject(value) if isinstance(value, dict) else value)

    def to_dict(self):

        if not isinstance(self.dict, dict):
            return

        return self.dict
