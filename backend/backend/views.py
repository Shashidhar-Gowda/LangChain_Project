from django.shortcuts import render
from django.http import JsonResponse
import random  # Simulating chatbot logic for now

def chatbot_view(request):
    responses = [
        "Hello! How can I help you?",
        "I'm here to assist you.",
        "Can you please rephrase your question?",
        "I'm just a simple chatbot in Django!"
    ]
    response = random.choice(responses)  # Pick a random response
    return JsonResponse({"response": response})
