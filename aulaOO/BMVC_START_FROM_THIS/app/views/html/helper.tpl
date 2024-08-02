<!DOCTYPE html>

<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>.::Bem-vindo ao BMVC::.</title>
    <link rel="stylesheet" type="text/css" href="static/css/helper.css">
    <script src="../../static/js/helper.js"></script>
</head>

<body>

    <div class= "object_centered">
      <h1>Seja bem-vindo ao BMVC! (Bottle Powered)</h1>
      <h4>Estrutura desenvolvida para oferecer suporte ao desenvolvimento FullStack da disciplina de Orientação a Objetos.</h4>
      <img src="{{'static/img/BottleLogo.png'}}" alt="Descrição da Imagem"
          width="300" height="300" onclick="displayText()">
      <h4>H.G.M.</h4>
    </div>

    <div class="object_centered">
         <h3>Para inserir uma página (HTML ou TPL):</h3>
         <h4 class="justify-text">Defina uma rota (HTTP: GET) no arquivo route.py, tal como indicado a seguir:</h4>
         <pre class="code-block"><code>

@app.route('/pagina', methods=['GET'])
def action_pagina():
    return ctl.render('pagina')

         </code></pre>

         <h4 class="justify-text">Escreva o arquivo 'pagina.tpl' ou 'pagina.html' e o coloque na pasta 'app/views/html/'. Em seguida, insira os arquivos estáticos necessários nas pastas correpondentes (/css,/js,/img), existentes na pasta "app/static".
           Carregue-os na página em questão, inserindo linhas semelhantes às mostradas a seguir.</h4>
         <pre class="code-block"><code>

&lt;!DOCTYPE html&gt;
&lt;html lang="pt-BR"&gt;
&lt;head&gt;
   &lt;meta charset="UTF-8"&gt;
   &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
   &lt;title&gt;Minha primeira página com o BMVC&lt;/title&gt;
   &lt;link rel=&quot;stylesheet&quot; type=&quot;text/css&quot; href=&quot;static/css/application.css&quot;&gt;

   &lt;link rel=&quot;stylesheet&quot; type=&quot;text/css&quot; href=&quot;static/css/pagina.css&quot;&gt;
   &lt;script src=&quot;../../static/js/pagina.js&quot;&gt;&lt;/script&gt;

&lt;/head&gt;
&lt;body&gt;

   &lt;h1&gt;Minha página com interação de modelos :)&lt;/h1&gt;

   simbolo-% if transfered:
       &lt;div&gt;
           &lt;h2&gt;Dados do Usuário:&lt;/h2&gt;
           &lt;p&gt;Username: chaves-duplas data.username chaves-duplas &lt;/p&gt;
           &lt;p&gt;Password: chaves-duplas data.password chaves-duplas &lt;/p&gt;
       &lt;/div&gt;
   simbolo-% else:
       &lt;h2&gt;Porém, desta vez não foram transferidas quaisquer informações ): &lt;/h2&gt;
   simbolo-% end

&lt;/body&gt;
&lt;/html&gt;

        </code></pre>

        <h4 class="justify-text">Edite o controlador Application (arquivo: application.py) para conter um método de administração
          dpara o conteúdo apresentado em '/pagina'.</h4>
          <pre class="code-block"><code>

def pagina(self):
    # seu código complementar aqui
    return template('app/views/html/pagina')

          </code></pre>

          <h4 class="justify-text">Não deixe de editar o dicionário 'self.pages' com a nova alternativa para a rota inserida.</h4>
          <pre class="code-block"><code>
(...)

self.pages = {
    (...)
    'pagina': self.pagina,
    (...)
}
(...)
          </code></pre>

     </div>

     <div class="object_centered">
          <h3>Para inserir um modelo e acessá-lo em uma das página:</h3>
          <h4 class="justify-text">Todos os modelos deverão ser alocados na pasta 'app/models', em arquivos separados, com extensão '.py' - neste exemplo: 'user_account.py'. O modelo utilizado, neste exemplo, se encontra a seguir:
          </h4>
          <pre class="code-block"><code>

class UserAccount():
    def __init__(self, username, password):
        self.username= username
        self.password= password

          </code></pre>
          <h4 class="justify-text">Defina uma infraestrutura para armazenar seu(s) modelo em um disco (banco de dados). Esta infraestrutura deve ser organziada
            dentro da pasta 'app/controllers/db'. Talvez seja interessante que você defina uma 'classe administradora' para o seu banco de dados, para que você possa acessar
            seus modelos com praticidade e segurança. Veja o exemplo a seguir da classe administradora 'DataRecord':
          </h4>
          <pre class="code-block"><code>

from app.models.user_account import UserAccount
import json

