from flask import render_template, request, redirect, url_for
from my_todo_list import app, db
from my_todo_list.models import Todo
from my_todo_list.forms import MyTodoForm

@app.route("/" , methods=['GET', 'POST'])
def home():
    todos = Todo.query.all()
    form = MyTodoForm()
    
    if request.method == "POST":
        if form.validate_on_submit():
            todo = Todo(content=form.content.data, completed=form.completed.data)
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for("home"))
        
    return render_template("home.html", todos=todos, form=form)

@app.route("/delete/<int:todo_id>", methods=["GET","DELETE"])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    
    return redirect(url_for("home"))