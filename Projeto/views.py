from database import Database,Note
from utils import load_template,build_response,extract_route
from urllib.parse import unquote_plus

def index(request):
    
    
    db= Database('data/banco')
    verifica=extract_route(request)
    if request.startswith('POST') and 'update' not in verifica:
        print(request)
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        print(partes) 
        corpo = partes[-1]
        if corpo !='':
            b=corpo.split("&")
            topicos=b[0].split('=')
            c=b[1].split('=')
            
            db.add(Note(title=unquote_plus(topicos[1]),content=unquote_plus(c[1])))
        return build_response(code=303, reason='See Other', headers='Location: /')
    
    if 'delete' in extract_route(request) and 'img' not in verifica:
        
        v=verifica.split('/')
        
        db.delete(v[1].replace('?',''))
        return build_response(code=303, reason='See Other', headers='Location: /')
    
    if 'reenvio' in extract_route(request) and 'img' not in verifica:
        v=verifica.split('/')
        ident=v[1].replace('?','')
        ident=int(ident)
        print(ident)

        
        dado=db.get(ident)
        print('/'*100)
        print(dado.title)
        print('/'*100)
        return build_response(body=load_template('edit.html').format(id=ident,titulo=dado.title,conteudo=dado.content))
    if 'update' in extract_route(request):
        v=verifica.split('/')

        ident=v[1]
        ident=int(ident)
        print('/////////////')
        print(ident)
        
        dado=db.get(ident)
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        print(partes) 
        corpo = partes[-1]
        if corpo !='':
            b=corpo.split("&")

            
            topicos=b[0].split('=')
            c=b[1].split('=')
            print(c)
            print('q'*10)
            print(b)
            print(topicos)
            if topicos[1]==None:
                print(2)
            print('q'*10)
            if topicos[1]=='' and c[1] !='':
                print(0)
                db.update(Note(id=ident,title=dado.title,content=unquote_plus(c[1])))
            elif c[1]=='' and topicos[1] !='':
                print(1)
                db.update(Note(id=ident,title=unquote_plus(topicos[1]),content=dado.content))
            elif c[1]=='' and topicos[1]=='':
                print(2)
                db.update(Note(id=ident,title=dado.title,content=dado.content))
            else:  
                print(3)  
                db.update(Note(id=ident,title=unquote_plus(topicos[1]),content=unquote_plus(c[1])))
    
        return build_response(code=303, reason='See Other', headers='Location: /')
        
        


   
    note_template = load_template('components/note.html')
    
    notes_li = [
        note_template.format(title=dados.title, content=dados.content,id=dados.id)
        for dados in db.get_all()
    ]
    notes = '\n'.join(notes_li)

    


    return build_response(body=load_template('index.html').format(notes=notes)) 