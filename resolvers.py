from typing import List

people_data = [
    {
        "id": "1",
        "firstName": "Ana",
        "lastName": "García",
        "age": 25,
        "email": "ana.garcia@email.com"
    },
    {
        "id": "2",
        "firstName": "Carlos",
        "lastName": "Rodríguez",
        "age": 32,
        "email": "carlos.rod@email.com"
    },
    {
        "id": "3",
        "firstName": "María",
        "lastName": "López",
        "age": 28,
        "email": "maria.lopez@email.com"
    },
    {
        "id": "4",
        "firstName": "Juan",
        "lastName": "Martínez",
        "age": 41,
        "email": "juan.martinez@email.com"
    },
    {
        "id": "5",
        "firstName": "Laura",
        "lastName": "Sánchez",
        "age": 35,
        "email": "laura.sanchez@email.com"
    }
]
def resolve_people(*_) -> List[dict]:
    return people_data

def resolve_people_by_age_range(*_, minAge: int, maxAge: int) -> List[dict]:
    return [
        person for person in people_data 
        if minAge <= person["age"] <= maxAge
    ]