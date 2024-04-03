from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/films")
async def root():
    return "element"


if __name__ == "__main__":
    uvicorn.run("som2:app", host="0.0.0.0", port=9900, reload=True)
