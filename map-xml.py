attribute_map = {
    "family": 1,
    "person": 2,
    "fistName": 3,
    "lastName": 4,
    "state": 5
}

def map_xml(s, out=[]):
    tag = s.split()[0][1:]
    s = s.split('>')[1].split()[1].split():
    out.append(attribute_map[tag])
    for e in s.split('>')[0].split()[1].split():
        name = e.split("=")[0]
        value = e.split("=")[1].strip("\"")
        out.append(attribute_map[name])
        out.append(value)
    if s:
        map_xml(s, out)
    out.append()

out = []
map_xml('''<family lastName="McDowell" state="CA"> <person firstName="Gayle">Some Message</person> </family>''', out)
print(out)




