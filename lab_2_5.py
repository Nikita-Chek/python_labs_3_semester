def string_(Object):
    if type(Object) is float:
        return '%f' %Object 
    if type(Object) is int:
        return '%i' %Object
    if Object is None:
        return 'null'
    if type(Object) is str:
        return '"' + Object + '"'
    if type(Object) is list:
        return string_list(Object)
    if type(Object) is tuple:
        return string_list(Object)
    if type(Object) is dict:
        return string_dict(Object)
    if Object:
        return 'true'
    if not Object:
        return 'false'
    return ValueError

def string_list(list_, s='['):
    for _ in list_:
        s += string_(_) + ', '
    s = s[:-2] + ']'
    return s

def string_dict(dictionary, s='{'):
    for _ in dictionary:
        s += string_(_) + ': ' + string_(dictionary[_]) + ', '
    s = s[:-2] + '}'
    return s

def to_json(Object, file=False):
    wrt = '{"json": ' + string_(Object) + '}'
    if file:
        file = open('additional/for_five.json', 'w')
        file.write(wrt)
    return wrt

#to_json([34,'er', ['34', True]], True)
