import reflex as rx

def self_message(username : str, message : str, name: str)->'reflex_component':
    
    
    return rx.box(#this box spans the entire width of the chat box for vertical layering purposes

        rx.vstack(#contains all of the message's components and limits its size
            rx.box(rx.box(rx.text(username, justify = 'right'),#holds the username and its related components 
                          width = '80%', height = '100%', align = 'left', justify = 'left'),
                   height = '20px', width = '100%'),
            
            rx.hstack(#Horizontally separates the text bubble and the pfp section
                rx.box(#box that encloses the text bubble
                    rx.text(message, color = 'white'),
                    width = '80%',
                    height = 'min-content',
                    align = 'left',
                    justify = 'left',
                    border_radius = '10px',#Curves the border of the bubble
                    background_color = '#5E24FF',#Shade of purple/blue for the box
                ),
                rx.box(#avatar/initial box
                    rx.avatar(fallback=get_initials(name), color_scheme="orange"),
                    align = 'right',
                    justify = 'right',
                ),
            ),

            width = '40%',
            justify = 'right',
            align = 'right',
        ),

        width = '100%',
        height = 'min-content'#value that represents the minimum height required to hold all contained elements

    )

def other_message(username : str, message : str, name: str)->'reflex_component':
    return rx.box(#this box spans the entire width of the chat box for vertical layering purposes

        rx.vstack(#contains all of the message's components and limits its size
            rx.box(rx.box(rx.text(username, justify = 'left'),#holds the username and its related components 
                          width = '80%', height = '100%', align = 'left', justify = 'left'),
                   height = '20px', width = '100%'),
            
            rx.hstack(#Horizontally separates the text bubble and the pfp section
                rx.box(#box that encloses the text bubble
                    rx.text(message, color = 'black', align = 'left', justify = 'left'),
                    width = '80%',
                    height = 'min-content',
                    align = 'right',
                    justify = 'right',
                    border_radius = '10px',#Curves the border of the bubble
                    background_color = '#f6f4da',#Shade of white/tan for the box
                ),
                rx.box(#avatar/initial box

                    align = 'left',
                    justify = 'left',
                ),
            ),

            width = '40%',
            justify = 'left',
            align = 'left',
        ),

        width = '100%',
        height = 'min-content'#value that represents the minimum height required to hold all contained elements

    )


def get_initials(name: str):
    my_str = name.split()
    return my_str[0][0] + my_str[1][0]  
