<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="static/img/favicon.ico" />
    <title>Crud de usuário</title>
    <link rel="stylesheet" type="text/css" href="/static/css/create.css">
    <script src="/static/js/create.js" defer></script>
</head>
<body>
  <h1>Seja bem-vindo ao BMVC! (Bottle Powered)</h1>
  <h4>Cadastre seu nome ou apelido e uma senha numérica de acesso com 6 dígitos:</h4>
    <form action="/create" method="post">
      <label for="username">Nome:</label>
      <input id="username" name="username" type="text" required /><br>
      <label for="password">Senha:</label>
      <input id="password" name="password" type="password" required /><br>
    </br>
      <div class= "button-container">
        <input value="Criar" type="submit" />
      </div>
    </form>
    <form action="/portal" method="post">
      <button type="submit">Portal</button>
    </form>
</body>
</html>
