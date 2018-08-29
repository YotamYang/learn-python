
class Hello:

    def __init__(self, name):
        self.name = name

    def sysHello(self):
        print('Hello {0}'.format(self.name))

class Hi(Hello):

    def __init__(self):
        Hello.__init__(self, 'zhangSan')

    def sayHi(self):
        print('Hi {0}'.format(self.name))

h = Hello('python')
h.sysHello()

hi = Hi()
hi.sysHello()
hi.sayHi()

