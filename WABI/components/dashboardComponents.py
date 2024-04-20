import reflex as rx




def challengeBox(*, title, body, reward, img):
    return rx.box()
    pass

def startButton(click_func: 'function'):
    return rx.button(
        "Start Now",
        width='90px',
        height='36px',
        align_items='center',  # Ensures content is centered within the button
        justify_content='center',  # Additionally centers content horizontally
        border_radius='14px',
        background_color='#5e24ff',
        color='white',  # Text color
        font_size='14px',
        line_height='20px',
        font_family="""Plus Jakarta Sans, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif""",
        text_align='center',  # Ensures text alignment is centered
        on_click=click_func  # Event handler for click
    )
    

def challengeTextBox(head, body, reward):
    return rx.box(rx.vstack(challengeHeaderBox(head), challengeBodyBox(body, reward), width = '237px', height = '100px',
                            align_items = 'flex-start'))

def challengeHeaderBox(text):
    return rx.box(rx.text(text, color = '#200a5c', font_size = '18px', line_height = '28px', font_weight = 'bold', font_family = 
"Plus Jakarta Sans, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans','Liberation Sans', sans-serif",
    letter_spacing = '-0.33px', left = '0', top = '-0.5px', width = 'min-content', height = 'min-content', white_space = 'nowrap',
    flex_direction = 'column'), align_items = 'flex-start', width = '100%', height = '28px', position = 'relative')

def challengeBodyBox(body, reward):
    return rx.box(rx.vstack(challengeSmallText(body),challengeSmallText(reward), spacing = '4'), align_items = 'flex-start')

def challengeSmallText(text:str):
    return rx.box(rx.text(text, color = '#220f57', font_size = '14px', line_height = '20px', 
                          font_family = "Plus Jakarta Sans, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans','Liberation Sans', sans-serif",
                          position = 'absolute', width = '100%', height = 'min-content', flex_direction = 'column'))