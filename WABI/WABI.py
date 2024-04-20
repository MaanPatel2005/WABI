"""Welcome to Reflex!."""

# Import all the pages.
from WABI.pages import *

import reflex as rx
import reflex_local_auth

class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App()


app.add_page(
    reflex_local_auth.pages.login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(
    reflex_local_auth.pages.register_page,
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="Register",
)