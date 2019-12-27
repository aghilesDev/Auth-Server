class Mapper:
    def mapp(obj,myClass):
        p=myClass()
        if p.__dict__.keys()==obj.__dict__.keys():
            p.__dict__=obj.__dict__
        else:
            p=None
    return p
