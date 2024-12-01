from app import app
from models import db, Book

with app.app_context():
    db.create_all()
    # Добавление книг в базу данных
    book1 = Book(title='Зов Ктулху', author='Говард Ф.Л.', price=500)
    book2 = Book(title='Остров сокровищ', author='Стивенсон Р.Л.', price=400)
    book3 = Book(title='Полдень, XXII век', author='Стругацкий А.Н., Стругацкий Б.Н.', price=600)
    db.session.add_all([book1, book2, book3])
    db.session.commit()