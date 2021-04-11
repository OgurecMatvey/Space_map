import folium
import os
from tkinter import *
font = ("Engravers MT", 12, "bold")


GREY = "#647387"
LIGHT_PINK = "#F2E4F9"




def open_map():
    t = theme.get()
    map = folium.Map(location=[57.1721950699114, 87.60990015555807], zoom_start=4, tiles=t)
    stations = [(51.09520725147888, 59.84274227664426,
                 "<p><strong>Космодром Ясный</strong><br><i>Первый пуск</i> отсюда был осуществлён 12 июля 2006 года. Ракета-носитель РС-20 «Воевода» вывела на околоземную орбиту американский спутник «Genesis I».<br> <i>Является действующим</i>.<br> Всего <i>было 10 запусков</i>.<br>Координаты для карты:51.09, 59.84</p><img src='yasniy.jpg' height='200px' width='300px'>",
                 'purple'),
                (51.85174519584252, 128.35495936075606,
                 "<p><strong>Космодром Восточный</strong><br><i>Первый запуск</i> с «Восточного» состоялся 28 апреля 2016 года. Ракета-носитель Союз-2.1а c блоком выведения «Волга» вывела на орбиту три космических аппарата: «Михайло Ломоносов», «Аист-2Д» и наноспутник «СамСат-218».<br> <i>Является действующим</i>.<br> Всего <i>было 5 запусков</i>.<br>Координаты для карты:51.85, 128.35</p><img src='https://cdn.iz.ru/sites/default/files/styles/900x506/public/news-2019-01/RIAN_3053599.HR_.ru_.jpg?itok=zvcj3zKB'  width='300px'>",
                 'purple'),
                (48.57501850677229, 45.76651688000907,
                 "<p><strong>Космодром Капустин яр</strong><br><i>Первый запуск</i> состоялся 16 марта 1962 года спутника «Космос-1».<br> <i>Сейчас действует</i>.<br> Всего <i>было 19 запусков</i>.<br>Координаты для карты:48.57, 45.76</p><img src='kapustin.jpg' width='300px'>",
                 'purple'),
                (45.96504099491279, 63.305927506397936,
                 "<p><strong>Космодром Байконур</strong><br><i>Первый запуск</i> был 15 мая 1957 года ракеты Р-7.<br> <i>На данный момент работает</i>.<br> Всего <i>было  более 1,5 тыс. запусков</i>.<br>Координаты для карты:45.96, 63.30</p><img src='baikon.jpg' width='300px'>",
                 'purple'),
                (62.92908752869038, 40.57586951771714,
                 "<p><strong>Космодром Плесецк</strong><br><i>Первый запуск</i> с Плесецка состоялся 17 марта 1966 г. - с пусковой установки номер 1 стартовала ракета-носитель Восток-2 с военным спутником Космос-112.<br> <i>Является действующим</i>.<br> Всего <i>было 1642  запусков</i>.<br>Координаты для карты:62.92, 40.57</p><img src='plesek.jpg' width='300px'>",
                 'purple')]
    m = mark.get()
    if m == 1:
        for station in stations:
            folium.Marker(location=(station[0], station[1]), popup=station[2],
                           icon=folium.Icon (color=station[3])).add_to (map)

    else:
        for station in stations:
            folium.CircleMarker(location=(station[0], station[1]), fill_color="red", radius=10,
                                 popup=station[2], icon=folium.Icon (color=station[3])).add_to (map)

    map.save ("map1.html")
    os.startfile("map1.html")


root = Tk()
root.title("Дизайн")
root.config(bg="black")
root.geometry("400x445")
root.resizable(FALSE, FALSE)


lbl = Label(text="Выбирайте карту", font=("Arial", 15, "bold"), bg=GREY, fg=LIGHT_PINK, width=35, height=4)
lbl.pack()
theme = StringVar()
mark = IntVar()
theme.set("Stamen Terrain")
mark.set(0)
Rb1 = Radiobutton(text="Космодромы на светлой карте", font=font, fg=LIGHT_PINK, bg=GREY, variable=theme, value="Stamen Terrain", padx=15, pady=10, width=35, selectcolor=GREY)
Rb1.pack()

Rb2 = Radiobutton(text="Космодромы на темной карте", font=font, fg=LIGHT_PINK, bg=GREY, variable=theme, value="CartoDB dark_matter", padx=15, pady=10, width=35, selectcolor=GREY)
Rb2.pack()

lbl2 = Label(text="Выбирайте маркер", font=("Arial", 15, "bold"), bg=GREY, fg=LIGHT_PINK, width=35, height=4)
lbl2.pack()

Rb3 = Radiobutton(text="Маркеры в виде кружочка", font=font, fg=LIGHT_PINK, bg=GREY, variable=mark, value=0, padx=15, pady=10, width=35, selectcolor=GREY)
Rb3.pack()

Rb3 = Radiobutton(text="Маркеры в виде капельки", font=font, fg=LIGHT_PINK, bg=GREY, variable=mark, value=1, padx=15, pady=10, width=35, selectcolor=GREY)
Rb3.pack()

b1 = Button(text="Запустить", font=font, fg=LIGHT_PINK, bg=GREY, command=open_map, padx=15, pady=10, width=35)
b1.pack()

selection = Label(padx=15, pady=10)
selection.pack()

root.mainloop()



