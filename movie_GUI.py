import numpy as np
import pandas as pd
import csv
import flet as ft

movies = pd.read_csv('movie_data.csv')
global main_genre
global sub_genre
global choose1
global choose2
global decision

main_genre = np.zeros((245, 12))
sub_genre = np.zeros((245, 12))
choose1 = np.zeros((12, 1))
choose2 = np.zeros((12, 1))
decision = np.zeros((245, 1))

#建立main_genre的矩陣(eigenmatrix)
for i in range (245):
    if  movies.iat[i,5] =='Mystery':
        main_genre[i][0]=2
    else:
        main_genre[i][0]=0

    if  movies.iat[i,5] =='Drama':
        main_genre[i][1]=2
    else:
        main_genre[i][1]=0

    if  movies.iat[i,5] =='Sci-Fi':
        main_genre[i][2]=2
    else:
        main_genre[i][2]=0

    if  movies.iat[i,5] =='Animation':
        main_genre[i][3]=2
    else:
        main_genre[i][3]=0

    if  movies.iat[i,5] =='Biography':
        main_genre[i][4]=2
    else:
        main_genre[i][4]=0

    if  movies.iat[i,5] =='Crime':
        main_genre[i][5]=2
    else:
        main_genre[i][5]=0

    if  movies.iat[i,5] =='Romance':
        main_genre[i][6]=2
    else:
        main_genre[i][6]=0

    if  movies.iat[i,5] =='Action':
        main_genre[i][7]=2
    else:
        main_genre[i][7]=0

    if  movies.iat[i,5] =='Fantastic':
        main_genre[i][8]=2
    else:
        main_genre[i][8]=0

    if  movies.iat[i,5] =='Comedy':
        main_genre[i][9]=2
    else:
        main_genre[i][9]=0

    if  movies.iat[i,5] =='Adventure':
        main_genre[i][10]=2
    else:
        main_genre[i][10]=0

    if  movies.iat[i,5] =='Thriller':
        main_genre[i][11]=2
    else:
        main_genre[i][11]=0


#建立sub_genre的矩陣(eigenmatrix)
for i in range (245):
    if  movies.iat[i,6] =='Mystery':
        sub_genre[i][0]=1
    else:
        sub_genre[i][0]=0

    if  movies.iat[i,6] =='Drama':
        sub_genre[i][1]=1
    else:
        sub_genre[i][1]=0

    if  movies.iat[i,6] =='Sci-Fi':
        sub_genre[i][2]=1
    else:
        sub_genre[i][2]=0

    if  movies.iat[i,6] =='Animation':
        sub_genre[i][3]=1
    else:
        sub_genre[i][3]=0

    if  movies.iat[i,6] =='Biography':
        sub_genre[i][4]=1
    else:
        sub_genre[i][4]=0

    if  movies.iat[i,6] =='Crime':
        sub_genre[i][5]=1
    else:
        sub_genre[i][5]=0

    if  movies.iat[i,6] =='Romance':
        sub_genre[i][6]=1
    else:
        sub_genre[i][6]=0

    if  movies.iat[i,6] =='Action':
        sub_genre[i][7]=1
    else:
        sub_genre[i][7]=0

    if  movies.iat[i,6] =='Fantastic':
        sub_genre[i][8]=1
    else:
        sub_genre[i][8]=0

    if  movies.iat[i,6] =='Comedy':
        sub_genre[i][9]=1
    else:
        sub_genre[i][9]=0

    if  movies.iat[i,6] =='Adventure':
        sub_genre[i][10]=1
    else:
        sub_genre[i][10]=0

    if  movies.iat[i,6] =='Thriller':
        sub_genre[i][11]=1
    else:
        sub_genre[i][11]=0

#取得各項的資料
titl = movies['TITLE']
GENRE_name = movies['GENRE_name']
DIRECTOR = movies['DIRECTOR']
yea = movies['YEAR']

#輸入主類型
def main_input(a):
    if a == 'Mystery':
        choose1[0][0]=2
    else:
        choose1[0][0]=0
    if a == 'Drama':
        choose1[1][0]=2
    else:
        choose1[1][0]=0
    if a == 'Sci-Fi':
        choose1[2][0]=2
    else:
        choose1[2][0]=0
    if a == 'Animation':
        choose1[3][0]=2
    else:
        choose1[3][0]=0
    if a == 'Biography':
        choose1[4][0]=2
    else:
        choose1[4][0]=0
    if a == 'Crime':
        choose1[5][0]=2
    else:
        choose1[5][0]=0
    if a == 'Romance':
        choose1[6][0]=2
    else:
        choose1[6][0]=0
    if a == 'Action':
        choose1[7][0]=2
    else:
        choose1[7][0]=0
    if a == 'Fantastic':
        choose1[8][0]=2
    else:
        choose1[8][0]=0
    if a == 'Comedy':
        choose1[9][0]=2
    else:
        choose1[9][0]=0
    if a == 'Adventure':
        choose1[10][0]=2
    else:
        choose1[10][0]=0
    if a == 'Thriller':
        choose1[11][0]=2
    else:
        choose1[11][0]=0

