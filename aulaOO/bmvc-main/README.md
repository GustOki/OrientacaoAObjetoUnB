Para executar, realize uma das seguintes estratégias:

Na raiz do projeto, faça:

1) Diretamente no terminal:

    $ python3 route.py
     
3) Conteinerizando:

    $ docker build -t bmvci .
    $ docker run -d --name my-running-app -p 8080:8080 bmvci
