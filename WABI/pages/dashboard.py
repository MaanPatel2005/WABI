from WABI.templates import template, ThemeState
from WABI.components.dashboardComponents import challengeBox, challengeBodyBox, challengeSmallText, challengeTextBox, dashboardButton, dashboardChallenges 
import reflex as rx
from firebase_admin import firestore
from ..components.welcome import Login
from google.cloud.firestore_v1.base_query import FieldFilter
from firebase_admin import firestore
db = firestore.client()

style1 = {
    "color": "green",
    "font_family": "Helvetica",
}
style2 = {
    "color": "black",
    "padding": "10px",
}
equal_style = {
    "flex": "20%",  # Use flexbox to distribute the boxes evenly
    "padding": "10px",
    "box_sizing": "border-box",  # Ensure padding is included in the box size
}

_user_name = Login.user
_points = 0
_animal = "Jaguar"
_steps = 1000
_distance = 10
_calories = 800

def empty():
    pass



class StepsState(rx.State):
    steps : str = "0"
    
    def update_steps(self, val):
        if str(val).isdigit():
            self.steps=val
            db = firestore.client()
            db.collection('users').document(Login.user).update({'steps': val})



class SliderVariationStateH(rx.State):
    value: int = 150

    def set_end(self, value: int):
        self.value = value
    
    def set_value(self, value: int):
        db = firestore.client()
        db.collection('users').document(Login.user).update({'weight': value})

        

class SliderVariationStateV(rx.State):
    value: int = 60

    def set_end(self, value: int):
        self.value = value
    
    def set_value(self, value: int):
        db = firestore.client()
        db.collection('users').document(Login.user).update({'height': value})

    



def slider_horizontal():
    return rx.vstack(
        rx.heading(SliderVariationStateH.value),
        rx.flex(rx.text("Min=0 lbs"),
        rx.text("Max=300 lbs"), justify = 'between', width = '100%'),
        rx.slider(
            default_value=150,
            min=0,
            max=300,
            on_change=SliderVariationStateH.set_end,
            on_value_commit=SliderVariationStateH.set_value,
            width = '90%',
            align = 'center',
            justify = 'center',
        ),
        rx.text('Weight', align = 'center', justify = 'center', font_size = "20px", weight = "bold"),
        width="100%", align = 'center', justify = 'center'
    )
def slider_vertical():
    return rx.hstack(
        
        
        rx.vstack(
            rx.text('Height', align = 'center', justify = 'center', font_size = "20px", weight = "bold")
            ,rx.text("Max= 120 inches"), 
                  rx.slider(
            default_value=60,
            min=0,
            max=120,
            on_change=SliderVariationStateV.set_end,
            on_value_commit=SliderVariationStateV.set_value,
            orientation = "vertical",
            height = "14em",
            width = "10%",
            align = 'center',
            justify = 'center',
            ),
                  rx.text("Min= 0 inches"),
                  align_items = 'center'),
        rx.heading(SliderVariationStateV.value),
        width="100%", align_items = 'center',
    )

@template(route="/", title="Dashboard")
# @reflex_local_auth.require_login
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """

    template_color = ThemeState.accent_color
    #template_color = f'{template_color}'
    return (rx.vstack(
        rx.center(
            rx.heading("Jungle Dashboard", size="8"),
            width="100%"
        ),
        rx.center(rx.avatar(src="/snake_head.png"), width='100%'),
        rx.center(rx.text(f"Explorer {_user_name}"), width='100%', font_size = "20px"),
        rx.center(rx.text(f"{_points} Banana Points"), width='100%', font_size = "20px"),
        rx.center(
            rx.hstack(
                rx.popover.root(
    rx.popover.trigger(
        dashboardButton('Daily Steps:', 'steps', 'pink', db.collection("users").document('maanvp').get().to_dict()['steps'], flex = '20%')
    ),
    rx.popover.content(
        rx.box(
            rx.text("Daily Steps", align = 'center' ),
            rx.text_area(max_length = 6, value = StepsState.steps, on_change = StepsState.update_steps),
            spacing="2"
        ),
        style={"width": 200},
    ),
),
                rx.popover.root(
    rx.popover.trigger(
        dashboardButton('Distance Traveled:', 'miles', 'pink', db.collection("users").document('maanvp').get().to_dict()['distance'], flex = '20%')
    ),
    rx.popover.content(
        rx.box(
            rx.text("Calculated by dividing the number of steps taken by 20." , align = 'center'),
            spacing="2",
        ),
        style={"width": 200},
    ),
),
                rx.popover.root(
    rx.popover.trigger(
        dashboardButton('Calories Burned:', 'calories', 'pink', db.collection("users").document('maanvp').get().to_dict()['calories'], flex = '20%')
    ),
    rx.popover.content(
        rx.box(
            rx.text("Calculated by multiplying the number of steps taken and height in inches then dividing by 153414.0436."),
            spacing="2",
        ),
        style={"width": 200},
    ),
),
         
               
                
                spacing="9",  # Adjust the spacing as needed
                width="100%"
            ),
            
            width = "100%",  # Make the component stretch across the whole page
        ),

        rx.center(
            rx.box(
                rx.heading("Daily Jungle Challenges", size="6"),
                padding="25px",
            ),
            width="100%"
        ),

        
        dashboardChallenges([['Skibbidy','Fanum Tax', '25 Bananas', 'paneleft.svg', empty, ThemeState],
                             ['Skibbidy','Fanum Axe', '25 Bananas', 'paneleft.svg', empty, ThemeState],
                             ['Skibbidy','Fanum Axe', '25 Bananas', 'paneleft.svg', empty, ThemeState]]),



        rx.spacer(),
        rx.spacer(),

        rx.center(
            rx.vstack(
                    rx.center(rx.heading("Buddy Profile", size="6"), width = '100%', height = 'fit-content'),
                    rx.spacer(),
                    slider_horizontal(),
                    rx.spacer(),
                    rx.spacer(),
                    rx.center(rx.hstack(
                        rx.center(rx.box(slider_vertical(),width = '90%'), rx.image(src = 'quandale.png', width = '55%'),width = '100%', 
                              height = 'fit-content'), 
                            width = '100%', align = 'center', 
                            justify = 'center',
                            height = 'fit-content',), 
                            width = '100%',
                    ),
                     width = '40%', spacing = '5', background_color = '#9ADE7D', border_radius = '20px', padding = "20px"
                    ),
            spacing = '5',
            width = '100%',
            padding_up = '30px',
        ),
        
    width = '100%', height = '100vh', spacing = '5',
    ))
