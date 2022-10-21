import turtle
import pandas

# Verileri okuyup bir sözlük haline getirme
data = pandas.read_csv("50_states.csv")
data_x_coord = data["x"]
data_states = data["state"]
data_y_coord = data["y"]
data_dict = {}
for i in range(0, len(data)):
    data_dict[data_states[i]] = [int((data_x_coord[i])), int((data_y_coord[i]))]


# Ekran oluşturma
image = "blank_states_img.gif"
ekran = turtle.Screen()
ekran.addshape(image)
turtle.shape(image)


#Gerekli değişkenleri atıyoz
guessed_state = []
devamMi = True


# Tahmin
while len(guessed_state) < 50 and devamMi == True:
    user_state = ekran.textinput(f"{len(guessed_state)}/50", "What's another state name?")
    if user_state == "quit":
        devamMi = False
    for i in range(0, len(data_states)):
        if data_states[i].lower() == user_state.lower():
            guessed_state.append(user_state)
            esek = turtle.Turtle()
            esek.hideturtle()
            esek.pencolor("black")
            esek.penup()
            esek.goto(data_dict[data_states[i]][0], data_dict[data_states[i]][1])
            esek.write(data_states[i])
            break

#Tahmin ettiklerimizi listeden çıkartıyoz
for state in data_states:
    for guessed in guessed_state:
        if state==guessed:
            data_states.pop(state)
#Tahmin edemediklerimizi csv dosyasına yazdırıyoz
data_states.to_csv("States_To_Learn.csv")