from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
from sqlalchemy import MetaData

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

# # 사람 -> 이름, 나이, 주소

def create_app() :

    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    
    #from . import test_models
    from . import models
    
    from .views.test import test_view, person_view
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(test_view.bp)
    app.register_blueprint(person_view.bp)
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
 
    return app
