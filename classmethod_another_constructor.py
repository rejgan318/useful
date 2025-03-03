from pydantic import BaseModel


class MyModel(BaseModel):
    a: str
    i: int

    @classmethod
    def another_constructor(cls, i):
        a = "Привет"
        return cls(a=a, i=i + 1)


model = MyModel(a="Стандартное создание", i=1)
print(model)
# a='Стандартное создание' i=1

another_model = MyModel.another_constructor(i=5)
print(another_model)
# a='Привет' i=6
