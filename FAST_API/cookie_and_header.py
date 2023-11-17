from fastapi import FastAPI,Cookie,Header
app = FastAPI()

@app.get('/items')
async def read_items(cookie_id: str | None = Cookie(None) ,
    accept_encoding : str | None = Header(None),
    user_agent : str | None = Header(None)):
    return {'cookies': cookie_id, "Accept_encoding":accept_encoding , "User-Agent":user_agent }