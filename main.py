from flask import Flask, jsonify, request
import json

app = Flask(__name__)

devs = [
    {'nome':'rafael',
     'habilidades':['Python','Flask']
     },
    {'nome':'Gallenai',
     'habilidades':['python','Django']}
]

@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            dev = devs[id]
        except IndexError:
            dev = {'status':'dev não existe'}
        except Exception:
            dev = {'status':'erro desconhecido'}

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status':'registro excluido'})

    return dev

@app.route('/dev/', methods=['GET','POST'])
def listaDevs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        devs.append(dados)
        idnovo = len(devs)
        return jsonify({'status':'sucesso registro inserido','id':idnovo})
    elif request.method == 'GET':
        return jsonify(devs)



if __name__=='__main__':
    app.run(debug=True)
