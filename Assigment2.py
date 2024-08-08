#Python string method

# 1 Case fold example
text = "MANIK"
a = text.casefold()
print (a)

# 2 Uppercase example
text = "The person who grew these was located in Central California and, er, hopefully very well-compensated."
b = text.upper()
print (b)

# 3 center example
text = "Aayusha Shrestha real name is dusha shrestha"
c = text.center(100)
print (c)

# 4 String count
text = "Aayusha Shrestha real name is dusha shrestha, Aayusha is from biratnagar-5, Aayusha loves to doing kichkich, Aayusha loves beer so much"
d = text.count("Aayusha")
print (d)

# 5 endswitch
text = "Aayusha Shrestha real name is dusha shrestha, Aayusha is from biratnagar-5, Aayusha loves to doing kichkich, Aayusha loves beer so much"
e = text.endswith(".")
print (e)

# 6 Expandtabs
text = "A\tA\tY\tU\tS\tH\tA"
f = text.expandtabs(20)
print (f)

# 7 find
txt = "Hello, welcome to my world."

x = txt.find("world")

print(x)


# 8 format
text2 = "The price of 1 kg apple is {price:.2f} ruppes."
print (text2.format(price=250))

# 9 string is decimal
text3 = "1250"
h = text3.isdecimal()
print(h)

# 10 string is digit
text4 = '88789'
i = text4.isdigit()
print(i)