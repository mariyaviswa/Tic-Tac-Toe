import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import threading

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.root, text="", font=('Arial', 24), width=5, height=2,
                                bg="white", fg="black",
                                command=lambda r=row, c=col: self.handle_click(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def handle_click(self, row, col):
        if self.buttons[row][col]['text'] == "" and not self.check_winner():
            self.play_click_sound()
            self.buttons[row][col]['text'] = self.current_player
            self.board[row][col] = self.current_player

            # Color based on player
            if self.current_player == "X":
                self.buttons[row][col].config(fg="blue")
            else:
                self.buttons[row][col].config(fg="red")

            if self.check_winner():
                messagebox.showinfo("Game Over", f"🎉 Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "🤝 It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != '':
                self.highlight_win([(i, 0), (i, 1), (i, 2)])
                return True
            if b[0][i] == b[1][i] == b[2][i] != '':
                self.highlight_win([(0, i), (1, i), (2, i)])
                return True
        if b[0][0] == b[1][1] == b[2][2] != '':
            self.highlight_win([(0, 0), (1, 1), (2, 2)])
            return True
        if b[0][2] == b[1][1] == b[2][0] != '':
            self.highlight_win([(0, 2), (1, 1), (2, 0)])
            return True
        return False

    def highlight_win(self, cells):
        for row, col in cells:
            self.buttons[row][col].config(bg="lightgreen")

    def check_draw(self):
        return all(self.board[row][col] != '' for row in range(3) for col in range(3))

    def reset_board(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                btn = self.buttons[row][col]
                btn.config(text="", bg="white", fg="black")
        self.current_player = "X"

    def play_click_sound(self):
        threading.Thread(target=playsound, args=('click.mp3',), daemon=True).start()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
