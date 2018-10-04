class VKObject(object):

    def __init__(self, object_data):

        if not isinstance(object_data, dict):
            return

        self.object_data = object_data
        for key, value in object_data.items():
            if isinstance(value, (list, tuple)):
                setattr(self, key, [VKObject(item) if isinstance(item, dict) else item for item in value])
            else:
                setattr(self, key, VKObject(value) if isinstance(value, dict) else value)

    def to_dict(self):

        if not isinstance(self.object_data, dict):
            return

        return self.object_data
