from rest_framework.authtoken.models import Token

def generate_token(user):
    # Check if the user already has a token
    token, created = Token.objects.get_or_create(user=user)
    # If a token was not created, delete the old one and generate a new one
    if not created:
        token.delete()
        token = Token.objects.create(user=user)
    return token.key
