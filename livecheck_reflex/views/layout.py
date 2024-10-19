import reflex as rx
from ..templates.template import ThemeState

def create_stylesheet_link(stylesheet_url):
    """Create a link element for a stylesheet."""
    return rx.el.link(href=stylesheet_url, rel="stylesheet")


def create_subtitle_heading(subtitle_text):
    """Create a subtitle heading with specific styling."""
    return rx.heading(
        subtitle_text,
        font_weight="600",
        color="#4338CA",
        font_size="1.125rem",
        line_height="1.75rem",
        as_="h3",
    )


def create_text_span(span_text):
    """Create a simple text span element."""
    return rx.text.span(span_text)


def create_section_heading(heading_text):
    """Create a section heading with specific styling."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom="1rem",
        font_size="1.5rem",
        line_height="2rem",
        color="#3730A3",
        as_="h2",
    )


def create_highlighted_span(highlighted_text):
    """Create a highlighted span of text."""
    return rx.text.span(
        highlighted_text, font_weight="600", color="#4F46E5"
    )


def create_speaker_text(speaker_label, speaker_text):
    """Create a formatted speaker text with label and content."""
    return rx.text(
        create_highlighted_span(
            highlighted_text=speaker_label
        ),
        speaker_text,
        margin_bottom="0.75rem",
    )


def create_subtext(margin_top, subtext_content):
    """Create a subtext element with specified margin top."""
    return rx.text(
        subtext_content,
        margin_top=margin_top,
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_centered_icon(alt_text, icon_tag):
    """Create a centered icon with specified alt text and tag."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="3rem",
        margin_bottom="0.75rem",
        margin_left="auto",
        margin_right="auto",
        width="3rem",
    )


def create_highlighted_text(text_content):
    """Create highlighted text with specific styling."""
    return rx.text(
        text_content, font_weight="500", color="#4F46E5"
    )


def create_icon_with_labels(
    icon_alt, icon_tag, primary_label, secondary_label
):
    """Create an icon with primary and secondary labels."""
    return rx.box(
        create_centered_icon(
            alt_text=icon_alt, icon_tag=icon_tag
        ),
        create_highlighted_text(text_content=primary_label),
        create_subtext(
            margin_top="0.25rem",
            subtext_content=secondary_label,
        ),
        text_align="center",
    )


def create_checkmark_icon():
    """Create a checkmark icon with specific styling."""
    return rx.icon(
        alt="Checkmark",
        # tag="check-circle",
        tag="alarm_smoke",
        height="1.25rem",
        margin_right="0.75rem",
        margin_top="0.25rem",
        width="1.25rem",
    )


def create_list_item_with_checkmark(item_text):
    """Create a list item with a checkmark icon and text."""
    return rx.el.li(
        create_checkmark_icon(),
        create_text_span(span_text=item_text),
        display="flex",
        align_items="flex-start",
    )


def create_colored_bar(bar_color, bar_height):
    """Create a colored bar with specified background color and height."""
    return rx.box(
        background_color=bar_color,
        height=bar_height,
        width="20%",
    )


def create_semi_transparent_bar(bar_height):
    """Create a semi-transparent blue bar with specified height."""
    return rx.box(
        background_color="#60A5FA",
        height=bar_height,
        opacity="0.5",
        width="20%",
    )


