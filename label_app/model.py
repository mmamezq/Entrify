from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Job(db.Model):
    """Class for jobs in the db."""

    __tablename__ = 'jobs'

    job_id = db.Column(db.BigInteger, primary_key = True, nullable = False, unique = True, autoincrement = False)
    job_title = db.Column(db.String, nullable = True)
    company_name = db.Column(db.String, nullable = True)
    li_level = db.Column(db.Integer, nullable = True)
    job_details = db.Column(db.String, nullable = True)
    label = db.Column(db.Integer, nullable = True)
    label_pattern = db.Column(db.String, nullable = True)
    matched_pattern = db.Column(db.String, nullable = True)
    uncertain = db.Column(db.Integer, nullable = True)

    def __repr__(self):
        return f'<Job {self.job_title} ID: {self.job_id}>'


def connect_to_db(app, db_name, echo = False):
    """Connect to PostgreSQL database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{db_name}'
    app.config['SQLALCHEMY_ECHO'] = echo
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)

    print(f'Connected to {db_name} db.')

    return db.engine


if __name__ == '__main__':
    from server import app
    
    connect_to_db(app, 'li-job-data', echo = True)
    db.create_all()