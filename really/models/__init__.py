from really import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    fullname = db.Column(db.String(50))

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    alias = db.Column(db.String(10))

class Issue(db.Model):
    __tablename__ = 'issues'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('bug', 'task', 'feature','story', 'epic'))
    summary = db.Column(db.String(200))
    priority = db.Column(db.Enum('blocker', 'critical', 'minor','trivial'))
    description = db.Column(db.String(200))
    due_date = db.Column(db.DateTime)

    parent_id = db.Column(db.Integer, db.ForeignKey('issues.id'))
    children = db.relationship('Issue', cascade="all, delete-orphan",
                               backref=db.backref('parent', remote_side=[id]))

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship("Project", backref="issues")