class DataRecord():
    """Banco de dados JSON para o recurso Usuários"""

    def __init__(self):
        self.user_accounts= [] # banco (json)
        try:
            with open("app/controllers/db/user_accounts.json", "r") as arquivo_json:
            user_data = json.load(arquivo_json)
            self.user_accounts = [UserAccount(**data) for data in user_data]
            self.limit = len(self.user_accounts) - 1  # Definindo o limite com base no número de contas de usuário
        except FileNotFoundError:
            self.user_accounts.append(UserAccount('Guest', '000000'))
            self.limit = len(self.user_accounts) - 1  # Definindo o limite como 0 no caso de nenhum arquivo encontrado


    def work_with_parameter(self, parameter):
        try:
            index = int(parameter)  # Convertendo o parâmetro para inteiro
            if index <= self.limit:
                return self.user_accounts[index]
        except (ValueError, IndexError):
            return None  # Tratamento de erro se o índice for inválido

          </code></pre>
          <h4 class="justify-text">A classe 'DataRecord' deve ser colocada na pasta 'app/controllers/', no arquivo 'datarecord.py'. Como se pode ver,
            a classe DataRecord executa, em seu construtor, a leitura de um arquivo JSON: user_accounts. Este arquivo, está convenientemente alocado na pasta 'app/controllers/db'.
            Temos um conteúdo básico para este arquivo, a seguir.
          </h4>
          <pre class="code-block"><code>

[{"username": "Henrique", "password": "123456"},{"username": "Moura", "password": "456789"}]

          </code></pre>
          <h4 class="justify-text">Em seguida, realize uma composição de um objeto DataRecord dentro da Application (Application -> Datarecord), no ato de sua construção - este objeto/atributo
            será tratado por: 'self.models'. Ainda dentro da classe Application, insira seu processamento de dados (tratamento do modelo) na action desejada e transmita as informações através
            da função template, tal como indicado a seguir:
          </h4>
          <pre class="code-block"><code>
(...)

class Application():

    def __init__(self):

        self.pages = {
        'pagina': self.pagina
        }

        self.models= DataRecord()

(...)

    def render(self,page,parameter=None):
        content = self.pages.get(page, self.helper)
        if not parameter:
            return content()
        else:
            return content(parameter)

(...)

    def pagina(self,parameter=None):
        if not parameter:
            return template('app/views/html/pagina',transfered= False)
        else:
            info = self.models.work_with_parameter(parameter)
            if not info:
               redirect('/pagina')
            else:
               return template('app/views/html/pagina',transfered= True, data=info)

          </code></pre>

          <h4 class="justify-text">No código acima, o parametro passado para action deve ser transmitido pela rota ou action específica. Com este parâmetro, o objeto 'self.models' poderá
            manipular os modelos e entregar as informações requeridas para a pagina, através da variável data. Lembre-se de importa a classe DataRecord no seu arquivo 'application.py'. Manipule a variável 'data' no arquivo TPL em forma de código comum, estabelecido
            tal como no exemplo a seguir:
          </h4>
          <pre class="code-block"><code>

&lt;!DOCTYPE html&gt;
&lt;html lang="pt-BR"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Minha segunda página com o BMVC&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;

    &lt;h1&gt;Minha página com interação de modelos :)&lt;/h1&gt;

    simbolo-% if transfered:
        &lt;div&gt;
            &lt;h2&gt;Dados do Usuário:&lt;/h2&gt;
            &lt;p&gt;Username: chaves-duplas data.username chaves-duplas &lt;/p&gt;
            &lt;p&gt;Password: chaves-duplas data.password chaves-duplas &lt;/p&gt;
        &lt;/div&gt;
    simbolo-% else:
        &lt;h2&gt;Porém, desta vez não foram transferidas quaisquer informações ): &lt;/h2&gt;
    simbolo-% end

&lt;/body&gt;
&lt;/html&gt;

          </code></pre>
          <h4 class="justify-text">Para finalizar, a rota específica deverá ser inserida no arquivo 'route.py'. Nosso exemplo termina
            com o fragmento de código a seguir:
          </h4>
          <pre class="code-block"><code>

@app.route('/pagina', methods=['GET'])
@app.route('/pagina/&lt;parameter&gt;', methods=['GET'])
def action_pagina(parameter=None):
    if not parameter:
        return ctl.render('pagina')
    else:
        return ctl.render('pagina',parameter)

          </code></pre>
          <h4 class="justify-text">Observe que a rota pode ser 'pagina/0' ou 'pagina/1'. Note que a ulr '/pagina' também poderá ser acessada sem informações sobre os modelos.
          </h4>
      </div>

</body>
</html>
