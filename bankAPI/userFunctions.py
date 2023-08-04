from .models import User


def getUserById(id):
    fields = [
        "name",
        "lastName",
        "address",
        "phoneNumber",
        "email",
        "birthDate",
        "genre",
    ]
    usersData = User.objects.filter(id == id).values(*fields)
    return usersData
