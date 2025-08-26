from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI()

# Add CORS middleware to allow requests from React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request model
class MessageRequest(BaseModel):
    message: str

# Define response model
class MessageResponse(BaseModel):
    result: str

@app.post("/process-message", response_model=MessageResponse)
async def process_message(request: MessageRequest):
    # Append "yyyy" to the input message
    processed_message = request.message + "yyyy"
    return MessageResponse(result=processed_message)

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "FastAPI server is running"}

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
