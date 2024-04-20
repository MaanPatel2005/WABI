import reflex as rx



def challengeBox(*, head, body, reward, img, click_func, ThemeState):
    try: 
        rx.console_log("challengeBox About to run: ")
        return rx.box(rx.image(src = img, width = '100%', height = '60%'), 
                  challengeTextBubble(head, body, reward, click_func, ThemeState), height = 'max-content', width = '30%'
                  , backgroundColor = f'{ThemeState.accent_color}', justify_content = 'flex-end')
    except: 
        rx.console_log("challengeBox Didn't run as it should have...")

def challengeTextBubble(head, body, reward, click_func, ThemeState):
    try: 
        rx.console_log("ChallengeTextBubble About to run: ")
        return rx.box(challengeTextBox(head,body,reward, ThemeState), 
                  startButton(click_func, ThemeState), width = '100%', height = 'max-content', padding_left = '5%')
    except: 
        rx.console_log("ChallengeTextBubble ended up failing")


def startButton(click_func: 'function', ThemeState):
    return rx.button(
        "Start Now",
        width='90px',
        height='36px',
        left = '70%',
        position = 'relative',
        align_items='center',  # Ensures content is centered within the button
        justify_content='center',  # Additionally centers content horizontally
        border_radius='14px',
        background_color='#5e24ff',
        color='white',  # Text color
        font_size='14px',
        line_height='20px',
        font_family="""Plus Jakarta Sans, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif""",
        text_align='center',  # Ensures text alignment is centered
        on_click=click_func()  # Event handler for click
    )
    

def challengeTextBox(head, body, reward, ThemeState):
    return rx.box(rx.vstack(challengeHeaderBox(head, ThemeState), 
                            challengeBodyBox(body, reward)),
                        width = '65%',
                        height = 'fit-content',
                        align_items = 'flex-start')

def challengeHeaderBox(text, ThemeState):
    return rx.box(rx.text(text, 
                          color = 'black', 
                          font_size = '18px', 
                          line_height = '28px', 
                          font_weight = 'bold', 
                          font_family = "Plus Jakarta Sans, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans','Liberation Sans', sans-serif",
                          letter_spacing = '-0.33px', 
                          left = '0', top = '-0.5px',
                          width = 'min-content', 
                          height = 'min-content', 
                          white_space = 'nowrap',
                          flex_direction = 'column'), 
                align_items = 'flex-start', 
                width = '100%', 
                height = 'max-content', 
                position = 'relative')

def challengeBodyBox(body, reward):
    rx.console_log('challengeBodyBox')
    return rx.box(rx.vstack(challengeSmallText(body),challengeSmallText(reward), 
                            spacing = '4'), 
                            align_items = 'flex-start',
                            background_color = 'blue')

def challengeSmallText(text:str):
    return rx.box(rx.text(text, color = 'black', font_size = '14px', line_height = '20px', 
                          font_family = "Plus Jakarta Sans, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans','Liberation Sans', sans-serif",
                          position = 'absolute', width = '100%', height = 'min-content', flex_direction = 'column'))