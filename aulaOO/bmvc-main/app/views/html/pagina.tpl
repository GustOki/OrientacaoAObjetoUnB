<!DOCTYPE html>
<html lang="pt-BR">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Minha primeira página com o BMVC</title>
   <link rel="stylesheet" type="text/css" href="static/css/application.css">
   <link rel="stylesheet" type="text/css" href="static/css/pagina.css">
   <script src="../../static/js/pagina.js"></script>

</head>
<body>

   <h1>Olá! Esta é a minha primeira página com o BMVC :)</h1>

</body>
</html>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha segunda página com o BMVC</title>
</head>
<body>

    <h1>Minha página com interação de modelos :)</h1>

    simbolo-% if transfered:
        <div>
            <h2>Dados do Usuário:</h2>
            <p>Username: chaves-duplas data.username chaves-duplas </p>
            <p>Password: chaves-duplas data.password chaves-duplas </p>
        </div>
    simbolo-% else:
        <h2>Porém, desta vez não foram transferidas quaisquer informações ): </h2>
    simbolo-% end

</body>
</html>