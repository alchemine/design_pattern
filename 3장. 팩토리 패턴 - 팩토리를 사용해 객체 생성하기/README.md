# 3장. 팩토리(factory) 패턴 - 팩토리를 사용해 객체 생성하기  
### 1. 팩토리 패턴의 정의  
다른 클래스의 객체를 생성하는 팩토리(factory) 클래스를 사용하는 패턴

<br>


### 2. 팩토리 패턴의 특징  
- 객체 생성과 클래스 구현을 나눠 상호 의존도를 줄일 수 있음
- Client는 생성하려는 객체 클래스 구현과 상관없이 사용할 수 있음. (객체를 생성하기 위해 client가 알아야할 정보가 최소화됨)
- 코드를 수정하지 않고 팩토리에 새로운 클래스를 추가할 수 있음
- 이미 생성된 객체를 팩토리가 재활용할 수 있음

<br>


### 3. 팩토리 패턴의 세 가지 유형  
1. 심플 팩토리 패턴(Simple Factory Pattern) \
인터페이스는 객체 생성 로직을 숨기고 객체를 생성
2. **팩토리 메소드 패턴(Factory Method Pattern)** \
인터페이스를 통해 객체를 생성하지만 서브 클래스가 객체 생성에 필요한 클래스를 선택
3. 추상 팩토리 패턴(Abstract Factory Pattern) \
추상 팩토리는 객체 생성에 필요한 클래스를 노출하지 않고 객체를 생성하는 인터페이스로, 내부적으로 다른 팩토리 객체를 생성

#### 3.1 팩토리 메소드 vs 추상 팩토리 메소드
|팩토리 메소드|추상 팩토리 메소드|
|:---|:---|
|객체 생성에 필요한 메소드가 사용자에게 노출됨|관련된 객체 집단을 생성하기 위해 한 개 이상의 팩토리 메소드가 필요|
|어떤 객체를 생성할지 결정하는 상속과 서브 클래스가 필요|다른 클래스 객체를 생성하기 위해 composition을 사용|
|한 개의 객체를 생성하는 팩토리 메소드를 사용|관련된 객체 집단을 생성|

<br>


### 4. 일반적인 구현 방법(factory method pattern)
[B_factory_method_pattern.py](/3장.%20팩토리%20패턴%20-%20팩토리를%20사용해%20객체%20생성하기/B_factory_method_pattern.py)

```python
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass
class PersonalSection(Section):
    def describe(self):
        print("Personal Section")
class AlbumSection(Section):
    def describe(self):
        print("Album Section")
class PatentSection(Section):
    def describe(self):
        print("Patent Section")
class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()
    @abstractmethod
    def createProfile(self):
        pass
    def getSections(self):
        return self.sections
    def addSections(self, section):
        self.sections.append(section)
class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())
class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == '__main__':
    profile_type = input("which Profile you'd like to create? [LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.getSections())
```
