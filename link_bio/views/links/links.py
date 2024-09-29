import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size


def links() -> rx.Component:
    return rx.vstack(
        title("Grupo 1"),
        link_button(
            "Primer botón",
            "Subtitulo 1",
            "https://google.es"
        ),
        link_button(
            "Segundo botón",
            "Este es el Subtitulo 2 del segundo botón del grupo 1",
            "https://google.es"
        ),
        link_button(
            "Tercer botón",
            "Subtitulo 3",
            "https://google.es"
        ),
        link_button(
            "Cuarto botón",
            "Subtitulo 4",
            "https://google.es"
        ),
        title("Grupo 2"),
        link_button(
            "Primer botón",
            "Subtitulo 1",
            "https://google.es"
        ),
        link_button(
            "Segundo botón",
            "Subtitulo 2",
            "https://google.es"
        ),
        link_button(
            "Tercer botón",
            "Subtitulo 3",
            "https://google.es"
        ),
        link_button(
            "Cuarto botón",
            "Subtitulo 4",
            "https://google.es"
        ),
        title("Contacto"),
        link_button(
            "MyPublicInbox",
            "Recibe respuesta rápidamente",
            "https://google.es"
        ),
        link_button(
            "Email",
            "Escríbeme algo bonito.",
            "https://google.es"
        ),
        width="100%",
        spacing=Size.MEDIUM.value
    )
