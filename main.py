import flet as ft
from templates.assets.colors.color_at import ColorAT

def main(page: ft.Page):
    page.window_width = 720
    page.window_height = 1280
    # que no se redimensione
    page.window_resizable = False
    color = ColorAT()

    texto = ft.Text("Hello world", color=ft.colors.GREEN)
    page.add(texto)
    btn = ft.ElevatedButton("Click me!", color=color.TC)
    page.add(btn)

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")

    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

ft.app(target=main)
