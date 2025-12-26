import aiohttp
from config import API_BASE_URL


class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL
    
    async def get_categories(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}/categories/') as resp:
                return await resp.json()
    
    async def get_products_by_category(self, category_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f'{self.base_url}/products/by-category/{category_id}/'
            ) as resp:
                return await resp.json()
    
    async def get_product(self, product_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}/products/{product_id}/') as resp:
                return await resp.json()
    
    async def create_order(self, order_data: dict):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f'{self.base_url}/orders/',
                json=order_data
            ) as resp:
                return await resp.json()


api = APIClient()