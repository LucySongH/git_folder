import turtle as t
import winsound
import time
import random

# 기본 설정
t.bgcolor("lightgreen")
t.up()
t.speed(0)
t.goto(0,220)
t.write("Turtle Race",False,"center",("",35))

# 레이스 경기장 그리기
t.goto(-400,170)
t.down()
t.color("brown")
t.begin_fill()
for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(400)
    t.right(90)
t.end_fill()

#결승선 그리기
t.color("black")
t.up()
t.goto(330,200)
t.down()
t.goto(330,-250)

# 터틀 선수 생성
start_ycor = [150,90,30,-30,-90,-150,-210]
color_list = ["white","pink","black","lightblue","green","red","blue"]
turtles = []
for i in range(7):
    new_turtle = t.Turtle()
    new_turtle.up()
    new_turtle.shape("turtle")
    new_turtle.color(color_list[i])
    new_turtle.goto(-370,start_ycor[i]) 
    new_turtle.write(i)
    new_turtle.goto(-350,start_ycor[i]) #출발선
    turtles.append(new_turtle)

# 레이스 라인
for i in range(6):
    t.up()
    t.goto(-400, start_ycor[i] -30)
    t.color("white")
    t.down()
    t.goto(400, start_ycor[i] -30)

# 배팅하기
user_choice = int(t.textinput("Turtle Race","which turtle is winning?"))
t.up()
t.goto(0,-290)
t.color("black")
t.write(f"you are betting at {user_choice}",False,"center",("",30))

#경기 시작 알림
winsound.Beep(523, 300)
time.sleep(0.3)
#경기 시작
game_over = False
while not game_over:
    for i in turtles:
        rand_speed = random.randint(1,10)
        i.forward(rand_speed)
        if i.xcor() > 330:
            game_over = True

# 1등 찾기
max_xcor = 0
winner = 0
for i in range(len(turtles)):
    if turtles[i].xcor() > max_xcor:
        max_xcor = turtles[i].xcor()
        winner = i

# 배팅 결과 발표
t.goto(0,0)
if user_choice == winner:
    t.write("succeed!",False,"center",("",30))
else:
    t.write(f"fail! The winner is No.{winner}",False,"center",("",30))
