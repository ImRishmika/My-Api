from fastapi import FastAPI

# modules

from modules.unsplash import get_unsplash

app = FastAPI()


@app.get("/")
async def read_root():
    return {"TechZBots": "Api working fine..."}


@app.get("/wall/?search={query}")
async def read_item(query):
    data = get_unsplash(query)

    if str(type(data)) == "<class 'str'>":
        return {"success": "False", "error": f"{data}"}

    return {"success": "True", "images": f"{data}"}