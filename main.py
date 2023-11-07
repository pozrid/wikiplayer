#импорт библиотек
from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI(title='Wiki Work')

#Output для имен(path)
class NameOutPut(BaseModel):
    return_name: str

#queer
class MultiNamesOutput(BaseModel):
    return_multi_names: str

#post
class GeoInput(BaseModel):
    x: float
    y: float

#post
class GeoOutput(BaseModel):
    geoplace: str


@app.get('/{name}', response_model=NameOutPut)
# def name_wikipedia(name_input: NameInput):
#     return name_input.name + str(wikipedia.page(name_input.name))

def names_wiki(name: str):
    """Поиск имени"""
    # return name + str(wikipedia.summary(name))
    return NameOutPut(return_name=str(wikipedia.summary(name)))


@app.get('/multi/{name}', response_model=MultiNamesOutput)
def multi_names_wiki(name: str, names_numbers: int):
    """Поиск определенного количества имен"""
    result = ''
    for i in range(names_numbers):
        result += name + f' pages numbers #{i + 1} :' + str(wikipedia.search(name, results=2))
    return MultiNamesOutput(return_multi_names=result)


@app.post('/', response_model=GeoOutput)
def geo_wiki(geo_input: GeoInput):
    """Локация"""
    # return str(wikipedia.page(geo_input.x, geo_input.y))
    return GeoOutput(geoplace=str(wikipedia.geosearch(geo_input.x, geo_input.y)))
