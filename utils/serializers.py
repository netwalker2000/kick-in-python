from abc import abstractmethod


class BaseSerializer(object):
    @abstractmethod
    def convert_to_dict(self, model):
        pass
