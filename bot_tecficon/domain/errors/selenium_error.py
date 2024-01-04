
from . import Error


class SeleniumError(Error):

    def __init__(self):
        super().__init__(
            '''Lo sentimos, ha ocurrido un error durante la ejecución del bot, esto puede darse por problemas de conexión o por cambios en la página web. Por favor, intente de nuevo.''')
