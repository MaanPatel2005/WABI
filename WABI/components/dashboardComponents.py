import reflex as rx


def challengeBox(*, title, body, reward, img):
    return rx.box()
    pass

def challengeBodyBox(body, reward):
    return rx.box(rx.vstack(challengeSmallText(body),challengeSmallText(reward)), align_items = 'flex-start')

def challengeSmallText(text:str):
    return rx.box(rx.text(text, color = '#220f57', font_size = '14px', line_height = '20px', 
                          font_family = "Plus Jakarta Sans, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans','Liberation Sans', sans-serif",
                          position = 'absolute', width = '100%', height = 'min-content', flex_direction = 'column'))