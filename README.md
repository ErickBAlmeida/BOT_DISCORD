# 🤖 Bot de Discord 

Um robô simples para gerenciar e interagir com usuários de um servidor de Discord.

## Funcionalidades

- **Sistema de Boas-vindas**: Envia uma mensagem personalizada quando um novo membro entra no servidor
- **Notificações de Call**: Avisa quando alguém entra no canal de voz pré-definido
- **Comandos Interativos**: Comandos simples para interação com os usuários

### Comandos Disponíveis

- `.ajuda` - Mostra a lista de comandos disponíveis
- `.ola` - O bot te cumprimenta com seu nome

## Estrutura do Projeto

- `main.py` - Arquivo principal com a lógica do bot
- `config.py` - Configurações dos canais de texto e voz
- `private/.env` - Arquivo de configuração com o token do bot (não incluído no repositório)

## Como Executar

1. Certifique-se de ter todas as dependências instaladas
2. Configure o arquivo `.env` com o token do seu bot
3. Execute o bot:
   ```powershell
   python main.py
   ```

## Características do Bot

- Prefix do comando: `.` (ponto)
- Intents: Todas habilitadas
- Sistema de eventos automatizados
- Mensagens personalizadas

## Contribuição

Sinta-se à vontade para contribuir com o projeto através de Pull Requests ou reportando issues.

## Autor

@ErickBAlmeida