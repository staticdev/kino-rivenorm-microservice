# kino-rivenorm-microservice

Webservice REST para normalizar mensagens usando Rivescript.

## Requisitos

- Instalar Docker-CE Versão 19.03+

## Geração interfaces

```sh
python3 -m pip install grpcio-tools
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protos/normalization.proto
```

## Execução

Rodar os comandos:

```sh
# gerar a imagem
sudo docker build -t staticdev/rivenorm:2.0.0 .
# verificar se gerou
sudo docker images
# instanciar imagem
sudo docker run --name rivenorm -d -p 50051:50051 staticdev/rivenorm:2.0.0
# conferir processo rodando
sudo docker ps -a

# para parar o container
sudo docker stop rivenorm
# para remover um container (precisa parar primeiro)
sudo docker rm rivenorm
# para deletar a imagem
sudo docker rmi staticdev/rivenorm:2.0.0
```

### Exemplo de uso

Foi criado um cliente gRPC de [exemplo](examples/normalization_client.py).
