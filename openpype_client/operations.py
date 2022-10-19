import re
from openpype.client.operations_base import BaseOperationsSession


PROJECT_NAME_ALLOWED_SYMBOLS = "a-zA-Z0-9_"
PROJECT_NAME_REGEX = re.compile(
    "^[{}]+$".format(PROJECT_NAME_ALLOWED_SYMBOLS)
)


class OperationsSession(BaseOperationsSession):
    def commit(self):
        raise NotImplementedError(
            "{} dose not have implemented 'commit'".format(
                self.__class__.__name__))


def create_project(*args, **kwargs):
    raise NotImplementedError("'create_project' not implemented")
