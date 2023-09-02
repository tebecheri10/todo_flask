from my_todo_list import db

class Todo(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    content = db.Column( db.String(200), nullable=False )
    completed = db.Column( db.Boolean, default=False )
    def __repr__(self):
        return f"<Task {self.id}>"

