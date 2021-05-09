from enum import unique, Enum

@unique
class UserRole(Enum):
    PRODUCING_MANAGER = 1
    STORAGE_MANAGER = 2
    FOREMAN = 3
    DIRECTOR = 4