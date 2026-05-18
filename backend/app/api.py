import os
from dotenv import load_dotenv

# Charger les variables d'environnement avant les autres imports
load_dotenv()

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional
from .graph import app_graph
from langchain_core.messages import HumanMessage, AIMessage

app = FastAPI(title='Clinical Orchestrator API')

class ChatInput(BaseModel):
    message: str
    thread_id: Optional[str] = "default"

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat(input: ChatInput, request: Request):
    try:
        # On pourrait extraire la clé API du header si on voulait la passer au graphe
        # auth_header = request.headers.get("Authorization")
        
        # Configuration pour LangGraph
        config = {"configurable": {"thread_id": input.thread_id}}
        
        # État initial ou messages additionnels
        inputs = {"messages": [HumanMessage(content=input.message)]}
        
        # Exécution du graphe (on prend le dernier message de l'état final)
        final_state = await app_graph.ainvoke(inputs, config=config)
        
        if not final_state.get("messages"):
            raise ValueError("No messages returned from graph")
            
        last_message = final_state["messages"][-1]
        return ChatResponse(response=last_message.content)
    except Exception as e:
        print(f"Error in /chat: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
