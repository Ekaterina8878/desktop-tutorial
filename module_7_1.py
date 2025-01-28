import os


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        # Если файл не существует, создаем его
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, 'w') as file:
                pass  # Просто создаем пустой файл

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read()

    def add(self, *products):
        current_products = self.get_products().splitlines()

        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)

                # Проверка, существует ли продукт в магазине
                if product_str in current_products:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(product_str + '\n')



if __name__ == "__main__":
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)

    s1.add(p1, p2, p3)

    print(s1.get_products())
