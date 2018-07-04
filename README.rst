kino-rivenorm-microservice
==========================

Webservice REST para normalizar mensagens usando Rivescript

Instalar Docker-CE
~~~~~~~~~~~~~~~~~~

Requisito mínimo: Versão 18.03.1+

.. code-block:: sh

  sudo apt remove docker docker-engine docker.io
  sudo apt-get install \
  apt-transport-https \
  ca-certificates \
  curl \
  software-properties-common
  # baixar chave GPG
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  # conferir o fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88
  sudo apt-key fingerprint 0EBFCD88
  # adicionar repositório oficial
  sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
  # baixar lista de pacotes do novo repositório
  sudo apt-get update
  # instalar
  sudo apt-get install docker-ce
  docker --version # test installation

Subir o serviço
~~~~~~~~~~~~~~~

Rodar os comandos:

.. code-block:: sh

  # gerar a imagem
  sudo docker build -t staticdev/rivenorm:0.1.2 .
  # verificar se gerou
  sudo docker images
  # instanciar imagem
  sudo docker run --name rivenorm -d -p 6000:5000 staticdev/rivenorm:0.1.2
  # conferir processo rodando
  sudo docker ps -a
  
  # para parar o container olhe o nome dele no docker ps -a e execute
  sudo docker stop NOMEDOCONTAINER
  # para remover um container (precisa parar primeiro)
  sudo docker rm NOMEDOCONTAINER

Exemplos de uso
---------------

Basta fazer um POST da mensagem a ser normalizada na url /reply passando a mensagem no campo "message".

A mensagem normalizada é retornada no campo "reply". O status da requisição no campo "status", tendo com valor padrão para sucesso "ok".

Exemplo curl:

.. code-block:: sh

  curl -X POST \
    http://localhost:6000/reply \
    -H 'content-type: application/json; charset=utf-8' \
    -d '{
      "message": "oi td bm?"
  }'

Exemplo python3 nativo (http.client):

.. code-block:: python

  import http.client

  conn = http.client.HTTPConnection("localhost:6000")

  payload = "{\"message\": \"oi td bm?\"}"

  headers = {
      'content-type': "application/json; charset=utf-8"
  }

  conn.request("POST", "/reply", payload, headers)
  res = conn.getresponse()
  data = res.read()

  print(data.decode("utf-8"))
