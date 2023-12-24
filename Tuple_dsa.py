# nested tuple

l = [12,23,41,52]
d = {"java" :"programming", "one" : "two"}

my_tuple = ("mouse",l,d, [8, 4, 6], (1, 2, 3))
print(my_tuple)

my_tuple[1].append(12)

d.update({"three" : "four"})

print(my_tuple)

print(type(my_tuple))