from WABI import styles
from WABI.templates import template, ThemeState
from firebase_admin import firestore
import reflex as rx
from google.cloud.firestore_v1.base_query import FieldFilter
from WABI.components.welcome import Login

class CheckboxState(rx.State):
    checked: bool = False
    def set_checked(self, thing: str, checked:bool):
        self.checked = not self.checked
        print(thing)
        print(f"This should be my name: {Login.user}")
        db = firestore.client()
        docs = (
            db.collection("posts").where(filter=FieldFilter('title', "==", thing)).stream()
        )
        value = next(docs)
        interested_users = value.get("Interested")
        interested_users.append(Login.user)
        print(interested_users)
        db.collection("posts").document(value.id).update({'Interested': interested_users})

@template(route="/buddy", title="Buddy Finder")
def buddy_finder() -> rx.Component:
    db = firestore.client() 
    query = db.collection('posts')
    docs = query.stream()
    accordion_items = [
        (doc.to_dict()['title'], rx.chakra.center(doc.to_dict()['desc'], rx.checkbox("Interested?", default_checked = False, on_change = lambda checked: CheckboxState.set_checked(doc.to_dict()['title'], checked))))  for doc in docs
    ]   
    return rx.center(
        rx.vstack(
            rx.center(
                rx.heading("Buddy Finder", size="8"),
                width="100%"    
            ),
            rx.center(
                rx.heading("Upcoming Group Activities", size="6"),
                width="100%"
            ),
            rx.spacer(),
            rx.spacer(),
            rx.center(
            rx.chakra.accordion(
                items=accordion_items,
                width="600px",
            )),
            rx.spacer(),
            rx.spacer(),
            rx.center(
                rx.heading("Links", size="5"),
                width="100%"
            ),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.center(rx.link(rx.button("Chat With Your Groups"),href="/chat"), width='100%'),
            rx.spacer(),
            rx.popover.root(
                rx.popover.trigger(
                    rx.center(rx.button("Create A Posting", variant="classic", style={"paddingRight": "50px"}), width='100%'),
                ),
                rx.popover.content(
                    rx.inset(
                        side="top",
                        background="url('https://images.unsplash.com/photo-1570288685280-7802a8f8c4fa?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') center/cover",
                        height="100px",
                    ),
                    rx.box(
                        rx.text_area(
                            placeholder="Write Out An Activity Plan!",
                            style={"height": 80},
                        ),
                        rx.flex(
                            rx.popover.close(
                                rx.center(rx.button("Share Activity", size="1"), width='100%')
                            ),
                            spacing="3",
                            margin_top="12px",
                            justify="between",
                        ),
                        padding_top="12px",
                    ),
                    style={"width": 360},
                ),
            )
        ),
        width="100%",
    )