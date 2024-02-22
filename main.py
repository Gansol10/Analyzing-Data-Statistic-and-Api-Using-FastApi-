from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

API_KEY = "phase0h8"

data = {'trip_seconds'}

@app.post("/add")
def add_item(added_item:dict, api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to add data!")
    else:
        id = len(data["trip_seconds"].keys())+1
        data["trip_seconds"][id] = added_item
        return f"trip_seconds successfully ID {id}"