# farmsupport/views.py

from django.shortcuts import render
from django.http import JsonResponse

def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get("user_message")
        
        # Here we handle chatbot responses directly
        if "weather" in user_message.lower():
            bot_response = "The weather today is sunny and warm."
        elif "soil" in user_message.lower():
            bot_response = "The soil is well-nourished."
        elif "help" in user_message.lower():
            bot_response = "How can I assist you further?"
        else:
            bot_response = "Sorry, I didn't understand that. Can you ask something else?"
        
        return JsonResponse({"message": bot_response})
    
    return render(request, "chatbot.html")








