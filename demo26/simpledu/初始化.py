from simpledu.modes import User , Course
from demo26.manage import  app,db

db.create_all(app=app)
# app.app_context().push()
# def my_function():
#     with app.app_context():
#         user = User(username='admin')
#         course1 = Course(name='python course', author=user)
#         course2 = Course(name='java course', author=user)
#
#         db.session.add(user)
#         db.session.add(course1)
#         db.session.add(course2)
#         db.session.commit()
# my_function()
