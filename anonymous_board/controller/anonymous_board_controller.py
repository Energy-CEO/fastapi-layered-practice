# Spring Boot / Spring Reactive
# @RestController / @Controller
# FastAPI 의 경우 API Router가 Controller 역할 수행
from typing import List

from fastapi import APIRouter, HTTPException

from anonymous_board.controller.request.create_anonymous_board_request import CreateAnonymousBoardRequest
from anonymous_board.controller.response.anonymous_board_response import AnonymousBoardResponse
from anonymous_board.service.anonymous_board_service_impl import AnonymousBoardServiceImpl

# @RequestMapping("/board")
# Controller, Service, Repository 객체 모두 싱글톤 구성
# Python의 특성상 이러한 IoC, DI 메커니즘이 취약
# Controller 역할을 하는 Router의 경우 자체적으로 싱글톤 구성을 가짐
anonymous_board_controller = APIRouter(prefix="/board")
board_service = AnonymousBoardServiceImpl.get_instance()

@anonymous_board_controller.post("/create",
                                 response_model=AnonymousBoardResponse)
def create_anonymous_board(request: CreateAnonymousBoardRequest):
    # 역할과 책임 관점에서 객체를 분리시키는 것이 더 좋음.
    # request로 퉁치는 것보다 request_form과 request를 분리시키는 것이 더 좋음.
    # 웹 페이지에서 요청하는 정보는 여러 도메인 정부를 전부 가지고 있으며, 여러 도메인 정보가 특정 도메인에 기록되는 구성
    # 따라서 위와 같이 request_form과 request를 분리하여, request에 역할과 책임을 갖게 함.
    create_board = board_service.create(request.title, request.content)

    return AnonymousBoardResponse(
        id=create_board.id,
        title=create_board.title,
        content=create_board.content,
        created_at=create_board.created_at
    )

@anonymous_board_controller.get("/list",
                                response_model=List[AnonymousBoardResponse])
def list_anonymous_boards():
    board_list = board_service.list()

    return [
        AnonymousBoardResponse(
            id=anonymous_board.id,
            title=anonymous_board.title,
            content=anonymous_board.content,
            created_at=anonymous_board.created_at.isoformat()
        ) for anonymous_board in board_list
    ]

@anonymous_board_controller.get("/{board_id}",
                                response_model=AnonymousBoardResponse)
def get_anonymous_board(board_id: str):
    try:
        anonymous_board = board_service.read(board_id)

    except ValueError:
        raise HTTPException(status_code=404, detail="Board not found")

    return AnonymousBoardResponse(
        id=anonymous_board.id,
        title=anonymous_board.title,
        content=anonymous_board.content,
        created_at=anonymous_board.created_at.isoformat()
    )
