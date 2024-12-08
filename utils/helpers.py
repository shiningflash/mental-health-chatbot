import base64

def format_chat_message(role: str, content: str) -> dict:
    return {"role": role, "content": content}

def get_base64_image(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")