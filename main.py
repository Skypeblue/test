from fastapi import FastAPI

api = FastAPI(title="Mon API pour les MAR22 BDE")

"""
HTTP(S):
- URL
- Methode
- Corps ?
- En-têtes ?


URL: https://example.org/data
- protocole: https://
- nom de domaine (cache pour l'adresse IP du serveur): example.org
- point de terminaison: /data

Méthodes:
- GET
- PUT
- POST
- DELETE
"""


@api.get('/')
def get_index():
    return {
        "hello": "world"
    }


@api.get('/ma_route')
def get_ma_route():
    return {
        "method": "GET",
        "endpoint": "/ma_route"
    }


@api.post('/mon_post')
def post_mon_post(nombre_entier: int):
    return {
        "nombre_entier": nombre_entier
    }
