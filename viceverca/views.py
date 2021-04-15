from django.shortcuts import render 
def home(request):
    return render(request, 'home.html')
def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    words_text = len(user_text.split())
    print(user_text)
    return render(request, 'reverse.html', {'usertext':user_text , 'reversedtext':reversed_text, 'words':words_text})