# desafio_dio_criando_sistema_bancario_python
# 🏦 Sistema Bancário em Python

Este projeto foi desenvolvido como desafio prático do curso de **Python Developer - DIO / Suzano**.  
O sistema simula operações bancárias simples, como **depósito**, **saque** e **emissão de extrato**, com algumas regras definidas.

---

## 📌 Funcionalidades

✅ **Depósito**  
- Permite adicionar saldo à conta.  
- Só aceita valores maiores que zero.  

✅ **Saque**  
- Limite de R$ 500,00 por saque.  
- Limite máximo de **3 saques por dia**.  
- Não permite saque se não houver saldo suficiente.  

✅ **Extrato**  
- Mostra todas as movimentações realizadas (depósitos e saques).  
- Exibe também o saldo atual da conta.  
- Caso não existam movimentações, informa o saldo inicial.  

✅ **Controle de datas**  
- O sistema registra data e hora de cada operação.  
- O limite de 3 saques é **reiniciado automaticamente a cada novo dia**.

---

## 📂 Estrutura do Código

- `menu`: menu de opções exibido ao usuário.  
- `deposito()`: função para realizar depósitos.  
- `saque()`: função para realizar saques respeitando limites.  
- `gerar_extrato()`: função para exibir o extrato e saldo atual.  
- `data()`: retorna a data e hora atual formatada.  

---

## ▶️ Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/joaopgioio/desafio_dio_criando_sistema_bancario_python.git
