import reflex as rx
import link_bio.styles.styles as styles


def link_icon(url: str, tag_icon: str = "external-link", alt: str = "Icono decorativo") -> rx.Component:
    return rx.link(
        rx.icon(
            tag=tag_icon,
            alt=alt
        ),
        href=url,
        is_external=True
    )
