from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# In-memory storage for questions and leaderboard
questions = [
    {
        "id": 1,
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris",
    },
    {
        "id": 2,
        "question": "What is the capital of Spain?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Madrid",
    },
    {
        "id": 3,
        "question": "What is the capital of Germany?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Berlin",
    },
    {
        "id": 4,
        "question": "What is the capital of England?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "London",
    },
]

leaderboardId = 1

leaderboard = []


@api_view(['GET'])
def get_questions(request):
    return Response(questions)

@api_view(['POST'])
def update_leaderboard(request):
    data = request.data
    
    global leaderboardId
    
    data["id"] = leaderboardId
    leaderboardId += 1
    
    leaderboard.append(data)

    leaderboard.sort(key=lambda x: x["score"], reverse=True)

    if len(leaderboard) > 10:
        leaderboard.pop()

    return Response(leaderboard, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_leaderboard(request):
    return Response(leaderboard)
