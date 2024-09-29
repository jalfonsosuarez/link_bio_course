import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/avatar.png",
            width=Size.VERY_BIG.value,
            height="auto",
            alt="Logotipo"
        ),
        rx.link(
            "Esto es un link",
            href="https://google.es",
            is_external=True,
            margin_bottom=Size.ZERO.value,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            f"Esto debe ser el footer del la página.",
            margin_top=Size.ZERO.value,
            margin_bottom=Size.ZERO.value,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            f"© {datetime.date.today().year} by JASM",
            margin_top=Size.ZERO.value,
            margin_bottom=Size.ZERO.value,
            font_size=Size.MEDIUM.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        width="100%",
        align="center",
        color=TextColor.FOOTER.value
    )
