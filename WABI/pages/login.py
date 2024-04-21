"""The home page of the app."""

from WABI import styles
from WABI.templates import template
import reflex as rx
# import reflex_local_auth
from rxconfig import config
import WABI.components.welcome as auth
import firebase_admin
from firebase_admin import firestore, credentials
cred = credentials.Certificate("WABI\\serviceAccountKey.json")



@template(route="/authenticate", title="Sign-In/Sign-Up")
def authenticate() -> rx.Component:
    return rx.chakra.tabs(
        rx.chakra.tab_list(
            rx.chakra.tab("Sign-In"),
            rx.chakra.tab("Sign-Up"),
        ),
        rx.chakra.tab_panels(
            rx.chakra.tab_panel(
                login()
                ),
            rx.chakra.tab_panel(
                signup()
            ),
        ),
        bg="black",
        color="white",
        shadow="lg",
    )


class LoginState(rx.State):
    username: str = ""
    password: str = ""

    def handle_login(self, form_data: dict):

        username = form_data["username"]
        password = form_data["password"]
        # Handle login logic here
        val = auth.Login(username, password).sign_in()
        print(val)
        if val:
            auth.Login.user = username
            print(auth.Login.user)
            return rx.redirect('/')
        else:
            return rx.redirect('/authenticate')

class SignUpState(rx.State):
    def handle_sign_up(self, form_data: dict):
        username = form_data["username"]
        password = form_data["password"]
        email = form_data["email"]
        name = form_data['name']
        height = form_data['height']
        weight = form_data['weight']
        auth.Login.user = username
        # Handle login logic here
        auth.sign_up(email, password, name, username, height, weight, 0, 0, 0, 0, "monkey") 
        return rx.redirect('/')


def login():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                placeholder="Username", 
                         name='username'),
                rx.input( 
                         placeholder="Password", 
                         type_="password",
                         name="password"),
                rx.button("Submit", type="submit"),
            ),
            on_submit=LoginState.handle_login, # Pass the function reference, not a call
            reset_on_submit=True,
        ),
    )

def signup():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Username",
                    name="username",
                ),
                rx.input(
                    placeholder="Email",
                    name="email",
                ),
                rx.input(
                    placeholder="Password",
                    type_="password",
                    name="password",
                ),
                rx.input(
                    placeholder="Name",
                    name="name",
                ),
                rx.input(
                    placeholder="Height",
                    name="height",
                ),
                rx.input(
                    placeholder="Weight",
                    name="weight",
                )),
                rx.button("Submit", type = "submit"),
                on_submit=SignUpState.handle_sign_up,
                reset_on_submit=True,
            ),
        )


