from .models import Profile


# type is the kind of exec member needed
def get_user_on_type(type):
    if type == "Professional":
        return Profile.objects.filter(isProfDirector=True)[0]
    if type == "Philanthropy":
        return Profile.objects.filter(isPhilDirector=True)[0]
    if type == "Tech":
        return Profile.objects.filter(isTechDirector=True)[0]
    if type == "President":
        return Profile.objects.filter(isPresident=True)[0]
    if type == "VP":
        return Profile.objects.filter(isVP=True)[0]
    if type == "Social":
        return Profile.objects.filter(isSocialDirector=True)[0]

    return -1