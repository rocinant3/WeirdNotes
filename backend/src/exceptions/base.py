
class BaseExceptionCase(Exception):
    def __init__(self, status_code: int, context: str = None):
        self.exception_case = self.__class__.__name__
        self.status_code = status_code
        self.context = context

    def __str__(self):
        return (
            f"<BaseException {self.exception_case} - "
            + f"status_code={self.status_code} - context={self.context}>"
        )
