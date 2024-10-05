import os
import django
import datetime

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab06.settings')
django.setup()

from tienda.models import Categoria, Producto

def poblar_db():
    # Datos de categorías y productos
    datos = [
        {
            "categoria": "Gaseosas",
            "productos": [
                {"nombre": "Fanta 500ml", "precio": 1.80, "stock": 10},
                {"nombre": "Coca Cola 500ml", "precio": 2.50, "stock": 10},
                {"nombre": "7up 500ml", "precio": 1.70, "stock": 10},
            ]
        },
        {
            "categoria": "Snacks",
            "productos": [
                {"nombre": "Cheetos", "precio": 1.00, "stock": 12},
                {"nombre": "Chizito", "precio": 1.00, "stock": 12},
            ]
        },
        {
            "categoria": "Galletas",
            "productos": [
                {"nombre": "Picaras", "precio": 1.00, "stock": 12},
                {"nombre": "Coronita Fresa", "precio": 0.70, "stock": 12},
            ]
        },
        {
            "categoria": "Chocolates",
            "productos": [
                {"nombre": "Princesa", "precio": 1.50, "stock": 8},
                {"nombre": "Sublime", "precio": 1.50, "stock": 8},
                {"nombre": "Triángulo", "precio": 1.20, "stock": 8},
            ]
        },
    ]

    for item in datos:
        cat, created = Categoria.objects.get_or_create(nombre=item["categoria"])
        for prod in item["productos"]:
            Producto.objects.get_or_create(
                categoria=cat,
                nombre=prod["nombre"],
                defaults={
                    "precio": prod["precio"],
                    "stock": prod["stock"],
                    "pub_date": datetime.datetime.now()
                }
            )

    print("Base de datos poblada exitosamente.")

if __name__ == '__main__':
    print("Iniciando script para poblar la base de datos...")
    poblar_db()
    print("Proceso completado!")
