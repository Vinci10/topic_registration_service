class NoStudentError(Exception):
    """Exception raised during registration topic for user different than student"""
    pass


class OccupiedTopicError(Exception):
    """Exception raised during registration on occupied topic"""
    pass


class RegistrationClosedError(Exception):
    pass
