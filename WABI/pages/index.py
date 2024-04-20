"""The home page of the app."""

from WABI import styles
from WABI.templates import template

import reflex as rx
import reflex_local_auth


@template(route="/", title="Home")
@reflex_local_auth.require_login
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)


