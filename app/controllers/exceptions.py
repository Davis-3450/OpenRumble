from app.utils.exceptions import BaseExcepciption


class BaseControllerException(BaseExcepciption):
    """Base exception for controller errors."""

    pass


class ControllerNotFound(BaseControllerException):
    """Exception raised when a controller is not found."""

    pass
