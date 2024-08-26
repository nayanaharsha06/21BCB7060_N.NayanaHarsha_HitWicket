from flask import Flask, request, jsonify, send_from_directory
from logic import Game

app = Flask(__name__, static_folder='game_server', static_url_path='')

game_instance = Game()

@app.route('/start_game', methods=['POST'])
def start_game():
    game_instance.start_game()
    return jsonify({"message": "Game started", "board_state": game_instance.curr_board_state()}), 200

@app.route('/move', methods=['POST'])
def make_move():
    data = request.json
    player = data.get('player')
    figure_name = data.get('figure_name')
    direction = data.get('direction')
    
    if not player or not figure_name or not direction:
        return jsonify({"error": "Missing parameters"}), 400
    
    success = game_instance.move(player, figure_name, direction)
    
    if success:
        return jsonify({"message": "Move successful", "board_state": game_instance.curr_board_state()}), 200
    else:
        return jsonify({"error": "Move failed"}), 400

@app.route('/board_state', methods=['GET'])
def get_board_state():
    return jsonify({"board_state": game_instance.curr_board_state()}), 200

@app.route('/')
def index():
    return send_from_directory('game_server', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
