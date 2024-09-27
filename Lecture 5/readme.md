# Lecture 4: Request Body
READ THIS [LINK](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/) to learn about the basic concept

### Here I will give you somethings that I noted:

```
FastAPI allows you to declare additional information and validation for your parameters.
```

```
Having a default value of any type, including None, makes the parameter optional (not required).
when you need to declare a value as required while using Query, you can simply not declare a default value
Or an alternative way to explicitly declare that a value is required. You can set the default to the literal value = ...
```
```
Required, can be None
To do that, you can declare that None is a valid type but still use ... as the default
EXAMPLE: async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):
```

```
Generic validations and metadata:
alias
title
description
deprecated

Validations specific for strings:
min_length
max_length
pattern
```
## USE THIS COMMAND TO START APP SERVER:
```
cd Lecture 4
uvicorn main:app --reload
```