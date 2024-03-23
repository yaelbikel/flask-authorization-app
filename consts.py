import enum

class Role(enum.Enum):
    ADMIN = "ADMIN"
    USER = "USER"

class Permission(enum.Enum):
    OWNER = "OWNER"
    VIEW = "VIEW"
    COMMENT = "COMMENT"
    EDIT = "EDIT"

# dummy data

users = {
    "user1": {"password": "adminpass", "role": Role.ADMIN},
    "user2": {"password": "userpass", "role": Role.USER}
}

files = {
    "file1": {"permissions": {"user1": [Permission.OWNER]}},
    "file2": {"permissions": {"user2": [Permission.OWNER], "user1": [Permission.VIEW]}}
}
