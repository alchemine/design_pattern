# 2장. 싱글톤(Singleton) 디자인 패턴  
### 1. 싱글톤 디자인 패턴의 정의  
글로벌하게 접근 가능한 하나의 객체를 제공하는 패턴

<br>

### 2. 싱글톤 디자인 패턴의 목적  
- 클래스에 대한 단일 객체 생성
- 전역 객체 제공
- 공유된 리소스에 대한 동시 접근 제어

<br>

### 3. 싱글톤 디자인 패턴의 특징  
- 스레드 풀과 캐시, 대화 상자, 레지스트리 설정 등 한 개의 객체만 필요한 경우 싱글톤 패턴을 사용하여 리소스를 관리
- 전역 변수를 수정하면 종속된 모든 class에 의도하지 않은 영향을 줄 수 있음

<br>

### 4. 일반적인 구현 방법 
[E1_example.py](/2장.%20싱글톤%20디자인%20패턴/E1_example.py)

```python
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
```
