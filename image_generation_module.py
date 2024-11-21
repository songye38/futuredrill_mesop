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

def send_prompt_flash(user_prompt: str):
    openai.api_key = os.getenv("OPENAI_API_KEY") #API 키 설정
    image_url = generate_image(user_prompt) #프롬프트 넣기 
    print("생성된 이미지 URL:", image_url)
    return image_url
