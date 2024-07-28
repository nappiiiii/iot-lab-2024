from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import models
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
router_v1 = APIRouter(prefix='/api/v1')
router_v2 = APIRouter(prefix='/api/v2')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils

@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router_v1.get('/books/{book_id}')
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

@router_v1.post('/books')
async def create_book(book: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newbook = models.Book(title=book['title'], author=book['author'], year=book['year'], is_published=book['is_published'], detail=book['detail'], info=book['info'], category=book['category'])
    db.add(newbook)
    db.commit()
    db.refresh(newbook)
    response.status_code = 201
    return newbook

@router_v1.patch('/books/{book_id}')
async def update_book(book_id: int, book: dict, db: Session = Depends(get_db)):
    update_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    update_book.title = book['title']
    update_book.author = book['author']
    update_book.year = book['year']
    update_book.is_published = book['is_published']
    update_book.detail = book['detail']
    update_book.info = book['info']
    update_book.category = book['category']
    db.commit()
    db.refresh(update_book)
    Response.status_code = 200
    return update_book

@router_v1.delete('/books/{book_id}')
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    db.delete(book)
    db.commit()
    return

@router_v1.get('/beverages')
async def get_beverages(db: Session = Depends(get_db)):
    return db.query(models.Beverage).all()

@router_v1.get('/beverages/{beverage_id}')
async def get_beverage(beverage_id: int, db: Session = Depends(get_db)):
    return db.query(models.Beverage).filter(models.Beverage.id == beverage_id).first()

@router_v1.post('/beverages')
async def create_beverage(beverage: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newbeverage = models.Beverage(name=beverage['name'], price=beverage['price'], detail=beverage['detail'])
    db.add(newbeverage)
    db.commit()
    db.refresh(newbeverage)
    response.status_code = 201
    return newbeverage

@router_v1.patch('/beverages/{beverage_id}')
async def update_beverage(beverage_id: int, beverage: dict, db: Session = Depends(get_db)):
    update_beverage = db.query(models.Beverage).filter(models.Beverage.id == beverage_id).first()
    update_beverage.name = beverage['name']
    update_beverage.price = beverage['price']
    update_beverage.detail = beverage['detail']
    db.commit()
    db.refresh(update_beverage)
    Response.status_code = 200
    return update_beverage

@router_v1.delete('/beverages/{beverage_id}')
async def delete_beverage(beverage_id: int, db: Session = Depends(get_db)):
    beverage = db.query(models.Beverage).filter(models.Beverage.id == beverage_id).first()
    db.delete(beverage)
    db.commit()
    return

@router_v1.get('/orders')
async def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@router_v1.get('/orders/{order_id}')
async def get_order(order_id: int, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

@router_v1.post('/orders')
async def create_order(order: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    neworder = models.Order(name=order['name'], price=order['price'], amount=order['amount'], ps=order['ps'])
    db.add(neworder)
    db.commit()
    db.refresh(neworder)
    response.status_code = 201
    return neworder

# @router_v1.patch('/orders/{order_id}')
# async def update_order(order_id: int, order: dict, db: Session = Depends(get_db)):
#     update_order = db.query(models.Order).filter(models.Order.id == order_id).first()
#     update_order.name = order['name']
#     update_order.price = order['price']
#     update_order.amount = order['amount']
#     update_order.ps = order['ps']
#     db.commit()
#     db.refresh(update_order)
#     Response.status_code = 200
#     return update_order

@router_v1.delete('/orders/{order_id}')
async def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    db.delete(order)
    db.commit()
    return

######################################################################################################

@router_v1.get('/students')
async def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@router_v1.get('/students/{student_id}')
async def get_student(student_id: int, db: Session = Depends(get_db)):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

@router_v1.post('/students')
async def create_student(student: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newstudent = models.Student(id=student['id'], name=student['name'], lastname=student['lastname'], dob=student['dob'], gender=student['gender'], email=student['email'])
    db.add(newstudent)
    db.commit()
    db.refresh(newstudent)
    response.status_code = 201
    return newstudent

@router_v1.patch('/students/{student_id}')
async def update_student(student_id: int, student: dict, db: Session = Depends(get_db)):
    update_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    update_student.name = student['name']
    update_student.lastname = student['lastname']
    update_student.dob = student['dob']
    update_student.gender = student['gender']
    update_student.email = student['email']
    db.commit()
    db.refresh(update_student)
    Response.status_code = 200
    return update_student

@router_v1.delete('/students/{student_id}')
async def delete_student(student_id: int, response: Response, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    db.delete(student)
    db.commit()
    response.status_code = 204
    return

app.include_router(router_v1)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)