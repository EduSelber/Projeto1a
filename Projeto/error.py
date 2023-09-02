from database import Database,Note
from utils import load_template,build_response,extract_route
from urllib.parse import unquote_plus
def er():
    return build_response(body=load_template('erro.html')) 