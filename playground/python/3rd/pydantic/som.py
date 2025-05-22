from typing import Annotated
from pydantic import BaseModel, Field, create_model


class Team(BaseModel):
    tn: str | None
    players: int | None


class User(BaseModel):
    id: int
    name: str
    team: Team | None = None
    is_active: bool = True


    def move(self, other):
        for field in self.model_fields:
            setattr(self, field, getattr(other, field))



class SuperUser(User):
    p1: int



u = SuperUser(id=1, name='a', p1=1)
u2 = SuperUser(id=3, name='b', p1=2, team=Team(tn="xx", players=2))
print(u)
u.move(u2)
print(u)
