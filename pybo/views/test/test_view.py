from flask import Blueprint, render_template, request
from pybo import db
from pybo.models import Question
from pybo.test_models import Person, Car
from werkzeug.utils import redirect

# 경로 -> 상대경로 -> 자기자신 기준.
#      -> 절대경로 -> 루트(최상위) 기준
# 라우팅 해주는 객체
bp = Blueprint('test', __name__, url_prefix="/test")

# /는 서버 주소를 의미 -> 127.0.0.1:5000/hello
@bp.route('/filter')
def filter() :
    return render_template('test/filter.html')

@bp.route('/hello')
def hello() :
    return "hello"

@bp.route('/bye')
def bye() :
    return "bye"

@bp.route('/introduce')
def introduce() :
    return "my name is cha"

@bp.route('/print_person/<int:no>')
def print_person(no) :
    
    #p1 = db.session.query(Person).first()
    # 여러개인가 한개인가
    # p1 = db.session.query(Person).filter(Person.no == 3).all()
    p2 = db.session.query(Person).filter(Person.no == no).first()
    
    return "{}살 {}사는 {}입니다.".format(p2.age, p2.address, p2.name)
    # return ""

@bp.route('/print_car/<int:no>')
def print_car(no) :
    c1 = db.session.query(Car).filter(Car.no == no).first()

    return "{} {}만원짜리 {}".format(c1.color, c1.price, c1.model)


@bp.route('/gugu')
def gugu() :
    return render_template('gugu.html')

@bp.route('/discount/<int:age>')
def discount(age) :
    
    return render_template('discount.html', age=age)

@bp.route('car_list')
def test() :
    
    c1 = db.session.query(Car).filter(Car.model == "아반떼").first()
    car_list = db.session.query(Car).all()
    
    return render_template('test.html', car_list=car_list)

@bp.route('add_car')
def add_car() :
    
    model = request.args.get('model')
    price = request.args.get('price')
    color = request.args.get('color')
    
    c1 = Car(model=model, price=price, color=color)
    db.session.add(c1)
    db.session.commit()
    
    return redirect('car_list')

@bp.route('car_form')
def car_form() :
    
    return render_template('car_form.html')

@bp.route('delete_car')
def delete_car() :
    db.session.query(Car).delete()
    db.session.commit()
    
    return redirect('car_list')
    
    
@bp.route('page_test')
def page_test() :
    question_list = Question.query.order_by(Question.create_date.desc())

    
    return render_template('test/page_test.html', question_list=question_list)
    
    
    