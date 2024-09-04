<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="static/img/favicon.ico" />
    <title>Chat</title>
    <link rel="stylesheet" type="text/css" href="/static/css/chat.css">
    <script src="/static/js/websocket/socket.io.min.js"></script>
    <script src="/static/js/chat.js" defer></script>
</head>
<body>
    <h1>{{current_user.username}}, experiemente este Chat em tempo real :)</h1>
    <h4>Os usuários conectados aparecerão abaixo:</h4>
    <div id="usersDisplay">
       % for user in auth_users:
          <li>{{user.username}}</li>
       % end
    </div>
    </br>
    <input type="text" id="messageInput" placeholder="Digite sua mensagem">
    <button id="sendButton">Enviar</button>
    <h2>Mensagens anteriores:</h2>
    <div id="messageDisplay">
        % for message in messages:
            <li>{{message.content}} | escrita por: {{message.username}}</li>
        % end
    </div>
  </br>
    <form action="/portal" method="get">
        <button type="submit">Portal</button>
    </form>
</body>
</html>
