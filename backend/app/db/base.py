from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: int
    __name__: str

    # 자동으로 테이블 이름을 생성
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
