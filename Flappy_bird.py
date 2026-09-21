# import random
# import tkinter as tk
#
#
# WIDTH = 480
# HEIGHT = 640
# GROUND_HEIGHT = 70
# PIPE_WIDTH = 72
# PIPE_GAP = 165
# PIPE_SPEED = 4
# GRAVITY = 0.45
# FLAP_STRENGTH = -8.5
#
#
# class FlappyBird:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Flappy Bird")
#         self.root.resizable(False, False)
#
#         self.canvas = tk.Canvas(
#             root,
#             width=WIDTH,
#             height=HEIGHT,
#             bg="#75c9e8",
#             highlightthickness=0,
#         )
#         self.canvas.pack()
#
#         self.keys = set()
#         self.running = False
#         self.score = 0
#         self.best_score = 0
#         self.bird_x = 120
#         self.bird_y = HEIGHT // 2
#         self.bird_velocity = 0
#         self.pipes = []
#
#         self.root.bind("<KeyPress>", self.on_key_press)
#         self.root.bind("<KeyRelease>", self.on_key_release)
#         self.canvas.bind("<Button-1>", lambda _event: self.flap())
#         self.show_start_screen()
#
#     def draw_background(self):
#         self.canvas.delete("all")
#         self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#75c9e8", outline="")
#         self.canvas.create_oval(35, 80, 145, 125, fill="#e8f7f8", outline="")
#         self.canvas.create_oval(105, 62, 210, 125, fill="#e8f7f8", outline="")
#         self.canvas.create_oval(310, 145, 415, 190, fill="#e8f7f8", outline="")
#         self.canvas.create_oval(375, 125, 470, 190, fill="#e8f7f8", outline="")
#         self.canvas.create_rectangle(
#             0, HEIGHT - GROUND_HEIGHT, WIDTH, HEIGHT, fill="#80bd45", outline=""
#         )
#         self.canvas.create_rectangle(
#             0, HEIGHT - GROUND_HEIGHT, WIDTH, HEIGHT - GROUND_HEIGHT + 12,
#             fill="#d6c15b", outline=""
#         )
#         for x in range(-20, WIDTH + 30, 35):
#             self.canvas.create_rectangle(
#                 x, HEIGHT - GROUND_HEIGHT, x + 18, HEIGHT - GROUND_HEIGHT + 8,
#                 fill="#f0df76", outline=""
#             )
#
#     def draw_bird(self):
#         x = self.bird_x
#         y = self.bird_y
#         self.canvas.create_oval(x - 19, y - 14, x + 20, y + 16, fill="#ffd447", outline="#bf8c19", width=2)
#         self.canvas.create_oval(x - 10, y + 2, x + 9, y + 13, fill="#f2b62d", outline="#bf8c19")
#         self.canvas.create_oval(x + 7, y - 10, x + 15, y - 2, fill="white", outline="#bf8c19")
#         self.canvas.create_oval(x + 11, y - 8, x + 14, y - 5, fill="#222222", outline="")
#         self.canvas.create_polygon(x + 18, y - 1, x + 34, y + 5, x + 18, y + 9, fill="#f08a2e", outline="#a8581d")
#
#     def draw_pipes(self):
#         for pipe in self.pipes:
#             x = pipe["x"]
#             gap_top = pipe["gap_top"]
#             gap_bottom = gap_top + PIPE_GAP
#             for top, bottom in ((0, gap_top), (gap_bottom, HEIGHT - GROUND_HEIGHT)):
#                 self.canvas.create_rectangle(x, top, x + PIPE_WIDTH, bottom, fill="#46ad55", outline="#267a39", width=3)
#             self.canvas.create_rectangle(x - 5, gap_top - 20, x + PIPE_WIDTH + 5, gap_top, fill="#56c763", outline="#267a39", width=3)
#             self.canvas.create_rectangle(x - 5, gap_bottom, x + PIPE_WIDTH + 5, gap_bottom + 20, fill="#56c763", outline="#267a39", width=3)
#
#     def draw_hud(self):
#         self.canvas.create_text(18, 18, anchor="nw", text=f"Score: {self.score}", fill="white", font=("Arial", 20, "bold"))
#         self.canvas.create_text(WIDTH - 18, 18, anchor="ne", text=f"Best: {self.best_score}", fill="white", font=("Arial", 14, "bold"))
#
#     def new_pipe(self, x=WIDTH + 30):
#         gap_top = random.randint(110, HEIGHT - GROUND_HEIGHT - PIPE_GAP - 70)
#         self.pipes.append({"x": x, "gap_top": gap_top, "scored": False})
#
#     def reset(self):
#         self.score = 0
#         self.bird_y = HEIGHT // 2
#         self.bird_velocity = 0
#         self.pipes = []
#         self.new_pipe(WIDTH + 80)
#         self.new_pipe(WIDTH + 330)
#
#     def show_start_screen(self):
#         self.draw_background()
#         self.draw_bird()
#         self.canvas.create_text(WIDTH // 2, 205, text="FLAPPY BIRD", fill="white", font=("Arial", 38, "bold"))
#         self.canvas.create_text(WIDTH // 2, 270, text="Click or press SPACE to flap", fill="#154b5c", font=("Arial", 17, "bold"))
#         self.canvas.create_text(WIDTH // 2, 325, text="Avoid the pipes and beat your best score", fill="#154b5c", font=("Arial", 13))
#         self.canvas.create_text(WIDTH // 2, 430, text="Click to start", fill="white", font=("Arial", 22, "bold"))
#
#     def start(self):
#         self.reset()
#         self.running = True
#         self.flap()
#         self.game_loop()
#
#     def flap(self):
#         if not self.running:
#             self.start()
#         else:
#             self.bird_velocity = FLAP_STRENGTH
#
#     def on_key_press(self, event):
#         if event.keysym == "space" and "space" not in self.keys:
#             self.keys.add("space")
#             self.flap()
#         elif event.keysym.lower() == "r" and not self.running:
#             self.start()
#
#     def on_key_release(self, event):
#         self.keys.discard(event.keysym)
#
#     def collides(self):
#         bird_left = self.bird_x - 17
#         bird_right = self.bird_x + 17
#         bird_top = self.bird_y - 12
#         bird_bottom = self.bird_y + 12
#         if bird_top <= 0 or bird_bottom >= HEIGHT - GROUND_HEIGHT:
#             return True
#         for pipe in self.pipes:
#             pipe_left = pipe["x"]
#             pipe_right = pipe_left + PIPE_WIDTH
#             inside_pipe_x = bird_right > pipe_left and bird_left < pipe_right
#             outside_gap = bird_top < pipe["gap_top"] or bird_bottom > pipe["gap_top"] + PIPE_GAP
#             if inside_pipe_x and outside_gap:
#                 return True
#         return False
#
#     def game_over(self):
#         self.running = False
#         self.best_score = max(self.best_score, self.score)
#         self.draw_background()
#         self.draw_pipes()
#         self.draw_bird()
#         self.draw_hud()
#         self.canvas.create_rectangle(65, 215, WIDTH - 65, 405, fill="#153f4f", outline="#e8f7f8", width=3)
#         self.canvas.create_text(WIDTH // 2, 260, text="GAME OVER", fill="#ffd447", font=("Arial", 32, "bold"))
#         self.canvas.create_text(WIDTH // 2, 315, text=f"Score: {self.score}    Best: {self.best_score}", fill="white", font=("Arial", 18, "bold"))
#         self.canvas.create_text(WIDTH // 2, 360, text="Click or press R to play again", fill="#e8f7f8", font=("Arial", 14))
#
#     def game_loop(self):
#         if not self.running:
#             return
#         self.bird_velocity += GRAVITY
#         self.bird_y += self.bird_velocity
#         for pipe in self.pipes:
#             pipe["x"] -= PIPE_SPEED
#             if not pipe["scored"] and pipe["x"] + PIPE_WIDTH < self.bird_x:
#                 pipe["scored"] = True
#                 self.score += 1
#         self.pipes = [pipe for pipe in self.pipes if pipe["x"] + PIPE_WIDTH > -10]
#         if not self.pipes or self.pipes[-1]["x"] < WIDTH - 230:
#             self.new_pipe()
#         if self.collides():
#             self.game_over()
#             return
#         self.draw_background()
#         self.draw_pipes()
#         self.draw_bird()
#         self.draw_hud()
#         self.root.after(20, self.game_loop)
#
#
# if __name__ == "__main__":
#     window = tk.Tk()
#     FlappyBird(window)
#     window.mainloop()

str = "Helpdisk"
print(len(str))

