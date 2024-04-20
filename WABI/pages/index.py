"""The home page of the app."""

from WABI import styles
from WABI.templates import template

import reflex as rx
# import reflex_local_auth
from rxconfig import config


class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: rx.Var[
        str
    ] = "https://prod.spline.design/WUURsddQ3Sp5-bwC/scene.splinecode"
    is_default = True

    lib_dependencies: list[str] = ["@splinetool/runtime"]


spline = Spline.create


def spline_example():
    return rx.center(
        spline(),
        overflow="hidden",
        width="100%",
        height="50em",
    )



@template(route="/", title="Home")
def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            spline_example(),
            align="center",
            height = "100hx",
            width = "100%"
        ),
        width = "100%"
    )




