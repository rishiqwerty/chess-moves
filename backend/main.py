from fastapi import FastAPI, HTTPException
from chess_moves import *
app = FastAPI()

# Create an in-memory dictionary to store data
data_store = {}

@app.post("/chess/{param}")
async def post_data(param:str,item: dict):
    # Store data in the dictionary
    moves = valid_moves(param, item)
    return {"valid_moves": moves}

if __name__ == "__main__":
    import uvicorn

    # Run the application using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
