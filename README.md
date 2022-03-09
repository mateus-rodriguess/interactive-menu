# interactive-menu

Neste projeto foi desenvolvido um cardápio web pra restaurantes, onde além de apresentar os produtos com a descrição e seus ingredientes os clientes podem adicioná-los no carrinho, escolher a quantidade e uma breve descrição, e depois efetuar o método de pagamento PIX.
Para o desenvolvimento foi usado o framework Django.
____________________________________________________________

## Objetivos

- [x] Lista de produtos
- [x] Categoria de produtos
- [x] Carinho de compra
- [x] Sistema de registo
    - [x] Perfil do usuario 
- [x] Compras
- [x] Gerenciamento de estoque
- [x] ADM
- [ ] Layout final
- [x] Conteiner docker
- [x] Testes
- [x] API
- [x] JWTAuthentication
____________________________________________________________

 # Como instalar
 * Install [Docker](https://docs.docker.com/compose/install/)
 * Executar o comando docker

```bash
docker-compose up
```
 * Criar o super usuario 
```bash
docker-compose run web python manage.py createsuperuser
```
Seu aplicativo estará em execução em `http://127.0.0.1:8000`
