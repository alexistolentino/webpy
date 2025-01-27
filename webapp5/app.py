import web
import json

urls = (
    '/', 'index'
)

app = web.application(urls, globals())
render = web.template.render('views')

class index:
    def GET(self):
        # Renderiza la página HTML
        return render.index()

    def POST(self):
        # Captura los datos enviados desde el formulario
        form = web.input()
        nombre = form.nombre
        email = form.email

        # Construye la respuesta como JSON
        response = {
            "nombre": nombre,
            "email": email
        }
        return json.dumps(response)  # Convierte el diccionario en JSON

if __name__ == "__main__":
    app.run()
