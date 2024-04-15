'''from django.db import models

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

dummy_items = [
    {'item': 'laptop', 'quantity': 10},
    {'item': 'printer', 'quantity': 5},
    {'item': 'keyboard', 'quantity': 8},
    {'item': 'monitors', 'quantity': 20},
    {'item': 'tablet', 'quantity': 15},
]

for order_data in dummy_items:
    Inventory.objects.create(**order_data)

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

dummy_items = [
    {'item': 'laptop', 'quantity': 2},
    {'item': 'printer', 'quantity': 3},
    {'item': 'keyboard', 'quantity': 1},
    {'item': 'monitors', 'quantity': 5},
    {'item': 'tablet', 'quantity': 6},
]

for order_data in dummy_items:
    Orders.objects.create(**order_data)'''

from django.db import models

class Composts(models.Model):
    compost_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 5000)
    description = models.TextField()
    available_units = models.IntegerField()
    cost_per_unit = models.IntegerField()

class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    compost_id = models.IntegerField()
    quantity = models.IntegerField()
    total_cost = models.IntegerField()
    date_of_purchase = models.DateField()


'''compost1 = Composts.objects.create(
    name="GreenGarden Blend",
    description="A rich blend of organic materials for lush gardens. This is rich in Zinc (Zn) which is involved in hormone production and stem elongation and Molybdenum (Mo) that is required for nitrogen fixation in legumes.",
    available_units=100,
    cost_per_unit=15
)

compost2 = Composts.objects.create(
    name="EcoGrow Plus",
    description="Premium organic compost for vibrant plant growth. It is rich in Boron (B) that aids in cell division, cell elongation, and flower formation along with Copper (Cu) which is essential for enzyme function and overall plant growth.",
    available_units=75,
    cost_per_unit=20
)

compost3 = Composts.objects.create(
    name="BloomBoost Pro",
    description="Boost your blooms with this nutrient-rich compost. Nutrients present in this are Iron (Fe) which is vital for chlorophyll production and overall plant greenness. Manganese (Mn) is also present that is involved in photosynthesis and nitrogen metabolism.",
    available_units=50,
    cost_per_unit=18
)

compost4 = Composts.objects.create(
    name="NourishNature Gold",
    description="Gold-standard compost for healthy soil and plants. Magnesium (Mg) that is necessary for photosynthesis and chlorophyll production and Sulfur (S) which plays a role in the formation of amino acids and proteins are present in this mix.",
    available_units=90,
    cost_per_unit=22
)

compost5 = Composts.objects.create(
    name="PurePlant Elixir",
    description="Elixir of life for your garden - pure and organic. Potassium (K) that helps with overall plant vigor, disease resistance, and stress tolerance and Calcium (Ca) that is essential for cell wall formation and stability are a prime component of this mix.",
    available_units=60,
    cost_per_unit=25
)

compost6 = Composts.objects.create(
    name="Garden Bliss",
    description="Experience garden bliss with this organic compost blend. It contains essential nutrients like Potassium (K) for plant vigor and Calcium (Ca) for strong cell walls. Additionally, it enriches the soil with vital micronutrients for healthy growth.",
    available_units=80,
    cost_per_unit=28
)

o1 = Orders.objects.create(
    compost_id=2,
    quantity=30,
    total_cost=600,
    date_of_purchase='2023-06-13'
)

o2 = Orders.objects.create(
    compost_id=4,
    quantity=20,
    total_cost=440,
    date_of_purchase='2023-08-27'
)'''