from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from datetime import datetime

app = FastAPI()

class EmailRequest(BaseModel):
    email: EmailStr

@app.post("/api/subscribe")
def subscribe_email(req: EmailRequest):
    email = req.email

    with open("waitlist.csv", "a") as f:
        f.write(f"{email},{datetime.now()}\n")

    return {"message": "Email saved!"}
