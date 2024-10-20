import subprocess
from stockfish import Stockfish

# Set paths to your engines
stockfish_path = "sf.exe" 
lc0_path = "lc0.exe" 

# Function to set options for Stockfish (multithreading, hash size, etc.)
def configure_stockfish(stockfish):
    stockfish._set_option("Threads", 24)  # Adjust the number of CPU threads
    stockfish._set_option("Hash", 2048)    # Set the hash size (in MB)

# Function to get the best move from Stockfish
def get_stockfish_best_move(fen):
    stockfish.set_fen_position(fen)
    return stockfish.get_best_move()

# Function to get the best move from LC0 (CUDA version)
def get_lc0_best_move(fen):
    weights_file = "bt4-1740.pb"  # Replace with your actual weights file path
    process = subprocess.Popen([lc0_path, 
                                "--backend=cuda-fp16", 
                                f"--weights={weights_file}"], 
                               stdin=subprocess.PIPE, 
                               stdout=subprocess.PIPE, 
                               text=True)

    # Sending UCI commands to LC0 to set up the position
    process.stdin.write("uci\n")
    process.stdin.write(f"position fen {fen}\n")
    process.stdin.write("go movetime 6500\n")
    process.stdin.flush()

    best_move = ""
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if "bestmove" in output:
            best_move = output.split()[1]
            break
        print(output.strip())  # Print the output for debugging

    process.terminate()  # Close LC0 process
    return best_move


# Main program to choose engine and calculate best move
if __name__ == "__main__":
    engine_choice = input("Which engine do you want to use? (1: Stockfish, 2: LC0): ")

    fen_input = input("Enter the FEN string of the chess position: ")

    if engine_choice == "1":
        # Use Stockfish
        stockfish = Stockfish(stockfish_path)
        configure_stockfish(stockfish)
        best_move = get_stockfish_best_move(fen_input)
        print(f"The best move from Stockfish is: {best_move}")
    elif engine_choice == "2":
        # Use LC0 (CUDA version)
        best_move = get_lc0_best_move(fen_input)
        print(f"The best move from LC0 is: {best_move}")
    else:
        print("Invalid choice. Please select either '1' for Stockfish or '2' for LC0.")