from utils import load_data, load_template,write_on_file,build_response
from urllib.parse import unquote_plus
def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        print("/////sdfgvfdfgvbf/////")
        print(partes)
        
        print("--------------------parteropo")
        corpo = partes[-1]
        params = {}
        
        print("////////////corpo/////////")
        print(corpo)
        print("/////////////////")
        for chave_valor in corpo.split('&'):
           
            chave, valor = chave_valor.split('=')
            params[chave] = unquote_plus(valor)

        write_on_file(params)
        return build_response(code=303, reason='See Other', headers='Location: /')

   
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    print(notes_li)
    notes = '\n'.join(notes_li)
    
    response_body='index.html'.format(notes=notes)
    print("//////////////////////////////////")
    print(load_template('index.html').format(notes=notes).encode())
    print(build_response(body=load_template('index.html').format(notes=notes)))
    print("//////////////////////////////////")
    return build_response(body=load_template('index.html').format(notes=notes))