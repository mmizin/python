# https://webdevblog.ru/chto-takoe-metaklassy-v-python/

################## Dynamically create class

def choose_class(name):

    if name == 'foo':
        class Foo:
            pass
        return Foo
    else:
        class Bar:
            pass
        return Bar


MyClass = choose_class('foo')
MyClass  #  <class '__main__.choose_class.<locals>.Foo'>
MyClass()  # <__main__.choose_class.<locals>.Foo object at 0x7fc083edafa0>


################## Create class by hand via type()

MyShinyClass = type('MyShinyClass', (), {})
MyShinyClass  #  <class '__main__.MyShinyClass'>
MyShinyClass()  # <__main__.MyShinyClass object at 0x7f698fd69fd0>

################## Add attribute to the class via type()

Foo = type('Foo', (), {'my_attribute': True})
Foo.my_attribute   #  True

################## Inheritance class via type()

ChildFoo = type('ChildFoo', (Foo,), {})
ChildFoo   #  <class '__main__.FooChild'>
ChildFoo.my_attribute   # True

################## Add function to the class via type()

def foo_function(self):
    return True

ChildFoo = type('ChildFoo', (Foo, ), {'foo_function': foo_function})
my_foo = ChildFoo()
my_foo.foo_function()   #  True


# Метаклассы — это «материал», который создает классы.
# Вы определяете классы для создания объектов, верно? Но мы узнали, что классы Python — это объекты.
# Что ж, метаклассы создают эти объекты. Это классы классов, и их можно изобразить так:

# MyClass = MetaClass()
# my_object = MyClass()

# Представьте себе глупый пример, в котором вы решили, что атрибуты всех классов в вашем модуле должны быть написаны в
# верхнем регистре. Есть несколько способов сделать это, но один из них — установить __metaclass__ на уровне модуля.

class UpperAttrMetaclass(type):
    def __new__(cls, clsname, bases, attrs):
        uppercase_attrs = {
            attr if attr.startswith("__") else attr.upper(): v
            for attr, v in attrs.items()
        }
        return type(clsname, bases, uppercase_attrs)


class Test(metaclass=UpperAttrMetaclass):
    v = 'vasya'


t = Test()
print(t.v)