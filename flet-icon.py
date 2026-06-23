import flet as ft
import pyperclip

Spis_Icons = {}
Icon_page = 1
for i in ft.Icons:
    try:
        if len(Spis_Icons[Icon_page]) == 56: Icon_page += 1
        else: Spis_Icons[Icon_page].append(i)
    except:
        Spis_Icons[Icon_page]=[]
        Spis_Icons[Icon_page].append(i)

def App(page: ft.Page):
    page.window.resizable = False
    page.window.width = 500
    page.window.height = 650
    page.title = "Flet-Icons"

    def Add_Icons():
        Icons_Row.controls = []
        for icon in Spis_Icons[int(Page_Number.value)]:
            Icons_Row.controls.append(ft.FloatingActionButton(icon=icon, key=(icon), on_click=lambda e, name_to_copy=icon.name: pyperclip.copy(name_to_copy)))
        page.update()

    def Go_Left():
        if int(Page_Number.value) != int(list(Spis_Icons)[0]):
            Page_Number.value = int(Page_Number.value)-1
            Add_Icons()
        else:
            Page_Number.value = int(list(Spis_Icons)[-1])
            Add_Icons()

    def Go_Right():
        if int(Page_Number.value) != int(list(Spis_Icons)[-1]):
            Page_Number.value = int(Page_Number.value)+1
            Add_Icons()
        else:
            Page_Number.value = int(list(Spis_Icons)[0])
            Add_Icons()
            
    def Go_Left_ten():
        if int(Page_Number.value) - 10 >= int(list(Spis_Icons)[0]):
            Page_Number.value = int(Page_Number.value) - 10
            Add_Icons()
        else:
            steps_left = 10 - (int(Page_Number.value) - int(list(Spis_Icons)[0]))
            Page_Number.value = int(list(Spis_Icons)[-1]) - steps_left + 1
            Add_Icons()

    def Go_Right_ten():
        if int(Page_Number.value)+10 <= int(list(Spis_Icons)[-1]):
            Page_Number.value = int(Page_Number.value)+10
            Add_Icons()
        else:
            Page_Number.value = int(Page_Number.value)+10 - int(list(Spis_Icons)[-1])
            Add_Icons()
    
    def Go_Start():
        Page_Number.value = int(list(Spis_Icons)[0])
        Add_Icons()

    def Go_End():
        Page_Number.value = int(list(Spis_Icons)[-1])
        Add_Icons()
            
    Icons_Row = ft.Row(width=500,height=520, wrap=True)
    Page_Number = ft.Text(value=1, size=20)
    Page_Container = ft.Container(content=Page_Number, alignment=ft.Alignment.CENTER, width=100, height=50, bgcolor="Blue", border_radius=25)
    Button_Left = ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS, on_click=Go_Left)
    Button_Right = ft.IconButton(icon=ft.Icons.ARROW_FORWARD_IOS, on_click=Go_Right)
    Button_Left_ten = ft.IconButton(icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_LEFT, on_click=Go_Left_ten)
    Button_Right_ten = ft.IconButton(icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_RIGHT, on_click=Go_Right_ten)
    Button_Start = ft.IconButton(icon=ft.Icons.ARROW_LEFT, on_click=Go_Start)
    Button_End = ft.IconButton(icon=ft.Icons.ARROW_RIGHT, on_click=Go_End)

    page.add(ft.Column(controls=[Icons_Row,ft.Row(controls=[Button_Start, Button_Left_ten, Button_Left, Page_Container, Button_Right, Button_Right_ten, Button_End], alignment=ft.MainAxisAlignment.CENTER)]))
    Add_Icons()
    
ft.run(main=App)