class tanmay(object):
    def __init__(self,name):
        self.name=name
    def change(self):
        return 'tanmay'+self.name
class lakshya(tanmay):
    def __init__(self,name):
        self.name=name
    def change(self):
        return super(lakshya,self).change()+'kkkk'
