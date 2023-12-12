from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def f_index():
    return {"message": "Денисов Роман Дмитриевич"}
@app.get('/users')
async def f_index():
    return {"message": "users", "key": "79238282828"}

@app.get('/tools')
async def f_index():
    return {"message": "tools", "key": "junior"}

