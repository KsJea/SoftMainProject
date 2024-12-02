# models.py  
class User:  
    def __init__(self, username, password, email, role):  
        self.username = username  
        self.password = password  
        self.email = email  
        self.role = role  

# Simulación de usuarios en memoria  
users = {  
    "admin": User(username="admin", password="adminpass", email="admin@example.com", role="admin"),  
    "user1": User(username="user1", password="userpass", email="user1@example.com", role="user"),  
    "user2": User(username="user2", password="userpass", email="user2@example.com", role="user"),  
}