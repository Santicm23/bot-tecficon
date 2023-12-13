
import os


temp = os.getenv('TOK')

assert temp is not None, 'Environment variable TOK is not set'
TOK: str = temp

BASE_URL = 'http://10.8.0.1:8090/scriptcase/app/Hurtado_Gandini'
