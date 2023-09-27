class LoginToken:
    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role

    def __str__(self):
        return f"LoginToken: id={self.id}, name={self.name}, role={self.role}"
