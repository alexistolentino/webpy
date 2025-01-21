import web

# Definición de las rutas
urls = (
    '/hello/(.*)', 'hello',  # Ruta para saludar
    '/goodbye/(.*)', 'goodbye'  # Ruta para despedirse
)
app = web.application(urls, globals())

# Clase para manejar el saludo
class hello:
    def GET(self, name):
        if not name:  # Si no se proporciona un nombre
            name = 'World'
        return 'Hello, ' + name + '!'

# Clase para manejar la despedida
class goodbye:
    def GET(self, name):
        if not name:  # Si no se proporciona un nombre
            name = 'everyone'
        return 'Goodbye, ' + name + '!'

if __name__ == "__main__":
    app.run()