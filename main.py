from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session , engine
import database_models
from sqlalchemy.orm import Session


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)


products = [
    Product(
        id=1,
        name="Laptop",
        description="A basic machine",
        price=1299,
        quantity=10,
    ),
    Product(
        id=2, name="mouse", description="A basic machine", price=199, quantity=14
    ),
    Product(
        id=3,
        name="keyboard",
        description="A basic machine",
        price=129,
        quantity=12,
    ),
    Product(
        id=4,
        name="monitor",
        description="A basic machine",
        price=299,
        quantity=11,
    ),
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()

    count = db.query(database_models.Product).count

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()

    

init_db()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}


@app.get("/products")
def get_all_products(db:Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products


@app.get("/products/{id}")
def get_product(id: int,db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products")
def create_product(product: Product,db:Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit() 
    # every time we make changes to db we need to commit
    # products.append(product)
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product, db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.quantity = product.quantity
        db_product.price = product.price
        db.commit()
        return "Product updated"
    else:
        return "No product found"

@app.delete("/products/{id}")
def delete_product(id: int, db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted"
    else:
        return "No product found"
