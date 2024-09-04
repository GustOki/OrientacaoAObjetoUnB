from app.models.user_account import UserAccount
from app.models.user_message import UserMessage
import json
import uuid


class MessageRecord():
    """Banco de dados JSON para o recurso: Mensagem"""

    def __init__(self):
        self.__user_messages= []
        self.read()


    def read(self):
        try:
            with open("app/controllers/db/user_messages.json", "r") as fjson:
                user_msg = json.load(fjson)
                self.__user_messages = [UserMessage(**msg) for msg in user_msg]
        except FileNotFoundError:
            print('Não existem mensagens registradas!')


    def __write(self):
        try:
            with open("app/controllers/db/user_messages.json", "w") as fjson:
                user_msg = [vars(user_msg) for user_msg in \
                self.__user_messages]
                json.dump(user_msg, fjson)
                print(f'Arquivo gravado com sucesso (Mensagem)!')
        except FileNotFoundError:
            print('O sistema não conseguiu gravar o arquivo (Mensagem)!')


    def book(self,username,content):
        new_msg= UserMessage(username,content)
        self.__user_messages.append(new_msg)
        self.__write()
        return new_msg


    def getUsersMessages(self):
        return self.__user_messages


# ------------------------------------------------------------------------------

class UserRecord():
    """Banco de dados JSON para o recurso: Usuário"""

    def __init__(self):
        self.__user_accounts= []
        self.__authenticated_users = {}
        self.read()


    def read(self):
        try:
            with open("app/controllers/db/user_accounts.json", "r") as fjson:
                user_d = json.load(fjson)
                self.__user_accounts = [UserAccount(**data) for data in user_d]
        except FileNotFoundError:
            self.__user_accounts.append(UserAccount('Guest', '000000'))


    def __write(self):
        try:
            with open("app/controllers/db/user_accounts.json", "w") as fjson:
                user_data = [vars(user_account) for user_account in \
                self.__user_accounts]
                json.dump(user_data, fjson)
                print(f'Arquivo gravado com sucesso (Usuário)!')
        except FileNotFoundError:
            print('O sistema não conseguiu gravar o arquivo (Usuário)!')


    def setUser(self,username,password):
        for user in self.__user_accounts:
            if username == user.username:
                user.password= password
                print(f'O usuário {username} foi editado com sucesso.')
                self.__write()
                return username
        else:
            print(f'O usuário {username} não foi identificado!')
            return None


    def removeUser(self,user):
        if user in self.__user_accounts:
            print(f'O usuário {user.username} foi encontrado no cadastro.')
            self.__user_accounts.remove(user)
            print(f'O usuário {user.username} foi removido do cadastro.')
            self.__write()
            return user.username
        print(f'O usuário {user.username} não foi identificado!')
        return None


    def book(self,username,password):
        new_user= UserAccount(username,password)
        self.__user_accounts.append(new_user)
        self.__write()
        return new_user.username


    def getCurrentUser(self,session_id):
        if session_id in self.__authenticated_users:
            return self.__authenticated_users[session_id]
        else:
            return None


    def getAuthenticatedUsers(self):
        return self.__authenticated_users


    def checkUser(self, username, password):
        for user in self.__user_accounts:
            if user.username == username and user.password == password:
                session_id = str(uuid.uuid4())  # Gera um ID de sessão único
                self.__authenticated_users[session_id] = user
                return session_id  # Retorna o ID de sessão para o usuário
        return None


    def logout(self, session_id):
        if session_id in self.__authenticated_users:
            del self.__authenticated_users[session_id] # Remove o usuário logado
