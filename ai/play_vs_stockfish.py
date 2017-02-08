from stockfish import Stockfish
import chess

board = chess.Board()

stockfish = Stockfish()

moves = []

while True:
	moves.append(input("Next Move:"))
	stockfish.set_position(moves)
	board.push(chess.Move.from_uci(moves[len(moves)-1]))


	moves.append(stockfish.get_best_move())
	stockfish.set_position(moves)
	board.push(chess.Move.from_uci(moves[len(moves)-1]))

	print("computer made move:",moves[len(moves)-1])
	print(board)
