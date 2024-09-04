<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="static/img/favicon.ico" />
    <title>cRud de usuário</title>
    <link rel="stylesheet" type="text/css" href="/static/css/pagina.css">
    <script src="/static/js/pagina.js"></script>
</head>
<body>
    % if transfered:
        <h1>Seja bem vindo :)</h1>
        <div>
            <h2>Dados do Usuário:</h2>
            <p>Username: {{current_user.username}} </p>
            <p>Password: {{current_user.password}} </p>
            <div class= "button-container">
                <form action="/logout" method="post">
                    <button type="submit">Logout</button>
                </form>
                <form action="/edit" method="get">
                    <button type="submit">Editar usuário</button>
                </form>
                <form action="/chat" method="get">
                    <button type="submit">Área de mensagens</button>
                </form>
                <form action="/portal" method="get">
                    <button type="submit">Portal</button>
                </form>
                <form action="/admin" method="get">
                    <button type="submit">Administração</button>
                </form>
            </div>
        </div>
    % else:
        <h1>Página reservada!</h1>
        <h3>Realize seu LOGIN em nosso portal</h3>
        <form action="/portal" method="get">
          <button type="submit">Portal</button>
        </form>
    % end
</body>
</html>
