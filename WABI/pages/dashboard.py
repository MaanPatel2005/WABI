from WABI.templates import template, ThemeState
from WABI.components.dashboardComponents import challengeBox, challengeBodyBox, challengeSmallText, challengeTextBox, dashboardButton
import reflex as rx

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




_user_name = "Wabi"
_level = 10
_animal = "Jaguar"
_steps = 1000
_distance = 10
_calories = 800

def empty():
    pass



class StepsState(rx.State):
    steps : str = "0"
    
    def update_steps(self, val):
        rx.console_log(val)
        if str(val).isdigit():
            self.set_steps(val)
        else:
            self.steps = self.steps
class SliderVariationStateH(rx.State):
    value: int = 150

    def set_end(self, value: int):
        self.value = value

class SliderVariationStateV(rx.State):
    value: int = 60

    def set_end(self, value: int):
        self.value = value



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
            width = '90%',
            align = 'center',
            justify = 'center',
        ),
        rx.text('Weight', align = 'center', justify = 'center', font_size = "20px", weight = "bold"),
        width="100%", align = 'center', justify = 'center'
    )
def slider_vertical():
    return rx.vstack(
        rx.heading(SliderVariationStateV.value),
        rx.text("Min=0 inches, Max=120 inches"),
        rx.slider(
            default_value=60,
            min=0,
            max=120,
            on_change=SliderVariationStateV.set_end,
            orientation = "vertical",
            height = "14em",
        ),
        width="100%", align_items = 'flex-start',
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
    return rx.vstack(
        rx.center(
            rx.heading("Jungle Dashboard", size="8"),
            width="100%"
        ),
        rx.center(rx.avatar(src="/snake_head.png"), width='100%'),
        rx.center(rx.text(f"Explorer {_user_name}"), width='100%'),
        rx.center(rx.text(f"Lvl {_level} {_animal}"), width='100%'),
        rx.center(
            rx.hstack(
                rx.popover.root(
    rx.popover.trigger(
        dashboardButton('Daily Steps:', 'steps', 'pink', flex = '20%')
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
        dashboardButton('Distance Traveled:', 'miles', 'pink', flex = '20%')
    ),
    rx.popover.content(
        rx.box(
            rx.text("Distance Traveled", align = 'center'),
            spacing="2",
        ),
        style={"width": 200},
    ),
),
                rx.popover.root(
    rx.popover.trigger(
        dashboardButton('Calories Burned:', 'calories', 'pink', flex = '20%')
    ),
    rx.popover.content(
        rx.box(
            rx.text("Popover content"),
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

        
        challengeBox(head='head', body='body but now it is very long so it has to wrap around and stuff', 
                     reward = 'reward', img='/github.svg',click_func = empty, ThemeState = ThemeState),



 

        rx.center(
            rx.vstack(
                    rx.center(rx.heading("Buddy Profile", size="6"), width = '100%', height = 'fit-content'),
                    rx.spacer(),
                    slider_horizontal(),
                    rx.spacer(),
                    rx.spacer(),
                    rx.spacer(),
                    
                    rx.spacer(),
                    rx.center(rx.hstack(
                        rx.center(rx.box(slider_vertical(),width = '90%'), width = '100%', 
                              height = 'fit-content'), 
                        rx.text("Female"),rx.switch(default_checked=True),rx.text("Male"),
                            width = '100%', align = 'center', 
                            justify = 'center',
                            height = 'fit-content',), 
                            width = '100%',
                    ),
                     width = '40%', spacing = '5', background_color = '#9ADE7D', border_radius = '20px',
                    ),
            spacing = '5',
            width = '100%',
            padding_up = '30px',
        ),
        
    width = '100%', height = '100vh', spacing = '5',
    )
