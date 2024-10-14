from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    @app.route('/test-db')
    def test_db_connection():
        try:
            db.session.execute('SELECT 1')
            return 'Connected to database successfully'
        except Exception as e:
            return f'Error connecting to database: {str(e)}'
        
    return app