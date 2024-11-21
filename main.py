import mesop as me
import image_generation_module


ROOT_BOX_STYLE = me.Style(
    background="#e7f2ff",
    font_family="Inter",
    display="flex",
    flex_direction="column",
)

#상태관리
@me.stateclass
class State:
    input: str = ""
    image_url :str = ""


# Replace page() with this:
@me.page(
    path="/",
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap"
    ],
)
def page():
    with me.box(style=ROOT_BOX_STYLE):
        header()
        with me.box(
            style=me.Style(
                width="min(680px, 100%)",
                margin=me.Margin.symmetric(horizontal="auto", vertical=36),
            )
        ):
            me.text(
                "[예제1]이미지 생성하기 프로토타입",
                style=me.Style(font_size=20, margin=me.Margin(bottom=24)),
            )
            chat_input()
            print_result()
        with me.box(
            style=me.Style(
                width="min(680px, 100%)",
                margin=me.Margin.symmetric(horizontal="auto", vertical=36),
            )
        ):
            me.text(
                "[예제2] 이미지 생성하기 프로토타입",
                style=me.Style(font_size=20, margin=me.Margin(bottom=24)),
            )
            chat_input()
            print_result()

def header():
    with me.box(
        style=me.Style(
            padding=me.Padding.all(16),
        ),
    ):
        me.text(
            "퓨쳐드릴 63호 프로토타입 만들기",
            style=me.Style(
                font_weight=500,
                font_size=24,
                color="#3D3929",
                letter_spacing="0.3px",
            ),
        )

def chat_input():
    state = me.state(State)
    with me.box(
        style=me.Style(
            border_radius=16,
            padding=me.Padding.all(8),
            background="white",
            display="flex",
            width="100%",
        )
    ):
        with me.box(style=me.Style(flex_grow=1)):
            me.native_textarea(
                value=state.input,
                placeholder="Enter a prompt",
                style=me.Style(
                    padding=me.Padding(top=16, left=16),
                    outline="none",
                    width="100%",
                    border=me.Border.all(me.BorderSide(style="none")),
                ),
            )
        with me.content_button(type="icon", on_click=send_prompt):
            me.icon("send")

def print_result():
    state = me.state(State) 
    with me.box(
        style=me.Style(
            padding=me.Padding.all(16),
        ),
    ):
        with me.box(style=me.Style(margin=me.Margin.all(15))):
            # URL 출력 (디버깅 용도)
            me.image(
                src=state.image_url,
                alt=state.input,
                style=me.Style(width="60%"),
            )


def send_prompt(e: me.ClickEvent):
    state = me.state(State)
    input = state.input
    state.input = ""
    state.image_url = image_generation_module.send_prompt_flash(input)