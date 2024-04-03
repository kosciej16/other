from typing import TypeVar, Generic, Any



T = TypeVar('T')

class AnyType(Generic):
    def __init__(self, Type: Any):
        self.Type = Type


class Nested(AnyType):
    def __init__(self, Type: T):
        super().__init__(Type)

n = Nested("A")
# class PrimitiveType(AnyType):
#     def __init__(self, Type:Literal['String', 'Number']):
#         super().__init__(Type)
#     def __str__(self):
#         return self.Type

# String = PrimitiveType('String')
# Number = PrimitiveType('Number')

# class NestedType(AnyType):
#     def __init__(self, Type:AnyType):
#         # see note from AnyType
#         assert self.__class__.__name__ in ('Struct', 'Array')
#         super().__init__(Type)

# class Array(NestedType):
#     def __init__(self, Type:AnyType):
#         super().__init__(Type)
#     def __str__(self):
#         return 'ARRAY(' +  str(self.Type) + ')'

# class Pair:
#     def __init__(self, Key:str, Type:AnyType):
#         self.Key = Key
#         self.Type = Type
#     def __str__(self):
#         return f'{self.Key} {self.Type}'

# class Struct(NestedType):
#     def __init__(self, Pairs:tuple[Pair]):
#         super().__init__(Pairs)
#     def __str__(self):
#         return 'STRUCT(' + ', '.join([str(Pair) for Pair in self.Type]) + ')'

# # array of strings
# if __name__ == '__main__':
#     a1 = Array('String')
#     print (a1)
#     a2 = Array(Array('Number'))
#     print (a2)
#     s = Struct((Pair("Hello", Array('STRING')), Pair("Tom", "NUMBER")))
#     print (s)
#     a3 = Array(s)
#     print (a3)
