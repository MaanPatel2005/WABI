from .dashboard import dashboard
from .index import index
from .settings import settings
from .leaderboard import leaderboard
from .buddy_finder import buddy_finder
from WABI.components.login import authenticate
import reflex as rx

class AppState(rx.State):
    is_authenticated: bool = False  # Track authentication status

def authentication():
    return rx.redirect('/authenticate')

app = rx.App()
authentication()