#輸入次要類型
def sub_input(b):
    if b == 'Mystery':
        choose2[0][0]=1
    else:
        choose2[0][0]=0
    if b == 'Drama':
        choose2[1][0]=1
    else:
        choose2[1][0]=0
    if b == 'Sci-Fi':
        choose2[2][0]=1
    else:
        choose2[2][0]=0
    if b == 'Animation':
        choose2[3][0]=1
    else:
        choose2[3][0]=0
    if b == 'Biography':
        choose2[4][0]=1
    else:
        choose2[4][0]=0
    if b == 'Crime':
        choose2[5][0]=1
    else:
        choose2[5][0]=0
    if b == 'Romance':
        choose2[6][0]=1
    else:
        choose2[6][0]=0
    if b == 'Action':
        choose2[7][0]=1
    else:
        choose2[7][0]=0
    if b == 'Fantastic':
        choose2[8][0]=1
    else:
        choose2[8][0]=0
    if b == 'Comedy':
        choose2[9][0]=1
    else:
        choose2[9][0]=0
    if b == 'Adventure':
        choose2[10][0]=1
    else:
        choose2[10][0]=0
    if b == 'Thriller':
        choose2[11][0]=1
    else:
        choose2[11][0]=0


#GUI
def main(page: ft.Page):
    global maximum
    page.scroll = "auto"
    page.update()
    page.bgcolor='#000000'
    st = ft.Stack(
        [
            ft.Image(
                src=f"the-prestige-feature.jpg",
                expand=1,
                width=500,
                height=200,
                fit=ft.ImageFit.CONTAIN
            ),
            ft.Row(
                [
                    ft.Text(
                        "Recommandation",
                        color="white",
                        size=40,
                        weight="bold",
                        opacity=0.7,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        width=500,
        height=200,
    )
    page.add(st)

    # GUI的排版
    page.title = "Movie Recommandation"
    page.window_width = 500
    page.window_height = 770
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 按鈕的function
    def  Main_genre_click(aaa):
        a = aaa.control.data
        main_input(a)
        t1.value="1st catagory: " + f'{a}'
        page.update()

    def Sub_genre_click(aaa):
        b = aaa.control.data
        sub_input(b)
        t2.value="2nd catagory: " + f'{b}'
        page.update()
        
    def result_click(aaa):
        choose=choose1*2+choose2
        decide1 = np.dot(main_genre, choose)
        decide2 = np.dot(sub_genre, choose)
        decision = decide1 + decide2
        maximum = decision.max()
        
        print("max= ", maximum)
        if maximum <=1 :
             page.add(ft.Text(f'Sorry, no releated movie.',size=18,color='WHITE'))
        else:
            page.add(ft.Text(f'Movies you might be interested in:',size=18,color='GREEN'))
            for i in range (245):
                if decision[i]==maximum:
                    movie_sug = titl[i]
                    release = yea [i]
                    director = DIRECTOR[i]
                    page.add(ft.Text(f'{movie_sug} ({release}, {director})',size=16,color='WHITE'))
            page.add(ft.Text(f'Movies you might be likely interested in:',size=18,color='GREEN'))
            for i in range (245):
                if decision[i]==maximum-1:
                    movie_sug = titl[i]
                    release = yea [i]
                    director = DIRECTOR[i]
                    page.add(ft.Text(f'{movie_sug} ({release},{director})',size=18,color='WHITE'))
                
            
    # ------建立物件------
    main = ft.Text("What kind of movie do you want to watch most?", size=18,color='WHITE')
    sub = ft.Text("What kind of movie do you want to watch second?", size=18,color='WHITE')
    t1 = ft. Text("1st catagory:     ", size=18, expand=1,color='GREEN')
    t2 = ft. Text("2nd catagory:     ", size=18, expand=1,color='WHITE')
    t3 = ft. Text("Movies you might be interested in:", size=18, expand=1,color='WHITE')

    #建立按鈕
    page.add(main,      
        ft.Row(
            controls=[
                ft.FilledButton(text=f"{GENRE_name[0]}", data=f"{GENRE_name[0]}", width=150, on_click=Main_genre_click,expand=1),
                ft.FilledButton(text=f"{GENRE_name[1]}", data=f"{GENRE_name[1]}", width=150, on_click=Main_genre_click,expand=1),
                ft.FilledButton(text=f"{GENRE_name[2]}", data=f"{GENRE_name[2]}", width=150, on_click=Main_genre_click,expand=1),
                ft.FilledButton(text=f"{GENRE_name[3]}", data=f"{GENRE_name[3]}", width=150, on_click=Main_genre_click,expand=1)
            ]
        ),
        ft.Row(
            controls=[
                ft.FilledButton(text=f"{GENRE_name[4]}", data=f"{GENRE_name[4]}", width=150, on_click=Main_genre_click,expand=1),
                ft.FilledButton(text=f"{GENRE_name[5]}", data=f"{GENRE_name[5]}", width=150, on_click=Main_genre_click,expand=1),
                ft.FilledButton(text=f"{GENRE_name[6]}", data=f"{GENRE_name[6]}", width=150, on_click=Main_genre_click,expand=1),
                ft.FilledButton(text=f"{GENRE_name[7]}", data=f"{GENRE_name[7]}", width=150, on_click=Main_genre_click,expand=1)
            ]
        ),
        ft.Row(
            controls=[
                ft.FilledButton(text=f"{GENRE_name[8]}", data=f"{GENRE_name[8]}", width=150, on_click=Main_genre_click,expand=1),
                ft.FilledButton(text=f"{GENRE_name[9]}", data=f"{GENRE_name[9]}", width=150, on_click=Main_genre_click,expand=1),
                ft.FilledButton(text=f"{GENRE_name[10]}", data=f"{GENRE_name[10]}", width=150, on_click=Main_genre_click,expand=1),
                ft.FilledButton(text=f"{GENRE_name[11]}", data=f"{GENRE_name[11]}", width=150, on_click=Main_genre_click,expand=1),
            ]
        ),
        
        sub,           
                ft.Row(
            controls=[
                ft.ElevatedButton(text=f"{GENRE_name[0]}", data=f"{GENRE_name[0]}", width=150, on_click=Sub_genre_click,expand=1),
                ft.ElevatedButton(text=f"{GENRE_name[1]}", data=f"{GENRE_name[1]}", width=150, on_click=Sub_genre_click,expand=1),
                ft.ElevatedButton(text=f"{GENRE_name[2]}", data=f"{GENRE_name[2]}", width=150, on_click=Sub_genre_click,expand=1),
                ft.ElevatedButton(text=f"{GENRE_name[3]}", data=f"{GENRE_name[3]}", width=150, on_click=Sub_genre_click,expand=1)
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text=f"{GENRE_name[4]}", data=f"{GENRE_name[4]}", width=150, on_click=Sub_genre_click,expand=1),
                ft.ElevatedButton(text=f"{GENRE_name[5]}", data=f"{GENRE_name[5]}", width=150, on_click=Sub_genre_click,expand=1),
                ft.ElevatedButton(text=f"{GENRE_name[6]}", data=f"{GENRE_name[6]}", width=150, on_click=Sub_genre_click,expand=1),
                ft.ElevatedButton(text=f"{GENRE_name[7]}", data=f"{GENRE_name[7]}", width=150, on_click=Sub_genre_click,expand=1)
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text=f"{GENRE_name[8]}", data=f"{GENRE_name[8]}", width=150, on_click=Sub_genre_click,expand=1),
                ft.ElevatedButton(text=f"{GENRE_name[9]}", data=f"{GENRE_name[9]}", width=150, on_click=Sub_genre_click,expand=1),
                ft.ElevatedButton(text=f"{GENRE_name[10]}", data=f"{GENRE_name[10]}", width=150, on_click=Sub_genre_click,expand=1),
                ft.ElevatedButton(text=f"{GENRE_name[11]}", data=f"{GENRE_name[11]}", width=150, on_click=Sub_genre_click,expand=1),
            ]
        ),
        
        ft.Row(          #結果
            controls=[
                 ft.FilledButton(
                    "Go!", on_click=result_click,expand=1,
                    style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
        ),
            ]
        ),
        ft.Row(          #結果
            controls=[t1]
        ),
        ft.Row(          #結果
            controls=[t2]
        ),
        ft.Row(     
            controls=[t3]
        ),
    )
ft.app(target=main)

