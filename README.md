# Projeto Integrador - E-commerce Dipirona

## Introdução

O E-commerce Dipirona é uma plataforma online desenvolvida para a venda de produtos personalizados, como canecas e camisetas, além de permitir que os clientes agendem eventos exclusivos. O objetivo é oferecer uma experiência de compra acessível e segura, direcionada aos clientes da marca Dipirona.

## Tecnologias Utilizadas

Este projeto utiliza as seguintes tecnologias e frameworks:

- **Framework:** Django
- **Banco de Dados:** MySQL

## Instalação

Para configurar o ambiente de desenvolvimento do projeto, siga os passos abaixo:

1. **Clone o repositório do projeto:**

   ```bash
   git clone https://github.com/kauaDaviAmaro/Projeto-Integrador-Ecommerce
   ```

2. **Instale as dependências:**
   As dependências estão listadas no arquivo `requirements.txt`. Para instalá-las, execute:

   ```bash
   pip install -r requirements.txt
   ```

   As principais dependências são:
   - Django
   - Pillow
   - mysqlclient
   - faker
   - requests

3. **Configuração do Banco de Dados:**
   No arquivo `settings.py`, configure as informações do banco de dados na variável `DATABASES`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'projectpi',
           'USER': 'root',
           'PASSWORD': '',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

   **Aviso:** Não se esqueça de criar o banco de dados antes de executar as migrações.

   Certifique-se de criar o banco de dados no mysql antes de executar as migrações:

   ```bash
   python manage.py migrate
   ```

4. **Seed do Banco de Dados:**
   Para preencher o banco de dados com dados ficticios (aleatórios), utilize o comando:

   ```bash
   python manage.py seed_all
   ```

5. **Criar Superusuário:**
   Para acessar o painel administrativo, é necessário criar um superusuário:

   ```bash
   python manage.py createsuperuser
   ```

6. **Executar o Servidor:**
   Inicie o servidor de desenvolvimento com:

   ```bash
   python manage.py runserver
   ```

## Funcionalidades Principais

- **Catálogo de Produtos:** Venda de produtos personalizados como canecas e camisetas.
- **Agendamento de Eventos:** Opção para clientes agendarem eventos diretamente na plataforma.
- **Carrinho de Compras:** Funcionalidade em desenvolvimento.
- **Sistema de Navegação:** Menu hamburguer e design responsivo para diferentes dispositivos.
- **Acessibilidade:** Implementação de ferramentas como Vlibras e descrições alternativas para imagens.

## Painel Administrativo

O E-commerce Dipirona conta com uma tela de administrador integrada, acessível apenas para usuários com permissões administrativas. Através dessa interface, é possível gerenciar os produtos, eventos, pedidos e outras configurações importantes do site.

### Acesso ao Painel Administrativo

1. **Criar Superusuário:** Antes de acessar o painel, é necessário criar um superusuário com o seguinte comando:

   ```bash
   python manage.py createsuperuser
   ```

2. **Login:** Acesse a tela de administração através do link `/admin/` no navegador (por exemplo, `http://127.0.0.1:8000/admin/`) e faça login com as credenciais do superusuário criado.

3. **Funcionalidades Disponíveis no Painel Administrativo:**
   - Gerenciamento de produtos e categorias.
   - Controle de pedidos e agendamentos de eventos.
   - Moderação de depoimentos de clientes.
   - Configuração de dados do site.

## Checklist do Projeto

### Geral

- [X] Auto seeding
- [ ] Melhor organização do projeto
- [ ] Implementar sistema de carrinho de compra?
- [ ] Testes automatizados para funcionalidades principais
- [ ] Documentação completa do código

### Administrador

- [ ] Traducao
- [ ] Organização

### Navbar

- [X] Menu hamburguer
- [X] Responsividade
- [ ] Implementar busca rápida no menu

### Home

- [ ] Responsividade
- [ ] Seção "Como Funciona"
- [ ] Depoimentos de Clientes
- [ ] Destaques de produtos e eventos

### Catálogo de Produtos

- [X] Responsividade
- [ ] Filtros de Busca e Categorias
- [ ] Implementar paginação

### Visualização de Produto

- [ ] Terminar e formatar design da pagina
- [ ] Responsividade
- [ ] Prosseguir para adicionar seu design

### Catálogo de Eventos

- [ ] Arrumar design da pagina
- [X] Responsividade
- [ ] Filtros de Busca e Categorias
- [ ] Adicionar descrição detalhada dos eventos

### Visualização de Evento

- [ ] Criar a pagina de visualização do evento
- [ ] Responsividade

### Fale Conosco

- [X] Validar Campos
- [X] Salvar Mensagem
- [X] Mostrar confirmação ao salvar
- [X] Responsividade

### Sobre Nós

- [ ] Adicionar uma descrição sobre a empresa
- [X] Responsividade

### Acessibilidade

- [X] Vlibras
- [X] Alt para imagem
- [ ] Navegação por teclado
- [ ] Suporte para leitores de tela

## Visualização de perfil

- [ ] Criar a página de visualização de perfil
- [ ] Adicionar edição de informações pessoais
- [ ] Histórico de compras e eventos agendados
- [ ] Foto de perfil e configuração de preferências

## Autenticação

- [ ] Implementar sistema de login e registro
- [ ] Recuperação de senha por e-mail

## Carrinho de Compras

- [ ] Implementar lógica de adicionar/remover itens
- [ ] Atualização automática do total
