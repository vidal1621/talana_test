from flask import Flask, request, jsonify

app = Flask(__name__)


def calcular_energia(energia, golpe):
    if golpe == 'P':
        return max(0, energia - 1)
    elif golpe == 'K':
        return max(0, energia - 2)
    else:
        return energia


@app.route('/pelea', methods=['POST'])
def ejecutar_pelea():
    pelea = request.json
    player1 = pelea['player1']
    player2 = pelea['player2']
    movimientos_player1 = player1.get('movimientos', [])
    golpes_player1 = player1.get('golpes', [])
    movimientos_player2 = player2.get('movimientos', [])
    golpes_player2 = player2.get('golpes', [])
    energia_player1 = 6
    energia_player2 = 6
    turno = 1
    resultado = []

    for movimiento_player1, golpe_player1, movimiento_player2, golpe_player2 in zip(movimientos_player1, golpes_player1,
                                                                                    movimientos_player2,
                                                                                    golpes_player2):
        if turno == 1:
            resultado.append({'accion': f'Tonyn realiza el movimiento {movimiento_player1}'})
            if golpe_player1:
                resultado.append({'accion': f'Tonyn ejecuta el golpe {golpe_player1}'})
                energia_player2 = calcular_energia(energia_player2, golpe_player1)
        else:
            resultado.append({'accion': f'Arnaldor realiza el movimiento {movimiento_player2}'})
            if golpe_player2:
                resultado.append({'accion': f'Arnaldor ejecuta el golpe {golpe_player2}'})
                energia_player1 = calcular_energia(energia_player1, golpe_player2)

        turno = 2 if turno == 1 else 1

        if energia_player1 == 0:
            resultado.append(
                {'accion': f'Arnaldor Shuatseneguer Gana la pelea y le queda {energia_player2} de energía'})
            break
        elif energia_player2 == 0:
            resultado.append({'accion': f'Tonyn Stallone Gana la pelea y le queda {energia_player1} de energía'})
            break

    return jsonify(resultado)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    """json_data = '''
{
  "player1": {
    "movimientos": ["D","DSD","S","DSD","SD"],
    "golpes": ["K","P","","K","P"]
  },
  "player2": {
    "movimientos": ["SA","SA","SA","ASA","SA"],
    "golpes": ["K","","K","P","P"]
  }
}
'''"""
