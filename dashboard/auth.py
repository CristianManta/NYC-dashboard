def get_user(request):
    username = request.get_argument('username')
    password = request.get_argument('password')

    if username == 'nyc' and password == 'iheartnyc':
        return 1
    else:
        return None

# Don't worry about this too much
login_url = '/login'
