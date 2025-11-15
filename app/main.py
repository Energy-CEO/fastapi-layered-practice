import os

from dotenv import load_dotenv
from fastapi import FastAPI

from anonymous_board.controller.anonymous_board_controller import anonymous_board_controller
from config.mysql_config import Base, engine

load_dotenv()

app = FastAPI()
app.include_router(anonymous_board_controller)

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("APP_HOST")
    port = int(os.getenv("APP_PORT"))
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host=host, port=port)
