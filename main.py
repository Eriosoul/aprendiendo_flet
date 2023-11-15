import flet as ft

DELTA_WIDTH: int = 80
DELTA_HEIGHT: int = 160

card_style: dict = {
    "width": 160,
    "height": 180,
    "bgcolor": "FFFFFF",
    "border_radius": 5,
    "animate": ft.Animation(420, "easeInOutBack"),
    "data": False,
    "clip_behavior": ft.ClipBehavior.HARD_EDGE,
    "shadow": ft.BoxShadow(
        spread_radius=1,
        blur_radius=10,
        color=ft.colors.with_opacity(0.21, "black"),
        offset=ft.Offset(2, 2),
    ),
}

# btn class
class Button(ft.Container):
    def __init__(self):
        super().__init__(
            **card_style,
            on_click=self.open,
        )

        # logo
        self.logo = ft.Image(
            src="https://img.icons8.com/?size=64&id=Dovzd6PbVQqJ&format=png",
            width=72,
            height=72,
        )

        self.content = ft.Column(
            alignment="start",
            horizontal_alignment="center",
            controls=[
                ft.Divider(height=5, color="transparent"),
                ft.Row(controls=[self.logo], alignment="center"),
                ft.Text("Amazon", size=21, color="white", font_family="Open Sans"),
                ft.Divider(height=5, color="transparent"),
            ],
        )

    def open(self, event):
        self.width += DELTA_WIDTH if not event.control.data else -DELTA_WIDTH
        self.height += DELTA_HEIGHT if not event.control.data else -DELTA_HEIGHT
        self.data = not event.control.data
        self.update()

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    button: ft.Container = Button()

    page.add(button)
    page.update()

if __name__ == '__main__':
    ft.app(target=main)
