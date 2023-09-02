import json


def extract_route(string):
    string_list = string.split(' ')
    route = string_list[1]
    new_string = route[1:]
    return new_string


def read_file(path):
    with open(path, 'rb') as f:
        return f.read()


def load_data(note):
    with open("data/" + note, 'r',encoding='utf-8') as archive:
        texto = archive.read()
    return json.loads(texto)


def load_template(template):
    with open("templates/" + template, 'r', encoding='utf-8') as archive:
        html = archive.read()
    return html


def write_on_file(dict):
    lista=load_data("notes.json")
    lista.append(dict)
    with open('data/notes.json','w', encoding='utf-8') as arquivo:
        return arquivo.write(json.dumps(lista,indent=4))

def build_response(body='', code=200, reason='OK', headers=''):
    response = ""
    if headers == '':
        response = "HTTP/1.1 " + str(code) + " " + \
            reason + headers + "\n\n" + body
    else:
        response = "HTTP/1.1 " + str(code) + " " + \
            reason + "\n" + headers + "\n\n" + body
    return str(response).encode()
