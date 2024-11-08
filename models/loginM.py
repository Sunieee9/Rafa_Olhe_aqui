class Login:
    # Construtor da classe Login, inicializando com usuário e senha
    def __init__(self, usuario, senha):
        self.usuario = usuario  # Armazena o nome de usuário
        self.senha = senha      # Armazena a senha do usuário

    # Método para validar o nome de usuário e a senha
    def validate(self, username, password):
        # Retorna True se o nome de usuário e a senha passados coincidem com os armazenados
        return self.usuario == username and self.senha == password
