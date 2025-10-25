from flask import Flask, render_template
app = Flask(__name__)
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 🔹 Ruta para la landing demo
@app.route('/')
def landing_demo():
    propiedad = {
        'titulo': 'Casa moderna en Monterrico',
        'descripcion': 'Hermosa casa con vista panorámica, rodeada de naturaleza. Ideal para descanso o inversión turística.',
        'precio': '$160,000',
        'imagenes': [
            'uploads/demo_casa1.jpg',
            'uploads/demo_casa2.jpg',
            'uploads/demo_casa3.jpg'
        ],
        'whatsapp': '50244851125'  # tu número en formato internacional sin +
    }
    return render_template('landing.html', propiedad=propiedad)

if __name__ == '__main__':
    app.run(debug=True)
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    

