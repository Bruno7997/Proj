# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():
    return render_template('index.html' , name = "EBr" , age = "14")

# defina a rota para a página do pai
@app.route("/P")
def P():return render_template('pai.html' , name = "Mon" , age = "35")

# defina a rota para a página da mãe
@app.route("/M")
def M():return render_template('mae.html' , name = "FF" , age = "34")

# defina a rota para a página do amigo
@app.route("/A")
def A():return render_template('amigo.html' , name = "Ju" , age = "16")

# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
