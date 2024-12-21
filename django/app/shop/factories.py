from factory import Faker
from factory.django import DjangoModelFactory
from .models import Sell, Material

locale = "ru_RU"
mats = Material.objects.all()


class SellFactory(DjangoModelFactory):
    class Meta:
        model = Sell

    count = Faker("random_int", min=1, max=100, locale=locale)
    name = Faker("first_name", locale=locale)
    surname = Faker("last_name", locale=locale)
    city = Faker("city_name", locale=locale)
    country = Faker("country", locale=locale)
    mat = Faker("random_element", elements=mats)
