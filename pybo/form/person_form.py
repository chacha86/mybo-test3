from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class PersonForm(FlaskForm):
    name = StringField('이름', validators=[DataRequired("이름은 필수 입력사항입니다.")])
    age = StringField('나이', validators=[DataRequired("나이는 필수 입력사항입니다.")])
    address = StringField('주소', validators=[DataRequired("주소는 필수 입력사항입니다.")])
    # StringFiled => input type="text"
    # TxetAreaFiled => <textarea></textarea>