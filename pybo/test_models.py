# 경로 -> . : 자기 자신이 있는 폴더
from pybo import db

class Person(db.Model) :
    # 자료형 -> 길이가 있는 문자, 길이가 없는 문자, 숫자, 날짜
    # 사람을 식별할 번호
    no = db.Column(db.Integer, primary_key=True) # primary_key -> 식별용 컬럼(중복X)
    name = db.Column(db.String(30)) # String(길이) - 길이 있는 문자
    age = db.Column(db.Integer) # Integer -> 숫자
    address = db.Column(db.String(30))
    
class Car(db.Model) :
    no = db.Column(db.Integer, primary_key=True) 
    person_no = db.Column(db.Integer, db.ForeignKey('person.no', ondelete='CASCADE'))    
    person = db.relationship('Person', backref=db.backref('car_list'))    
    model = db.Column(db.String(30)) 
    price = db.Column(db.Integer) 
    color = db.Column(db.String(30))
    
    
# 자동차 모델을 만들고 
# 색상, 가격, 자동차모델명
# 1. 하얀색 1000만원짜리 모닝
# 2. 검정색 2000만원짜리 아반떼
# 3. 파란색 3000만원짜리 싼타페

# 위 세 자동차를 DB에 저장해주시고,
# /print_car/1 
# 자동차 출력

# 예시
# 127.0.0.1:5000/print_car/1
# 브라우저에 '하얀색 1000만원짜리 모닝' 이라고 출력

# 127.0.0.1:5000/print_car/2
# 브라우저에 '검정색 2000만원짜리 아반떼' 이라고 출력
