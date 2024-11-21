import mesop as me
import image_generation_module


ROOT_BOX_STYLE = me.Style(
    background="#e7f2ff",
    height = '100%',
    font_family="Inter",
    display="flex",
    flex_direction="column",
)

#상태관리
@me.stateclass
class State:
    input: str = ""
    image_url :str = ""
    selected_style: str = "A"  # 선택된 스타일 (기본 A)


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
            style_selector()  # 스타일 선택 버튼
            chat_input()
            print_result()

# 스타일 선택 버튼
def style_selector():
    state = me.state(State)
    
    with me.box(style=me.Style(display="flex", margin=me.Margin(bottom=20))):
        # A 스타일 버튼 (일러스트 스타일)
        with me.box(style=me.Style(margin=me.Margin(right=10))):
            me.button(
                "일러스트 스타일(A)",
                on_click=lambda e: set_style("A"),  # 클릭 시 A 스타일로 설정
                style=me.Style(background="#4CAF50", color="white", padding=me.Padding.all(10)),
            )
        # B 스타일 버튼 (실사 스타일)
        with me.box(style=me.Style(margin=me.Margin(right=10))):
            me.button(
                "실사 스타일(B)",
                on_click=lambda e: set_style("B"),  # 클릭 시 B 스타일로 설정
                style=me.Style(background="#008CBA", color="white", padding=me.Padding.all(10)),
            )

# 스타일 설정 함수
def set_style(style: str):
    state = me.state(State)
    state.selected_style = style  # 선택된 스타일 업데이트

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
                on_blur=on_blur,
                style=me.Style(
                    padding=me.Padding(top=16, left=16),
                    outline="none",
                    width="100%",
                    border=me.Border.all(me.BorderSide(style="none")),
                ),
            )
        with me.content_button(type="icon", on_click=send_prompt):
            me.icon("send")


def on_blur(e: me.InputBlurEvent):
    state = me.state(State)
    state.input = e.value
    print("on_blur에서 state.input 업데이트:", state.input)  # 디버그 출력


# 사용자가 입력한 프롬프트를 처리하고 이미지를 생성
def send_prompt(e: me.ClickEvent):
    state = me.state(State)
    input_text = state.input
    state.input = ""  # 입력 필드 초기화

    # 스타일에 따른 이미지 생성
    if state.selected_style == "A":
        # A 스타일 (예: 일러스트 스타일)
        state.image_url = image_generation_module.send_prompt_flash(input, "A")  # 스타일 파라미터 전달

    elif state.selected_style == "B":
        # B 스타일 (예: 실사 스타일)
        state.image_url = image_generation_module.send_prompt_flash(input, "B")  # 스타일 파라미터 전달