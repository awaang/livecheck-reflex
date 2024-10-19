"""The home page."""

from ..templates import template
from ..backend.table_state import TableState
from ..views.layout import create_main_layout

import reflex as rx

# @template(route="/", title="Home", on_load=TableState.load_entries)
@template(route="/home", title="Home")
def home() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.vstack(
        rx.heading("User Dashboard", size="5"),
        create_main_layout(),
        spacing="8",
        width="100%",
    )