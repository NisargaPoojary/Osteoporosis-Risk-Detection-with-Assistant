from django.shortcuts import render
from django.http import JsonResponse
import openai
import json
from decouple import config

openai.api_base = "https://integrate.api.nvidia.com/v1"
openai.api_key = config('NVIDIA_API_KEY')  

system_message = {"role": "system", "content": "You are a helpful assistant."}
messages = [system_message]

def chatbot_view(request):
    if request.method == "GET":
        return render(request, "index.html")

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            user_input = data.get("message", "").strip()

            if not user_input:
                return JsonResponse({"error": "No input provided."}, status=400)

            messages.append({"role": "user", "content": user_input})

            response = openai.ChatCompletion.create(
                model="nvidia/llama-3.1-nemotron-70b-instruct",
                messages=messages,
                temperature=0.5,
                max_tokens=1024,
                stream=False
            )

            bot_reply = response['choices'][0]['message']['content']
            bot_reply_lines = bot_reply.split("\n")
            formatted_reply = []
            for line in bot_reply_lines:
                clean_line = line.replace("*", "").replace("#", "").strip()
                if clean_line:
                    if clean_line.endswith(":"):
                        formatted_reply.append(f"\n{clean_line}")
                    else:
                        formatted_reply.append(f"{clean_line}")

            bot_reply = "\n".join(formatted_reply).strip()

            messages.append({"role": "assistant", "content": bot_reply})

            return JsonResponse({"reply": bot_reply})

        except Exception as e:
            return JsonResponse({"error": f"API error: {str(e)}"}, status=500)
