# Spinal

A Spinal API é uma API construída em Python que permite a integração de *agents* com modelos de linguagem (LLMs). Ela recebe requisições com mensagens e chamadas de ferramentas, interage com a LLM e retorna a resposta serializada, incluindo quaisquer chamadas de ferramentas realizadas pelo modelo.

## Funcionalidade

Esta API foi projetada para receber requisições no formato JSON contendo uma lista de mensagens e ferramentas a serem usadas pelo modelo. Ela processa a requisição, interage com o modelo de linguagem e retorna a resposta, incluindo as chamadas de ferramentas (tool calls) que o modelo possa ter feito.

### Endpoints

#### `POST /message`

Recebe um conjunto de mensagens e ferramentas e retorna a resposta do modelo de linguagem.

**Requisição**

- Método: `POST`
- URL: `/message`
- Corpo da requisição (JSON):
  
```json
{
    "messages": [
        {
            "role": "user",
            "content": "Olá, como você está?"
        }
    ],
    "tools": [
        {
            "tool_name": "tool_example",
            "parameters": {
                "param1": "value1"
            }
        }
    ]
}
```

### Resposta

* Código de Status: 200 OK
* Corpo da resposta (JSON):

```json
{
    "message": "Aqui está a sua resposta!"
}
```