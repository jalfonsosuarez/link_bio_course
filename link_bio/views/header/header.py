import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/avatar.png",
                name="José Alfonso",
                fallback="JA",
                size="8",
                radius="full",
            ),
            rx.vstack(
                rx.heading(
                    "José Alfonso Suárez.",
                ),
                rx.text(
                    "@joseasuarez",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value

                ),
                rx.hstack(
                    link_icon(
                        "https://www.google.es",
                        "mail",
                        "Google"
                    ),
                    link_icon(
                        "https://www.linkedin.com",
                        "linkedin",
                        "Linkedin"
                    ),
                    link_icon(
                        "https://www.x.com",
                        "x",
                        "Equis o Twitter"
                    ),
                    link_icon(
                        "https://www.youtube.com",
                        "youtube",
                        "Youtube"
                    ),
                    spacing=Size.MEDIUM.value
                ),
                width="100%"
            ),
            align="center",
            spacing=Size.BIG.value
        ),
        rx.flex(
            info_text("+30", "años de experiencia"),
            rx.spacer(),
            info_text("+30", "años de experiencia"),
            rx.spacer(),
            info_text("+30", "años de experiencia"),
            width="100%"
        ),
        rx.text("""Estoy aprendiendo Reflex de Python.
                        Además todo esto lo estoy haciendo desde un Dev Container de VS Code.
                        Mola mucho tener esto de los Dev Container, puedo tener contenedores separados con
                        las configuraciones para cada lenguaje que use.
                        """,
                color=TextColor.BODY.value
                ),
        spacing=Size.BIG.value,
        align_items="start",
    )
