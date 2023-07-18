from flask import Flask, request, jsonify

app = Flask(__name__)


class Jugador:
    def __init__(self, movimientos, golpes, nombre):
        self.movimientos = movimientos
        self.golpes = golpes
        self.nombre = nombre
        self.energia = 6

    def calcular_energia(self, golpe):
        if golpe == 'P':
            self.energia = max(0, self.energia - 1)
        elif golpe == 'K':
            self.energia = max(0, self.energia - 2)

    def realizar_movimiento(self, movimiento):
        return f'{self.nombre} realiza el movimiento {movimiento}'

    def ejecutar_golpe(self, golpe):
        return f'{self.nombre} ejecuta el golpe {golpe}'


@app.route('/pelea', methods=['POST'])
def ejecutar_pelea():
    pelea = request.json

    # Crear instancia del jugador 1
    player1 = Jugador(pelea['player1'].get('movimientos', []), pelea['player1'].get('golpes', []), 'Tonyn')

    # Crear instancia del jugador 2
    player2 = Jugador(pelea['player2'].get('movimientos', []), pelea['player2'].get('golpes', []), 'Arnaldor')

    resultado = []

    # Iterar sobre los movimientos y golpes de ambos jugadores
    for movimiento_player1, golpe_player1, movimiento_player2, golpe_player2 in zip(player1.movimientos, player1.golpes,
                                                                                    player2.movimientos,
                                                                                    player2.golpes):
        # Realizar movimiento del jugador 1 y agregar al resultado
        resultado.append({'accion': player1.realizar_movimiento(movimiento_player1)})

        if golpe_player1:
            # Ejecutar golpe del jugador 1, actualizar la energía del jugador 2 y agregar al resultado
            resultado.append({'accion': player1.ejecutar_golpe(golpe_player1)})
            player2.calcular_energia(golpe_player1)

        # Realizar movimiento del jugador 2 y agregar al resultado
        resultado.append({'accion': player2.realizar_movimiento(movimiento_player2)})

        if golpe_player2:
            # Ejecutar golpe del jugador 2, actualizar la energía del jugador 1 y agregar al resultado
            resultado.append({'accion': player2.ejecutar_golpe(golpe_player2)})
            player1.calcular_energia(golpe_player2)

        # Verificar si algún jugador ha perdido toda su energía
        if player1.energia == 0:
            resultado.append({'accion': f'{player2.nombre} Gana la pelea y le queda {player2.energia} de energía'})
            break
        elif player2.energia == 0:
            resultado.append({'accion': f'{player1.nombre} Gana la pelea y le queda {player1.energia} de energía'})
            break

    # Devolver el resultado de la pelea como una respuesta JSON
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
            result =
            [
            
                    {
                        "accion": "Tonyn realiza el movimiento D"
                    },
                    {
                        "accion": "Tonyn ejecuta el golpe K"
                    },
                    {
                        "accion": "Arnaldor realiza el movimiento SA"
                    },
                    {
                        "accion": "Tonyn realiza el movimiento S"
                    },
                    {
                        "accion": "Arnaldor realiza el movimiento ASA"
                    },
                    {
                        "accion": "Arnaldor ejecuta el golpe P"
                    },
                    {
                        "accion": "Tonyn realiza el movimiento SD"
                    },
                    {
                        "accion": "Tonyn ejecuta el golpe P"
                    }
            ]
    '''"""
