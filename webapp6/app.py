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

        for i in range(5):
            print(i)
if __name__ == "__main__":
    app.run()