from anonymous_board.repository.anonymous_board_repository_impl import AnonymousBoardRepositoryImpl
from anonymous_board.service.anonymous_board_service import AnonymousBoardService


class AnonymousBoardServiceImpl(AnonymousBoardService):
    # python 의 변수 구분 문법
    # '_' 없으면 public, 1개면 protected, 2개면 public
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.anonymous_board_repository = AnonymousBoardRepositoryImpl.get_instance()

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # 보편적으로 Spring 작업 시 아래와 같이 진행됨.
    # 1번째 패턴
    # @Autowired
    # AnonymousBoardService anonymousBoardService;

    # 2번째 패턴
    # @RequiredArgsConstructor
    # final AnonymousBoardService anonymousBoardService;

    # 3번째 패턴
    # 생성자에서 직접 주입
    # 문제 해결 시 항상 final 로 의존성 추가하므로 수 십개를 추가해도 저항 없음.
    # 일종의 경고가 필요함.

    def create(self, title: str, content: str):
        return self.__instance.anonymous_board_repository.create(title=title, content=content)
