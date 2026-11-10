from Podii.accounts.models import User


def update_user_profile(user, data):
  if 'first_name' in data:
    user.first_name = data['first_name']
  if 'last_name' in data:
    user.last_name = data['last_name']

  user.save()
  return user