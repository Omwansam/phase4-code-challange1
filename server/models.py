from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Hero(db.Model):
    __tablename__ = 'heroes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

# Relationship mapping the  heroes to the heroes power
    hero_powers = db.relationship('HeroPower', back_populates='hero',cascade="all,delete-orphan")    


#def to_dict(self):
#        return {
#           'id': self.id,
#          'name': self.name,
#            'super_name': self.super_name,
#        }
def __repr__(self):
        return f"<Hero(id={self.id}, name='{self.name}', super_name='{self.super_name}')>"

class Power(db.Model):
    __tablename__ = 'powers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='power',cascade="all,delete-orphan")  

@validates('description')
def validate_description(self, key, description):
    if not description:
        raise ValueError("Description is required.")
    if len(description) < 20:
        raise ValueError("Description must be at least 20 characters long.")
    return description


def __repr__(self):
    return f"<Power(id={self.id}, name='{self.name}', description='{self.description}')>"   


# Association table or the join table 
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)


# Foreign key to sore the hero id
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
#Foreign key to store power id
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

# Relationship to Hero (many to many)
    hero =db.relationship('Hero', back_populates='hero_powers')
# relationships to power (many to many)
    power = db.relationship('Power', back_populates='hero_powers')

    # Validation for strength field
    @validates('strength')
    def validate_strength(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be one of 'Strong', 'Weak', or 'Average'.")
        return strength

def __repr__(self):
    return f"<HeroPower(id={self.id}, strength='{self.strength}', hero_id={self.hero_id}, power_id={self.power_id})>"

# Create tables    




    

