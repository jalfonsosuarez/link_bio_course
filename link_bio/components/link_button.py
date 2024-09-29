import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


def link_button(text_title: str, text_body: str, url: str, img: str = "arrow-right") -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=img,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=styles.Size.MEDIUM.value,
                    alt=text_title
                ),
                rx.vstack(
                    rx.text(
                        text_title,
                        style=styles.button_title_style
                    ),
                    rx.text(
                        text_body,
                        style=styles.button_body_style
                    ),
                    spacing=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                    align_items="start",
                    margin=Size.ZERO.value
                )
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )
