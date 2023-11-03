import flet as ft

def main(page: ft.Page):
    page.window_width = 720
    page.window_height = 1280
    # que no se redimensione
    page.window_resizable = False

    texto = ft.Text("Hello world", color=ft.colors.GREEN)
    page.add(texto)
    btn = ft.ElevatedButton("Click me!")
    page.add(btn)

ft.app(target=main)
