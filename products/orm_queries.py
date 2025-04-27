from products.models import Products
from django.db.models import Q
#ORM Queries Examples
# Basic queries
Products.objects.all()
Products.objects.get(id=1)
Products.objects.filter(price__gt=500)
Products.objects.filter(price__gte=500)
Products.objects.exclude(is_available=True)

# String matching
Products.objects.filter(name__contains="Pro")     # Case-sensitive
Products.objects.filter(name__icontains="pro")    # Case-insensitive

# Ordering
Products.objects.order_by('price')   # ASC
Products.objects.order_by('-price')  # DESC

# Aggregation
from django.db.models import Avg
Products.objects.aggregate(Avg('price'))

# Values
Products.objects.values('id', 'price')


#Complex Queries with Q Objects
# OR condition
Products.objects.filter(Q(price__gt=500) | Q(is_available=True))

# AND condition
Products.objects.filter(Q(price__gt=500) & Q(is_available=True))

# NOT condition
Products.objects.filter(~Q(is_available=True))

# Raw SQL Queries (only if needed)
Products.objects.raw('SELECT * FROM products_products WHERE price > %s', [500])

#Debugging ORM
qs = Products.objects.filter(price__gt=500)
print(qs.query)   # See the generated SQL query


# Solve the N+1 Query Problem
# Bad Practice (creates N+1 queries):
# products = Products.objects.all()
# for product in products:
#     print(product.category.name)
# Good Practice (only 1 query using select_related):
#
# products = Products.objects.select_related('category').all()
# for product in products:
#     print(product.category.name)
# For ManyToMany, use prefetch_related:
# orders = Order.objects.prefetch_related('products').all()
# for order in orders:
#     print(order.products.all())


#Test using Django Shell:
# python manage.py shell
#
# from products.models import *
#
# # Create Category
# cat = Category.objects.create(name="Electronics")
#
# # Create Product
# prod = Products.objects.create(name="iPhone 15", price=1200, category=cat)
#
# # Create Order
# order = Order.objects.create()
# order.products.add(prod)
#
# # Access Products inside Order
# order.products.all()
#
# # Access Orders from Product
# prod.orders.all()
