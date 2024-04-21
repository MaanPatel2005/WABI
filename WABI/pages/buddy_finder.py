from WABI import styles
from WABI.templates import template, ThemeState
from firebase_admin import firestore
import reflex as rx
from google.cloud.firestore_v1.base_query import FieldFilter
from WABI.components.welcome import Login
import WABI.components.welcome as auth
from firebase_admin import firestore




class CreatePostings(rx.State):
    val = ''
    def handle_posting(self, form_data: dict):
        title = form_data["title"]
        desc = form_data["desc"]
        print(form_data)
        db = firestore.client()
        doc_ref = db.collection('posts').document(title)
        doc_ref.set({'title': title, 'desc': desc, 'Interested': [Login.user]})
        return rx.redirect('/buddy')
    
class CheckboxState(rx.State):
    checked: bool = False
    def set_checked(self, thing: str, checked:bool):
        self.checked = not self.checked
        print(thing)
        print(f"This should be my name: {Login.user}")
        if checked:
            db = firestore.client()
            docs = (
                db.collection("posts").where(filter=FieldFilter('title', "==", thing)).stream()
            )
            value = next(docs)
            interested_users = value.get("Interested")
            interested_users.append(Login.user)
            print(interested_users)
            db.collection("posts").document(value.id).update({'Interested': interested_users})
        else:
            db = firestore.client()
            docs = (
                db.collection("posts").where(filter=FieldFilter('title', "==", thing)).stream()
            )
            value = next(docs)
            interested_users = value.get("Interested")
            index = interested_users.index(Login.user)
            interested_users = interested_users[0:index] + interested_users[index + 1:]
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
                        background="url('https://images.unsplash.com/photo-1437622368342-7a3d73a34c8f?q=80&w=1920&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') center/cover",
                        height="100px",
                    ),
                    rx.box(
                        rx.form(
                            rx.input(
                                placeholder="Title of your activity:",
                                name = 'title',
                                style={"height":30}
                            ),  
                            rx.input(
                                placeholder="Write Out An Activity Plan!",
                                name = 'desc',
                                style={"height": 50},
                            ),
                            
                            rx.flex(
                                rx.popover.close(
                                    rx.center(rx.button("Share Activity", type="submit",size="1"), 
                                             width='100%')
                                ),
                                spacing="3",
                                margin_top="12px",
                                justify="between",
                            ),
                            on_submit=CreatePostings.handle_posting,
                            reset_on_submit=True
                        ),
                        padding_top="12px",
                    ),
                    style={"width": 360},
                ),
            )
        ),
        width="100%",
    )


    