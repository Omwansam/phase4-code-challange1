from flask import Flask, jsonify , make_response, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)

# Configure the database connection

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)

# Defining routes
@app.route('/')
def index():
    return "Index for User/Power/HeroPower API"

# Route to return heroes

@app.route('/heroes', methods=['GET'])
def get_heroes():

    heroes =[]
    for hero in Hero.query.all():
        hero_dict = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        }
        heroes.append(hero_dict)

    response = make_response(
        jsonify(heroes),
        200
    )  

    return response

# Route to return heroes with id 
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):   
    hero = Hero.query.filter(Hero.id == id).first()
    

    # If the hero does not exist, return a 404 error
    if not hero:
        return make_response(
            jsonify({"error": f"Hero with id {id} not found"}),
            404
        )


    hero_powers = []
    for hero_power in hero.hero_powers:
        
        power_dict = {
            "hero_id": hero_power.hero_id,
            "id": hero_power.id,  
            "power": {
                "description": hero_power.power.description,
                "id": hero_power.power.id,  # Unique ID for the Power
                "name": hero_power.power.name
            },
            "power_id": hero_power.power_id,  # Not unique, references the Power
            "strength": hero_power.strength
        }
        hero_powers.append(power_dict)

    # Construct the response dictionary for the hero
    hero_dict = {
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": hero_powers
    }

    # Return the hero details in the expected format
    response = make_response(
        jsonify(hero_dict),
        200
    )

    return response
# Route to return power

@app.route('/powers' , methods=['GET'])

def get_powers():

    powers = []
    for power in Power.query.all():
        power_dict = {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        powers.append(power_dict)

    response =make_response(
        jsonify(powers),
        200
    )    

    return response

# Route to return power by id 

@app.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.filter(Power.id == id).first()

    if power:
        power_dict = {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        response = make_response(
            jsonify(power_dict),
            200
        )
    else:
        response = make_response(
            jsonify({"error": "Power not found"}),
            404
        )

    return response    

@app.route('/hero_powers', methods=['POST'])

def create_hero_power():
    data = request.get_json()
    # Validate the hero_id and power_id (ensure they exist)
    
    
    strength = data.get("strength")
    hero_id = data.get("hero_id")
    power_id = data.get("power_id")
    
    if not strength or not hero_id or not power_id:
        return make_response(
            jsonify({"errors": ["validation errors"]}),
            400
        )
    hero = Hero.query.filter(Hero.id == hero_id).first()
    power = Power.query.filter(Power.id == power_id).first()
    if not hero  or not power:
        return make_response(
            jsonify({"errors": ["Hero not found"]}),
            404
        )
    hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)


    try:
        db.session.add(hero_power)
        db.session.commit()

        power_dict = {
            "id": hero_power.id,
            "hero_id": hero_power.hero_id,
            "power_id": hero_power.power_id,
            "strength": hero_power.strength,
            "hero": {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            },
            "power": {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
        }
        response = make_response(
            jsonify(power_dict),
            201
        )

    except Exception as e:
        
        db.session.rollback() 
        return make_response(
            jsonify({"errors": ["validation errors"]}),
            400
        )   






















@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.filter(Power.id == id).first()

    if not power:
        return make_response(
            jsonify({"error": "Power not found"}),
            404
        )

    data = request.get_json()

    # Validate the description (ensure it's provided and non-empty)
    new_description = data.get("description", "").strip()
    if not new_description:
        return make_response(
            jsonify({"errors": ["validation errors"]}),
            400
        )

    # Optionally update name if it's provided, otherwise retain the existing name
    new_name = data.get("name")
    if new_name is not None:  
        power.name = new_name  # Update the name

    power.description = new_description  

    try:
        # Commit the changes to the database
        db.session.commit()

        # Return the updated power details in the expected format
        power_dict = {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }


        return make_response(
            jsonify(power_dict),
            200
        )

    except Exception as e:

        db.session.rollback()  
        return make_response(
            jsonify({"errors": ["validation errors"]}),
            400
        )








if __name__ == "__main__":
    app.run(port=5555, debug=True)