from flask import Blueprint, render_template, request
from pybo import db
from pybo.test_models import Car, Person
from pybo.form.person_form import PersonForm
from werkzeug.utils import redirect

bp = Blueprint('person', __name__, url_prefix="/person")

@bp.route('list')
def test() :
    person_list = db.session.query(Person).all()
    return render_template('person_list.html', person_list=person_list)

@bp.route('person_form')
def person_form() :
    
    return render_template('person_form.html')

@bp.route('add_person', methods=("GET", "POST")) # default - GET, POST
def add_person() :
    
    form = PersonForm()
    if form.validate_on_submit() and request.method == "POST": # 입력 제대로 했는지 체크. 제대로 했으면 True, 안했으면 False
    
        address = form.address.data
        age = form.age.data
        name = form.name.data
        
        # 여기에 데이터 체크
        
        p1 = Person(name=name, age=age, address=address)
        db.session.add(p1)
        db.session.commit()
        
        return redirect('person_list')
    
    return render_template('person_form.html', form=form)