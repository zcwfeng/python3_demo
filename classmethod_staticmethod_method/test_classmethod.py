def get_no_of_instances(cls_obj):
    return cls_obj.no_inst
class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1
ik1 = Kls()
ik2 = Kls()
print(get_no_of_instances(Kls))



def iget_no_of_instance(ins_obj):
    return ins_obj.__class__.no_inst
class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1
ik1 = Kls()
ik2 = Kls()
print(iget_no_of_instance(ik1))


# class Kls(object):
#     no_inst = 0
#     def __init__(self):
#         Kls.no_inst = Kls.no_inst + 1
#     @classmethod
#     def get_no_of_instance(cls_obj):
#         return cls_obj.no_inst
# ik1 = Kls()
# ik2 = Kls()
# print(ik1.get_no_of_instance())
# print(Kls.get_no_of_instance())
