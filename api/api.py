#Objetivo: Criar uma api para calcular o teorema de pitágoras.
import math #Trazendo uma biblioteca do proprio python de soma.
from flask import Flask , request, jsonify #Puxando as dependências que serão utilizadas no projeto.
from  flask_cors import CORS

app = Flask(__name__)
CORS(app) #Aplicando o cors para que assim, seja feito requisições no site.

@app.route('/')
def apiRequest(): #Criação da função da api
  
  try: #Elaborando um try para caso uma letra seja colocada dentro de um parâmentro de número, assim sendo indetificado pelo ValueError.
    ladoA = int(request.args.get('ladoa')) #Conversão sobre os "números" de maneira string para int.
    ladoB = int(request.args.get('ladob'))
    
    def hipotenusa(ladoA,ladoB): #Função básica de cálculo do teorema de pitágoras.
          ladoC = math.sqrt( ladoA * ladoA + ladoB * ladoB )
          return ladoC 

    person = {"result": hipotenusa(ladoA,ladoB)} #Criação de um json de maneira básica para resposta dos request em json.
    return jsonify(person) #Utilização de uma biblioteca do Flask para conversão para json.
  except ValueError:#Usando o parâmentro de erro "ValueError" para incapacitar o uso de string nos request da api.
     person = {"result": "Error"} #Resultado informado em casos de erro, em formato json.
     return jsonify(person)#Aplicação do json para a interface do usuário/request.
   

if __name__ == '__main__':
    app.run(debug=True)#Execução do python, caso seja necessário alteração da porta da api.
    
