# 6장. 옵서버 패턴 - 객체 이해하기
## 6.1 행위 패턴 개요(The Behavior Design Pattern)
1. 생성 패턴(싱글톤), 구조 패턴(퍼사드)에 이은 세 번째 디자인 패턴
2. 생성 패턴에서는 객체가 생성되는 방식이 중요
3. 객체가 생성되는 세부 과정을 숨기고 생성하려는 객체 형과 독립적인 구조를 지원
4. 객체와 클래스를 합쳐 더 큰 기능을 구현
5. 구조를 간소화하고 클래스와 객체 사이의 관계를 찾는 것이 주목적


<br>

## 6.2 옵서버 패턴 이해
옵서버 패턴에서 객체(subject)는 자식(옵서버, observer)의 목록을 유지하며 subject가 옵서버에 정의된 메소드를 호출할 때마다 옵서버에 이를 알린다.

### 6.2.1 옵서버 패턴의 목적
- 객체 간 일대다 관계를 형성하고 객체의 상태를 다른 종속 객체에 자동으로 알림
- Subject의 핵심 부분을 캡슐화

### 6.2.2 옵서버 패턴이 적합한 상황
- 분산 시스템의 이벤트 서비스를 구현
- 뉴스 에이전시 프레임워크
- 주식 시장 모델


<br>

## 6.3 옵서버 패턴의 구성원
1. **Subject** \
여러 개의 observer들을 관리
2. **Observer** \
Subject를 감시하는 객체를 위한 인터페이스를 제공 \
Subject의 상태를 알 수 있도록 ConcreteObserver가 구현해야 하는 메소드를 정의
3. **ConcreteObserver** \
Subject의 상태를 저장 \
Subject에 대한 정보와 실제 상태를 일관되게 유지하기 위해 Observer 인터페이스를 구현


<br>

## 6.4 옵서버 패턴 메소드
Subject의 변경 사항을 Observer에 알리는 2가지 방법: **Pull**, **Push**

### 6.4.1 Pull model
Pull model에서 Observer의 역할
1. Subject는 변경 사항이 있음을 등록된 Observer에 브로드캐스트함
2. Observer는 직접 게시자에게 변경 사항을 요청하고 끌어와야함(pull)
3. Pull model은 Subject가 Observer에 알리는 단계와 Observer가 Subject로부터 필요한 데이터를 받아오는 두 단계가 필요하므로 **비효율적**

### 6.4.2 Push model
Push model에서 Subject의 역할
1. Subject가 Observer에 데이터를 보냄
2. Subject는 Observer가 필요로 하지 않는 데이터까지 보낼 수 있기 때문에, 응답 시간이 늦어질 수 있음
3. 성능을 위해 Subject는 오직 필요한 데이터만을 보내야함


<br>

## 6.5 느슨한 결합과 옵서버 패턴
> **느슨한 결합(Loose coupling)** \
상호 작용하는 객체 간의 관계(결합, 서로 알고 있는 정도)를 최대한 느슨하게 구성하는 SW 어플레이케이션 설계 원칙

### 6.5.1 느슨한 결합의 효과
- 한 부분에 대한 수정이 예기치 않게 다른 부분까지 영향을 끼치는 위험을 줄임
- 테스트와 유지 보수 및 장애 처리가 쉬움
- 시스템을 쉽게 여러 부분으로 분리할 수 있음


### 6.5.2 Subject와 Observer의 느슨한 결합을 추구하는 옵서버 패턴
- Subject는 Observer가 어떤 인터페이스를 구현하는지 모르고 ConcreteObserver의 존재를 알지 못함
- 언제든지 새로운 Observer를 추가할 수 있음
- Observer가 추가됨에 따라 Subject를 수정할 필요가 없음
- Subject 또는 Observer는 독립적으로 재사용될 수 있음
- Subject 또는 Observer에 대한 수정이 서로에게 아무런 영향을 주지 않음


<br>

## 6.6 옵서버 패턴의 장단점
### 장점
- 객체 간의 느슨한 결합 원칙을 따름
- Subject 또는 Observer 클래스를 수정하지 않고 객체 간 자유롭게 데이터를 주고받을 수 있음
- 새로운 Observer를 언제든지 추가/제거할 수 있음

### 단점
- ConcreteObserver는 상속을 통해 Observer 인터페이스를 구현하기 때문에 컴포지션에 대한 선택권이 없음
- 제대로 구현되지 않은 Observer 클래스는 복잡도를 높이고 성능 저하의 원인이 될 수 있음
- 애플리케이션에서 알림(notification) 기능은 간혹 신뢰할 수 없으며 레이스 상태(race condition) 또는 비일관성을 초래할 수 있음
