# Para ejecutar este script, utilizar el comando:
# > strawberry server main:schema

import strawberry

@strawberry.type
class User:
    name: str
    age:int

@strawberry.type
class Query:
    @strawberry.field
    def user(self)->User:
        return User(name="Patrick", age=10)


schema = strawberry.Schema(query=Query)