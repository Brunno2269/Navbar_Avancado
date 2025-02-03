from flask import Flask, render_template, jsonify
import logging

app = Flask(__name__)

# Configuração de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    logger.info("Carregando página inicial...")
    return render_template('index.html')

@app.route('/about')
def about():
    logger.info("Carregando página Sobre...")
    return render_template('about.html')

@app.route('/services')
def services():
    logger.info("Carregando página Serviços...")
    return render_template('services.html')

@app.route('/contact')
def contact():
    logger.info("Carregando página Contato...")
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    logger.warning(f"Página não encontrada: {e}")
    return render_template('404.html'), 404

if __name__ == '__main__':
    logger.info("Iniciando servidor Flask...")
    app.run(debug=True)