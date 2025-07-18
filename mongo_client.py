from pymongo import MongoClient
from typing import Dict, Any, List
from dotenv import load_dotenv
from os import getenv

load_dotenv()
client = MongoClient(getenv('MONGO_URI'))
db = client[getenv('MONGO_DB')]

def adicionar_tabela(colecao: str, dados: Dict[str, Any]) -> str:
    """Adiciona um item genérico à coleção especificada."""
    result = db[colecao].insert_one(dados)
    return str(result.inserted_id)

def remover_tabela(colecao: str, filtro: Dict[str, Any]) -> int:
    """Remove um item da base em um filtro da coleção especificada."""
    result = db[colecao].delete_one(filtro)
    return result.deleted_count

def editar_tabela(colecao: str, filtro: Dict[str, Any], novos_dados: Dict[str, Any]) -> int:
    """Edita base em um filtro e novos dados na coleção especificada."""
    result = db[colecao].update_one(filtro, {"$set": novos_dados})
    return result.modified_count

def listar_tabela(colecao: str, filtro: Dict[str, Any] = {}) -> List[Dict[str, Any]]:
    results = db[colecao].find(filtro)
    return [{k: str(v) if k == "_id" else v for k, v in result.items()} for result in results]
