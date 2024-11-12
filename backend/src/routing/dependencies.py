from app.repositories.item import ItemRepository
from app.repositories.user import UserRepository
from app.services.item import ItemService
from app.services.user import UserService


def user_service():
    return UserService(UserRepository)


def item_service():
    return ItemService(ItemRepository)