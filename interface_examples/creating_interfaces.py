from typing import TypedDict


# Definindo a tipagem para o dicionário
class Product(TypedDict):
    id: int
    name: str
    price: float
    in_stock: bool


# Usando o TypedDict
product_example: Product = {
    "id": 1,
    "name": "Notebook",
    "price": 2500.99,
    "in_stock": True,
}

# Acessando as chaves com segurança
print(product_example["name"])  # Saída: Notebook
