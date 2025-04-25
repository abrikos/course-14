# Products catalogue

## Description

Catalogue for smartphones and lawn grasses

## Install instruction

Dependencies

```poetry python-dateutil```

```poetry python-utils```

```poetry pytest```

```poetry pytest-cov```

## Testing
```python -m pytest --cov=src --cov-report=html```

## Categories

```python
new_category = Category('name', 'description', [product1, product2])
new_category.add_product(product3)
print(new_category.products)
```

## Products
Product prints itself on creation
```python
smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
```
You can print product and sum up 2 products within one type 
