from turtle import Turtle
class Score :
    def __init__(self):
        self.score=0
        self.scoreboard=Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0,260)
        self.scoreboard.penup()
        self.scoreboard.color("white")
        self.scoreboard.write(f"score:{self.score}",align="center",font=("Courier",24,"normal"))
    
    def update_score(self):
        self.score+=1
        self.scoreboard.clear()
        self.scoreboard.write(f"score:{self.score}",align="center",font=("Arial",24,"normal"))

    def game_over(self):
        self.scoreboard.goto(0,0)
        self.scoreboard.write(f"Game Over",align="center",font=("Courier",24,"normal"))