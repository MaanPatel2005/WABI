import reflex as rx



def challengeBox(*, head, body, reward, img, click_func, ThemeState):
    return rx.box( challengeImg(img),
                challengeTextBubble(head, body, reward, click_func, ThemeState), height = 'min-content', width = '29%'
                  , backgroundColor = f'{ThemeState.accent_color}', border_radius = '10px', justify_content = 'flex-end',
                  box_sizing = 'border-box', padding_bottom = '1%')

def challengeImg(img):
    return rx.image(src = img, width = '100%', height = '200px')

def challengeTextBubble(head, body, reward, click_func, ThemeState):
    rx.console_log("ChallengeTextBubble About to run: ")
    return rx.box(challengeTextBox(head,body,reward, ThemeState), 
                startButton(click_func, ThemeState), width = '100%', 
                height = 'max-content', padding_left = '5%',
                bottom = '0', position = 'relative', align_items = 'flex-end')


def startButton(click_func: 'function', ThemeState):
    return rx.button(
        "Start Now",
        width='28%',
        height='36px',
        position = 'absolute',
        right = '2%',
        bottom = '10px',
        align_items='center',  # Ensures content is centered within the button
        justify_content='center',  # Additionally centers content horizontally
        border_radius='14px',
        background_color='#5e24ff',
        color='white',  # Text color
        font_size='13px',
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
                        align_items = 'flex-start',
                        box_sizing = 'border-box')

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
                position = 'relative',
                box_sizing = 'border-box')

def challengeBodyBox(body, reward):
    return rx.box(rx.vstack(challengeSmallText(body),challengeSmallText(reward), 
                            spacing = '1'), 
                            align_items = 'flex-start',
                            height = 'min-content',
                            width = '100%',
                            box_sizing = 'border-box')

def challengeSmallText(text:str):
    return rx.box(rx.text(text, color = 'black', font_size = '14px', line_height = '20px', 
                          font_family = "Plus Jakarta Sans, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans','Liberation Sans', sans-serif",
                          position = 'relative', width = '100%', height = 'min-content', flex_direction = 'column'),
                          box_sizing = 'border-box')