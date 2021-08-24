class Wizard:
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.rootdir)
            else:
                print("No Operation")


if __name__ == "__main__":
    ## 클라이언트 코드
    wizard = Wizard('python3.5.gzip', '/usr/bin/')

    ## 사용자는 파이썬을 선택
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()
