




class TweetService:
    def __init__(self, items_repo: AbstractRepository):
        self.items_repo: AbstractRepository = items_repo()

    async def add_item(self, item: ItemWrite):
        product_dict = item.model_dump()
        if product_dict['amount'] < 0:
                raise RequestValidationError("не может быть отрицательной цены!")
        product_id = await self.items_repo.add_one(product_dict)
        return product_id

    async def get_items(self):
        return await self.items_repo.find_all()

    async def update_info(self, id: int, new_data: ItemUpdate)->str:
        dict = new_data.model_dump()
        if dict['amount'] < 0:
                raise RequestValidationError("не может быть отрицательной цены!")
        return await self.items_repo.update_info(id, dict)

    async def delete_item(self, id)->str:
        return  await self.items_repo.delete_item(id)