import reflex as rx
from WABI.templates import template

def self_message(username : str, message : str, name: str)->'reflex_component':
    return rx.box( rx.flex(
        rx.flex(
            rx.hstack(
                rx.box(rx.vstack(rx.box( rx.flex(rx.text(username, height = '100%'), width = '100%', align = 'end', justify= 'end'), height = '20px', width = '100%'),rx.box(rx.text(message, color = 'white'),width = '100%', background_color = 'blue', border_radius = '20px', padding = '15px')),width = '80%'), 
                rx.box(
                    rx.flex(rx.box(#avatar/initial box
                    rx.avatar(fallback=get_initials(name), color="#F6F4DA"),
                    align = 'start',
                    justify = 'start',
                ),width = '100%', align = 'baseline'),
                width = '20%'),width = '100%', align = 'end', justify = 'end')
            ,width = '40%', align = 'end', justify = 'end',
        ),width = '100%', align = 'end', justify = 'end'
    ),width = '100%')


"""rx.box(
                        rx.vstack(
                            rx.flex(
                                height = '20px', 
                                width = '40%'
                                    ), 
                            rx.box(
                                rx.text(message, color = 'white', max_width = '100%',),
                                width = '40%',
                            
                                ),
                            
                                )
                            ,width = '80%'
                        ), 
                        rx.flex(
                            width = '20%'
                            )"""

def other_message(username : str, message : str, name: str)->'reflex_component':
    return rx.box( 
             rx.flex(
                rx.flex(
                    rx.hstack(
                        rx.box(
                            rx.flex(rx.box(#avatar/initial box
                                rx.flex(rx.avatar(fallback=get_initials(name), color="#F6F4DA"), align = 'baseline', width = '100%'),
                    #align = 'start',
                ),width = '100%', align = 'baseline'),
                width = '20%' , height = 'fit-content'),
                rx.box(rx.vstack(rx.box( rx.flex(rx.text(username, height = '100%'), width = '100%', align = 'start', justify = 'start',), 
                                        height = '20px', width = '100%'),
                                 rx.box(rx.text(message, color = 'black'),
                                        width = '100%', background_color = '#F7EBDE', border_radius = '20px', padding = '15px')),
                                        width = '80%'), 
                width = '100%', align = 'start', justify = 'start',)
            ,width = '40%', align = 'start', justify = 'start',
        ),width = '100%', align = 'start', justify = 'start',
    ),width = '100%', align = 'start', justify = 'start')





    # return rx.box(#this box spans the entire width of the chat box for vertical layering purposes

    #     rx.vstack(#contains all of the message's components and limits its size
    #         rx.box(rx.box(rx.text(username, justify = 'start'),#holds the username and its related components 
    #                       width = '80%', height = '100%', align = 'start', justify = 'start'),
    #                height = '20px', width = '100%'),
            
    #         rx.hstack(#Horizontally separates the text bubble and the pfp section
    #             rx.box(#box that encloses the text bubble
    #                 rx.text(message, color = 'black', align = 'start', justify = 'start'),
    #                 width = '80%',
    #                 height = 'min-content',
    #                 align = 'end',
    #                 justify = 'end',
    #                 border_radius = '10px',#Curves the border of the bubble
    #                 background_color = '#f6f4da',#Shade of white/tan for the box
    #                 padding = '10px',
    #             ),
    #             rx.box(#avatar/initial box
    #                 rx.avatar(fallback=get_initials(name), color="#F6F4DA"),
    #                 align = 'start',
    #                 justify = 'start',
    #             ),
    #         ),

    #         width = '40%',
    #         justify = 'start',
    #         align = 'start',
    #     ),

    #     width = '100%',
    #     height = 'min-content'#value that represents the minimum height required to hold all contained elements

    # )

    # Styles for the action bar.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
input_style = dict(
    border_width="1px", box_shadow=shadow
)
button_style = dict(
    background_color=rx.color("accent", 10),
    box_shadow=shadow,
)
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Type your Message Here",
            style=input_style,
        ),
        rx.button("Send", style=button_style),
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            #chat(),
            action_bar(),
            align="center",
        )
    )


class State3(rx.State):
    # The current question being asked.
    question: str

def get_initials(name: str):
    my_str = name.split()
    return my_str[0][0] + my_str[1][0]  

@template(route="/chat", title="Chat")
def chat():
    return rx.box(
        rx.box(
         rx.scroll_area(
         rx.flex(
            self_message("energydrinklover", "i really love puravhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", "andrew xiong"),
            other_message("energydrinklover", "i really love puravhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", "andrew xiong"),
            self_message("test2user", "i really love skibidi toilet ohio fanum tax with kai cenat", "andrew `xiong`"),
            other_message("energydrinklover", "i really love puravhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", "andrew xiong"),
            self_message("test2user", "i really love skibidi toilet ohio fanum tax with kai cenat", "andrew `xiong`"),
            self_message("energydrinklover", "i really love puravhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", "andrew xiong"),
            other_message("energydrinklover", "i really love puravhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", "andrew xiong"),
            self_message("test2user", "i really love skibidi toilet ohio fanum tax with kai cenat", "andrew `xiong`"),
            
            width = "100%",
        direction = 'column',
    ),
    type="always",
    scrollbars="vertical",
    style={"height": '80%'},
    ),height = '650px', padding_up = '50px'),index(), width = '100%')