from typing import Annotated
from fastapi import FastAPI, Query


class MyFastAPIApp:
    def __init__(self):
        self.app = FastAPI()
        self._baseUrl = "definir"

        # Define routes in the constructor
        self.define_routes()

    def define_routes(self):
        @self.app.get("/")
        async def read_root():
            return {"message": "Hello, World!"}

        @self.app.get("/news/latest")
        async def read_item(item_id: int, q: str = None):
            return {"message": "These are the latest news"}
        
        @self.app.get("/news/all")
        async def read_producao(ano: Annotated[str | None, Query(min_length=4, max_length=4)] = None):
            """Example of API documentation \n
            other line
            """
            return {"message": "These are the latest news"}

        ## Define the Pydantic type for the year parameter
        #YearParam = conint(ge=1970, le=2022)
        #@router.get("/productions/{year}", response_model=ProductionResponse)
        #async def get_productions (year: YearParam) -> ProductionResponse:

    def run(self):
        # Run the FastAPI app
        import uvicorn
        uvicorn.run(self.app, host="127.0.0.1", port=8000)