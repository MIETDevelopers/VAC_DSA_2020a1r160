## Variable length, with keyword.
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s : %s" % (key, value))

myFun(Name="Ishav Vemra", RollNumber="2020a1r160")