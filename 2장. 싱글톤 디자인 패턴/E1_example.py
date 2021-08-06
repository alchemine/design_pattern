### 데이터베이스 기반 애플리케이션에서 적용된 싱글톤 패턴

## 안정된 클라우드 서비스를 설계하기 위한 주의사항
##  1. DB 작업 간의 일관성이 유지돼야 한다. 작업 간 충돌이 발생하지 않아야 한다.
##  2. 다수의 DB 연산을 처리하려면 메모리와 CPU를 효율적으로 사용해야 한다.


import sqlite3


class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj  = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

print("Database Objects DB1", db1)
print("Database Objects DB2", db2)
