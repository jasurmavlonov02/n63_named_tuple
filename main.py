# # NamedTuple => 


# user = [19,'john','doe',124235,4]

# print(user[0])

from collections import namedtuple

# # point = (10,20)
# Point = namedtuple('Point',['x','y'])

# point = Point(x = 10 , y = 15)

# # print(point.y)

# print(point[0])


# Person = namedtuple('Person',['name','age','children'])
# person = Person('John Doe',35,['Tom','Ann','Josiphe'])
# print(person.name)


Product = namedtuple('Product','name description price quantity')
product = Product('Iphone 15','Norm',15_000,25)

product_data_as_dict = Product._asdict(product)
# print(product.name)
# print('Product fields : ', product._fields)
# product = product._replace(name = 'Samsung',quantity = 100)
# print(product)
# product.name = '123'
# product[1] = 'asdasd'
print('NamedTuple to Dictionary')
print(product_data_as_dict)
print('--------------------')

