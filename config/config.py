class Config():
    def __init__(self):
        self.test = "Foo"
        self.validateConfig()

    def newConfig(self, test):
        self.test = test
        self.validateConfig()

    def validateConfig(self):
        print("test value: {}".format(self.test))
        print("Valid")
