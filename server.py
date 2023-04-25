from flask import Flask, request
import test
app = Flask(__name__)

# executar o comando "flask -A server.py run"
# pra iniciar o servidor
@app.route('/', methods=["GET"])
def healthcheck():
    return "OK"

# Fonte: https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/?highlight=file
# Como subir um arquivo com Flask em python
# Decorator para mapear rota do servidor com metodo post e endpoint '/upload'
@app.route('/upload', methods=['POST'])
def upload_file():
    print(request.files)
    if 'file' not in request.files:
        return "Sem arquivo"
    
    print('Arquivo recebido')
    
    file = request.files['file']
    
    # valida tipo do arquivo
    # se for csv
    # então faz o processamento dos cpfs
    if allowed_file( file.filename ):
        print('CSV recebido !')
        print('Começar a processar os CPFs !')
        
        test.processar( file )

        return ('CSV processado !')
  
    # se não for csv, termina
    print('Arquivo não é compatível')
    return 'Arquivo não é compatível'

# Valida se o arquivo é do tipo csv
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'csv'}

if __name__ == '__main__':
    print(__name__)
    # permite que seja rodado o servidor direto com python
    app.run()
