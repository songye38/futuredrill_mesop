import mesop as me
import openai
import os


def generate_image(prompt: str):
    try:
        # 이미지 생성 요청
        response = openai.Image.create(
            prompt=prompt,
            n=1,  # 생성할 이미지 수
            size="1024x1024"  # 이미지 크기
        )
        # 생성된 이미지 URL 반환
        return response['data'][0]['url']
    except Exception as e:
        return f"이미지 생성 중 오류 발생: {e}"

def send_prompt_flash(user_prompt: str,user_style :str):
    openai.api_key = os.getenv("OPENAI_API_KEY") #API 키 설정

    if user_style == "A":
        # A 스타일: 일러스트 스타일
        prompt = f"Illustration of {user_prompt}"  # 예시로 'Illustration of'를 추가
    elif user_style == "B":
        # B 스타일: 실사 스타일
        prompt = f"Realistic photo of {user_prompt}"  # 예시로 'Realistic photo of'를 추가


    image_url = generate_image(prompt) #프롬프트 넣기 
    print("생성된 이미지 URL:", image_url)
    return image_url
