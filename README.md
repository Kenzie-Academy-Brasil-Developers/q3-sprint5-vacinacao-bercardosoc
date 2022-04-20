# DataBase de vacinas
Esta é uma API de vacinas onde o usuário pode registrá-las e lê-las.

## Requisições

Para realizá-las, deve-se utilizar o link de deploy da API no heroku: https://cadernetas-de-vacina.herokuapp.com

### GET / vaccinations - Status code - OK - 200
Apenas utilizando o GET teremos acesso a ela, sendo o corpo de resposta tendo dois formados possíveis:

Caso não haja nenhum registro, nos depararemos com:

```json
Vaccination data: []
```

Porém, se houver registros, teremos:

```json
[
  {
    "cpf": "01234567891",
    "name": "Chrystian",
    "first_shot_date": "Fri, 29 Oct 2021 16:30:31 GMT",
    "second_shot_date": "Thu, 27 Jan 2022 16:30:31 GMT",
    "vaccine_name": "Pfizer",
    "health_unit_name": "Santa Rita"
  },
  {
    "cpf": "19876543210",
    "name": "Cauan",
    "first_shot_date": "Fri, 29 Oct 2021 16:31:30 GMT",
    "second_shot_date": "Thu, 27 Jan 2022 16:31:30 GMT",
    "vaccine_name": "Coronavac",
    "health_unit_name": "Santa Rita"
  },
  {
    "cpf": "54221194161",
    "name": "Eduardo",
    "first_shot_date": "Fri, 29 Oct 2021 16:35:24 GMT",
    "second_shot_date": "Thu, 27 Jan 2022 16:35:24 GMT",
    "vaccine_name": "Coronavac",
    "health_unit_name": "Santa Rita"
  }
]
```

### POST / vaccinations - Status code - CREATED - 201

Uma requisição, para ser aceita, deve conter as seguintes chaves:

```json

{
  "cpf": "01234567891",
  "name": "Chrystian",
  "vaccine_name": "Pfizer",
  "health_unit_name": "Santa Rita"
}

```
Assim, a resposta de retorno será:

```json

{
  "cpf": "01234567891",
  "name": "Chrystian",
  "first_shot_date": "Fri, 29 Oct 2021 16:36:13 GMT",
  "second_shot_date": "Thu, 27 Jan 2022 16:36:13 GMT",
  "vaccine_name": "Pfizer",
  "health_unit_name": "Santa Rita"
}

```

No entanto, para exceções, há erros como os seguintes:

### POST / vaccinations - Status code - BAD REQUEST - 404

Caso o CPF tenha uma numeração diferente de 11 números inteiros, essa deve ser a resposta:

```json

{
  "cpf": "01234567891978785415210",
  "name": "Chrystian",
  "vaccine_name": "Pfizer",
  "health_unit_name": "Santa Rita"
}

```

```json
{
    "error": "CPF must be 11 digits"
}
```

### POST / vaccinations - Status code - BAD REQUEST - 404

Caso umas das chaves passadas não seja uma string, como o exemplo do cpf, deverá haver uma resposta a altura:

```json

{
  cpf: "01234567891",
  "name": "Chrystian",
  "vaccine_name": "Pfizer",
  "health_unit_name": "Santa Rita"
}

```

```json
{
    "error": "Values must be strings"
}
```
### POST / vaccinations - Status code - BAD REQUEST - 404

Caso umas das chaves esteja em falta, como o exemplo do cpf, deverá haver uma resposta que esclaresça o erro ao usuário:

```json

{
  "name": "Chrystian",
  "vaccine_name": "Pfizer",
  "health_unit_name": "Santa Rita"
}

```

```json
{
  "error": "missing_keys",
  "expected": [
    "vaccine_name",
    "cpf",
    "health_unit_name",
    "name"
  ],
  "received": [
    "vaccine_name",
    "health_unit_name",
    "name"
  ]
}
```

### POST / vaccinations - Status code - BAD REQUEST - 404

Caso umas das chaves seja uma string, mas esteja incorreta semanticamente, como o exemplo do nome, deverá haver uma resposta que esclaresça o erro ao usuário:

```json

{
	"cpf": "01234567891",
  "nameeeee": "Chrystian",
  "vaccine_name": "Pfizer",
  "health_unit_name": "Santa Rita"
}

```

```json
{
  "error": "invalid_keys",
  "expected": [
    "vaccine_name",
    "cpf",
    "health_unit_name",
    "name"
  ],
  "wrong_key(s)": [
    "nameeeee"
  ]
}
```

### POST / vaccinations - Status code - CONFLICT - 409

Caso o CPF já esteja cadastrado, deve-se tratar o erro com conflito e informar que tal está cadastrado.

```json

{
	"cpf": "01234567891",
  "name": "Chrystian",
  "vaccine_name": "Pfizer",
  "health_unit_name": "Santa Rita"
}

```

```json

{
  "error": "CPF already registered"
}

```