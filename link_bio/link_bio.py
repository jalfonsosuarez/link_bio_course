import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

# class State(rx.State):
#     pass

def index() -> rx.Component:
    return rx.box(
            navbar(),
            rx.center(
                rx.vstack(
                    header(),
                    links(),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin_y=Size.BIG.value,
                    padding=Size.BIG.value,
                    align="center"
                )
            ),
            rx.center(
                footer()
            )
        )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap",
        "https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
    ],
    style=styles.BASE_STYLE
)
app.add_page(index)
# app._compile()
