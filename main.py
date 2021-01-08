from fastapi import FastAPI,requests
from pydantic import BaseModel
import sqlite3 

class Database: 
    def __init__(self):
        self.conn = sqlite3.connect('main.db')
        self.c = self.conn.cursor()
    @property
    def table(self): 
        data = """
        CREATE TABLE product(
            id INTEGER PRIMARY KEY,
            name_product TEXT,
            price INTEGER
            )
            """
        self.c.execute(data)
        self.conn.commit()
    def create(self, *data):
        self.c.execute("INSERT INTO product(name_product, price) VALUES(?, ?)", data)
        self.conn.commit()
        
    def delete(self, id): 
         self.c.execute(f"DELETE FROM product WHERE id={id}")
         self.conn.commit()
         
    def update(self, *data): 
        self.c.execute("UPDATE product SET name_product=?, price=? WHERE id=?", data)
        self.conn.commit()
    @property
    def all_data(self): 
            return  self.c.execute("SELECT * FROM product")
         
    def detail_data(self, id):
        self.c.execute(f'SELECT * FROM product WHERE id = {id}')
        return self.c.fetchone() 
        
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index(): 
    data =Database().all_data
    row =[
        {'id': i[0], 'name_product': i[1], 'price': i[2]} 
        for i in data
    ]
    return row
class Item(BaseModel): 
       name_product: str
       price: int 
@app.post('/', status_code=201)
def create(item: Item): 
    data =item.dict()
    Database().create(data['name_product'], data['price'])
    return item

@app.delete('/{id}')
def delete_data(id: int):
    data = Database().detail_data(id)
    if not data: 
        return {'msg': 'not found'} 
    Database().delete(id)
    return {"msg": "Success Delete Data"} 


@app.get('/{id}')
def details(id: int): 
    data = Database().detail_data(id)
    if not data: 
        return {"msg": 'not fount'}
    return {'id': data[0], 'name_product': data[1], 'price': data[2]}

@app.put('/{id}')
def update_data(item: Item,id: int): 
    data = Database().detail_data(id)
    if not data:
        return {"msg": 'not fount'}
    data = item.dict()
    Database().update(data['name_product'], data['price'], id)
    return data