def create_small_text_span(span_text):
    """Create a small text span with specific font size."""
    return rx.text.span(
        span_text,
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_header():
    """Create the header section with title."""
    return rx.box(
        rx.heading(
            "Discussion Mediator",
            font_weight="700",
            font_size="1.875rem",
            line_height="2.25rem",
            color="#4F46E5",
            as_="h1",
        ),
        background_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    )


def create_recording_button():
    """Create a button to start recording with microphone icon."""
    return rx.el.button(
        rx.icon(
            alt="Microphone icon",
            tag="mic",
            height="1.25rem",
            margin_right="0.5rem",
            width="1.25rem",
        ),
        " Start Recording ",
        background_color="#4F46E5",
        transition_duration="300ms",
        display="flex",
        font_weight="600",
        _hover={"background-color": "#4338CA"},
        align_items="center",
        margin_bottom="1.5rem",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_progress_bar():
    """Create a progress bar with time indicators."""
    return rx.box(
        rx.box(
            rx.box(
                background_color="#4F46E5",
                height="1rem",
                border_radius="9999px",
                width="33.333333%",
            ),
            background_color="#E5E7EB",
            height="1rem",
            margin_bottom="0.5rem",
            border_radius="9999px",
        ),
        rx.flex(
            create_text_span(span_text="0:00"),
            create_text_span(span_text="5:00"),
            display="flex",
            justify_content="space-between",
            color="#4B5563",
            font_size="0.875rem",
            line_height="1.25rem",
        ),
        max_width="28rem",
        width="100%",
    )


def create_recording_section():
    """Create the recording section with button and progress bar."""
    return rx.box(
        rx.flex(
            create_recording_button(),
            create_progress_bar(),
            display="flex",
            flex_direction="column",
            align_items="center",
        ),
        background_color="#ffffff",
        padding="2rem",
        border_radius="0.5rem",
        box_shadow="0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    )


def create_transcription_box():
    """Create a box displaying live transcription of the conversation."""
    return rx.box(
        create_speaker_text(
            speaker_label="Speaker 1:",
            speaker_text=" I believe we should increase funding for education.",
        ),
        create_speaker_text(
            speaker_label="Speaker 2:",
            speaker_text=" But where would that money come from? We're already facing budget constraints.",
        ),
        create_speaker_text(
            speaker_label="Speaker 1:",
            speaker_text=" We could reallocate funds from other areas, such as defense spending.",
        ),
        create_speaker_text(
            speaker_label="Speaker 2:",
            speaker_text=" That's a sensitive topic. We need to ensure our national security isn't compromised.",
        ),
        background_color="#ffffff",
        height="20rem",
        overflow_y="auto",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    )


def create_fact_check_item():
    """Create a fact-checking item with claim, status, and explanation."""
    return rx.box(
        create_subtitle_heading(
            subtitle_text="Claim: Education funding is insufficient"
        ),
        rx.text(
            "Status: Partially True",
            font_weight="500",
            margin_top="0.25rem",
            font_size="0.875rem",
            line_height="1.25rem",
            color="#D97706",
        ),
        create_subtext(
            margin_top="0.5rem",
            subtext_content="While education funding varies by region, many areas report underfunding issues.",
        ),
        margin_bottom="1.5rem",
    )


def create_fact_checking_box():
    """Create a box displaying fact-checking information."""
    return rx.box(
        create_fact_check_item(),
        rx.box(
            create_subtitle_heading(
                subtitle_text="Claim: Reallocating defense funds is viable"
            ),
            rx.text(
                "Status: Debatable",
                class_name="text-orange-600",
                font_weight="500",
                margin_top="0.25rem",
                font_size="0.875rem",
                line_height="1.25rem",
            ),
            create_subtext(
                margin_top="0.5rem",
                subtext_content="This is a complex issue with various economic and security implications.",
            ),
        ),
        background_color="#ffffff",
        height="20rem",
        overflow_y="auto",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    )


def create_emotion_detection_section():
    """Create a section displaying emotion detection for speakers."""
    return rx.box(
        create_section_heading(
            heading_text="Emotion Detection"
        ),
        rx.box(
            rx.flex(
                create_icon_with_labels(
                    icon_alt="Calm",
                    icon_tag="smile",
                    primary_label="Speaker 1",
                    secondary_label="Calm",
                ),
                create_icon_with_labels(
                    icon_alt="Concerned",
                    icon_tag="frown",
                    primary_label="Speaker 2",
                    secondary_label="Concerned",
                ),
                display="flex",
                justify_content="space-around",
            ),
            background_color="#ffffff",
            padding="1.5rem",
            border_radius="0.5rem",
            box_shadow="0 1px 2px 0 rgba(0, 0, 0, 0.05)",
        ),
    )


def create_mediator_suggestions_box():
    """Create a box displaying mediator suggestions."""
    return rx.box(
        rx.list(
            create_list_item_with_checkmark(
                item_text="Encourage speakers to provide specific data to support their claims."
            ),
            create_list_item_with_checkmark(
                item_text="Suggest exploring compromise solutions that address both education and security concerns."
            ),
            create_list_item_with_checkmark(
                item_text="Remind participants to maintain a respectful tone and consider each other's perspectives."
            ),
            display="flex",
            flex_direction="column",
            gap="0.875rem",
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    )


def create_emotion_trend_bars():
    """Create bars representing emotion trends."""
    return rx.flex(
        create_colored_bar(
            bar_color="#34D399", bar_height="25%"
        ),
        create_colored_bar(
            bar_color="#FBBF24", bar_height="50%"
        ),
        rx.box(
            class_name="bg-orange-400",
            height="75%",
            width="20%",
        ),
        create_colored_bar(
            bar_color="#FBBF24", bar_height="50%"
        ),
        create_colored_bar(
            bar_color="#34D399", bar_height="33.333333%"
        ),
        position="absolute",
        bottom="0",
        display="flex",
        height="100%",
        align_items="flex-end",
        left="0",
        width="100%",
    )


def create_productivity_trend_bars():
    """Create bars representing productivity trends."""
    return rx.flex(
        create_semi_transparent_bar(
            bar_height="33.333333%"
        ),
        create_semi_transparent_bar(bar_height="50%"),
        create_semi_transparent_bar(bar_height="25%"),
        create_semi_transparent_bar(bar_height="60%"),
        create_semi_transparent_bar(
            bar_height="66.666667%"
        ),
        position="absolute",
        bottom="0",
        display="flex",
        height="100%",
        align_items="flex-end",
        left="0",
        width="100%",
    )


def create_time_labels():
    """Create time labels for the trend graph."""
    return rx.flex(
        create_text_span(span_text="0:00"),
        create_text_span(span_text="1:15"),
        create_text_span(span_text="2:30"),
        create_text_span(span_text="3:45"),
        create_text_span(span_text="5:00"),
        display="flex",
        justify_content="space-between",
        color="#4B5563",
        font_size="0.75rem",
        line_height="1rem",
    )


def create_trend_graph_labels():
    """Create labels for the emotion and productivity trend graph."""
    return rx.flex(
        rx.flex(
            create_text_span(span_text="Calm"),
            create_text_span(span_text="Concerned"),
            create_text_span(span_text="Frustrated"),
            display="flex",
            justify_content="space-between",
            color="#4B5563",
            font_size="0.75rem",
            line_height="1rem",
        ),
        create_time_labels(),
        position="absolute",
        display="flex",
        flex_direction="column",
        height="100%",
        justify_content="space-between",
        left="0",
        padding="1rem",
        top="0",
        width="100%",
    )


def create_trend_graph():
    """Create a graph showing emotion and productivity trends."""
    return rx.box(
        rx.box(
            create_emotion_trend_bars(),
            create_productivity_trend_bars(),
            create_trend_graph_labels(),
            height="100%",
            position="relative",
            width="100%",
        ),
        background_color="#F3F4F6",
        height="16rem",
        overflow="hidden",
        border_radius="0.5rem",
        width="100%",
    )


def create_trend_legend():
    """Create a legend for the emotion and productivity trend graph."""
    return rx.flex(
        rx.flex(
            rx.box(
                background_color="#34D399",
                height="1rem",
                margin_right="0.5rem",
                width="1rem",
            ),
            create_small_text_span(
                span_text="Emotional State"
            ),
            display="flex",
            align_items="center",
        ),
        rx.flex(
            rx.box(
                background_color="#60A5FA",
                height="1rem",
                margin_right="0.5rem",
                opacity="0.5",
                width="1rem",
            ),
            create_small_text_span(
                span_text="Productivity Level"
            ),
            display="flex",
            align_items="center",
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_top="1rem",
    )


def create_main_content():
    """Create the main content section of the application."""
    return rx.box(
        create_recording_section(),
        rx.box(
            rx.box(
                create_section_heading(
                    heading_text="Live Transcription"
                ),
                create_transcription_box(),
            ),
            rx.box(
                create_section_heading(
                    heading_text="Fact-Checking"
                ),
                create_fact_checking_box(),
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
        ),
        create_emotion_detection_section(),
        rx.box(
            create_section_heading(
                heading_text="Mediator Suggestions"
            ),
            create_mediator_suggestions_box(),
        ),
        rx.box(
            create_section_heading(
                heading_text="Emotion and Productivity Trends"
            ),
            rx.box(
                create_trend_graph(),
                create_trend_legend(),
                background_color="#ffffff",
                padding="1.5rem",
                border_radius="0.5rem",
                box_shadow="0 1px 2px 0 rgba(0, 0, 0, 0.05)",
            ),
        ),
        display="flex",
        flex_direction="column",
        gap="2rem",
    )


def create_main_layout():
    """Create the main layout of the application."""
    return rx.fragment(
        create_stylesheet_link(
            stylesheet_url="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
        ),
        create_stylesheet_link(
            stylesheet_url="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap"
        ),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }
        body {
            font-family: 'Inter', sans-serif;
        }
    """
        ),
        rx.box(
            rx.box(
                create_header(),
                create_main_content(),
                max_width="64rem",
                margin_left="auto",
                margin_right="auto",
                padding="1rem",
            ),
            background_color="#F9FAFB",
            color="#1F2937",
        ),
    )