import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight

MAX_WIDTH = "600px"


class Size(Enum):
    ZERO = "0em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "size": "lg",
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.MEDIUM.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECONDARY.value,
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

button_title_style = {
    "font_family": Font.TITLE.value,
    "font_weight": FontWeight.MEDIUM.value,
    "color": TextColor.HEADER.value,
    "font_size": Size.DEFAULT.value
}

button_body_style = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "color": TextColor.BODY.value,
    "font_size": Size.MEDIUM.value
}

title_style = {
    "width": "100%",
    "font_family": Font.TITLE.value,
    "font_weight": FontWeight.MEDIUM.value,
    "color": TextColor.HEADER.value,
    "padding_top": Size.DEFAULT.value
}

navbar_title_style = {
    "font_family": Font.LOGO.value,
    "font_weight": FontWeight.MEDIUM.value,
    "font_size": Size.LARGE.value,
}
