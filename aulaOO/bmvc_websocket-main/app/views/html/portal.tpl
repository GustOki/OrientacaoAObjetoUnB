<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="static/img/favicon.ico" />
    <title>>.::Portal (Login)::.</title>
    <link rel="stylesheet" type="text/css" href="/static/css/portal.css">
    <script src="/static/js/portal.js"></script>
</head>
<body>
    <div class= "object_centered">
      <h1>Seja bem-vindo ao BMVCh@t!</h1>
      <h4>Estrutura desenvolvida para oferecer suporte ao desenvolvimento FullStack da disciplina de Orientação a Objetos (Henrique Moura - 01/2024).</h4>
      <img src="{{'static/img/BottleLogo.png'}}" alt="Descrição da Imagem"
         width="300" height="300" onclick="displayText()">
    </div>
    <h1>Login</h1>
    % if username:
      <div class= "object_centered">
        % if edited:
            <h4>Usuário logado: {{ username }} (editado) </h4>
        % else:
            <h4>Usuário logado: {{ username }} </h4>
        % end
          <form action="/logout" method="post">
              <button type="submit">Logout</button>
          </form>
          <form action="/edit" method="get">
              <button type="submit">Área de usuário</button>
          </form>
          <form action="/chat" method="get">
              <button type="submit">Área de mensagens</button>
          </form>
      </div>
    % else:
        % if removed is not None:
            <h4>O usuário {{ removed }} foi removido deste cadastro.</h4>
        % elif created is not None:
            <h4>O usuário {{ created }} foi criado neste cadastro.</h4>
        % end
        <div class= "object_centered">
          <form action="/portal" method="post">
              <label for="username">Nome:</label>
              <input id="username" name="username" type="text" required /><br>
              <label for="password">Senha:</label>
              <input id="password" name="password" type="password" required /><br>
              </br>
              <input id="setUsers" value="Login" type="submit" />
          </form>
          <form action="/create" method="get">
              <button type="submit">Criar conta de usuário</button>
          </form>
        </div>
    % end
</body>
</html>
