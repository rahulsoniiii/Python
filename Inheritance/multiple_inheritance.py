class Father:
    name = "rakesh"
    strength = 78
class Mother:
    name = "Shruti"
    strength = 57
class Son(Father,Mother): #First Parameter has priority over second one
    name  = "ram"

f = Father()
m = Mother()
s = Son()
print(s.strength)
