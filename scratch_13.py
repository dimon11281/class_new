class Car:
    def __init__(self, name_car="Swallow", year_car=2000, fabricator_car="Nissan", engine_capacity = 2.0, color_car="white", price_car=1_000_000):
        self.__name_car = name_car
        self.__year_car = year_car
        self.__fabricator_car = fabricator_car
        self.__engine_capacity = engine_capacity
        self.__color_car = color_car
        self.__price_car = price_car

    def set_name(self, y):
        self.__name_car = y

    def set_year_car(self, y):
        self.__year_car = y

    def set_fabricator_car(self, y):
        self.__fabricator_car = y

    def set_engine_capacity(self, y):
        self.__engine_capacity = y

    def set_color_car(self, y):
        self.__color_car = y

    def set_price_car(self, y):
        self.__price_car = y

    def get_year_car(self):
        return self.__year_car

    def get_fabricator_car(self):
        return self.__fabricator_car

    def get_engine_capacity(self):
        return self.__engine_capacity

    def get_color_car(self):
        return self.__color_car

    def get_price_car(self):
        return self.__price_car

    def __str__(self):
        return (f"Название: {self.__name_car}, год выпуска {self.__year_car}, производитель {self.__fabricator_car}, объем двигателя {self.__engine_capacity}, "
                f"цвет {self.__color_car}, цена автособиля {self.__price_car}")


# car1 = Car("Zayobyshek", 1995, "Volga", color_car="yellow")
# print(car1)
# print(car1.set_price_car(1_500_000))
# print(car1)


class Book:

    def __init__(self, name_book, year_book=2000, publishing_book="Книгиздат", genre_book="детектив", author_book="писатель", price_book=1_000):
        self.__name_book = name_book
        self.__year_book = year_book
        self.__publishing_book = publishing_book
        self.__genre_book = genre_book
        self.__author_book = author_book
        self.__price_book =price_book

    def set_name_book(self, x):
        self.__name_book = x

    def get_name_book(self):
        return self.__name_book

    def set_year_book(self, x):
        self.__year_book = x

    def get_year_book(self):
        return self.__year_book

    def set_publishing_book(self, x):
        self.__publishing_book = x

    def get_publishing_book(self):
        return self.__publishing_book

    def set_genre_book(self, x):
        self.__genre_book = x

    def get_genre_book(self):
        return self.__genre_book

    def set_author_book(self, x):
        self.__author_book = x

    def get_author_book(self):
        return self.__author_book

    def set_price_book(self, x):
        return self.__price_book

    def __str__(self):
        return (f"Название: {self.__name_book}, год выпуска {self.__year_book}, производитель {self.__publishing_book}, жанр {self.__genre_book}, "
                f"автор {self.__author_book}, цена книги {self.__price_book}")


book1 = Book("Вострица", price_book=2000)
print(book1)
print(book1.set_year_book(2024))


class Stadion:

    def __init__(self, name_stadion, year_stadion, country_stadion, city_stadion, volume_stadion):
        self.__name_stadion = name_stadion
        self.__year_stadion = year_stadion
        self.__country = country_stadion
        self.__city = city_stadion
        self.__volume = volume_stadion

    def set_name_stadion(self, name):
        self.__name_stadion = name

    def get_name_stadion(self):
        return self.__name_stadion

    def set_year_stadion(self, years):
        self.__year_stadion = years

    def get_year_stadion(self):
        return self.__year_stadion

    def set_country(self, country):
        self.__country = country

    def get_country(self):
        return self.__country

    def set_city(self, city):
        self.__city = city

    def get_city(self):
        return self.__city

    def set_volume(self, volume_book):
        self.__volume = volume_book

    def get_volume(self):
        return self.__volume

    def __str__(self):
        return (f"Название: {self.__name_stadion}, год выпуска {self.__year_stadion}, страна {self.__country}, город {self.__city}, "
                f"вместимость {self.__volume}")




