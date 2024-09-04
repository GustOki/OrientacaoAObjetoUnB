<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="static/img/favicon.ico" />
    <title>cruD de usuário</title>
    <link rel="stylesheet" type="text/css" href="/static/css/delete.css">
    <script src="/static/js/delete.js"></script>
</head>
<body>
    % if user:
        <h1>Página de remoção de Usuários:</h1>
        <h4>Usuário logado: {{ user.username }} </h4>
        <form action="/delete" method="post">
        </br>
          <div class= "button-container">
            <input value="Remover" type="submit" />
            <form action="/logout" method="post">
              <button type="submit">Logout</button>
            </form>
            <form action="/portal" method="get">
              <button type="submit">Portal</button>
            </form>
          </div>
        </form>
    % else:
      <h1>Página reservada!</h1>
      <h3>Realize seu LOGIN em nosso portal</h3>
      <form action="/portal" method="get">
        <button type="submit">Portal</button>
      </form>
    % end
</body>
</html>
