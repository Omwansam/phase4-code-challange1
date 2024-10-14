from app import app
import random
from models import db, Hero, HeroPower, Power


with app.app_context():
    #Delete all rows in tables

        print("Clearing db...")
        db.session.query(HeroPower).delete()  # Delete relationships first
        db.session.query(Power).delete()
        db.session.query(Hero).delete()
        db.session.commit() 

        print("Seeding powers...")
        powers = [
            Power(name="super strength", description="gives the wielder super-human strengths"),
            Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
            Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
            Power(name="elasticity", description="can stretch the human body to extreme lengths"),
        ]

        db.session.add_all(powers)
        db.session.commit()

        print("Seeding heroes...")
        heroes = [
            Hero(name="Kamala Khan", super_name="Ms. Marvel"),
            Hero(name="Doreen Green", super_name="Squirrel Girl"),
            Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
            Hero(name="Janet Van Dyne", super_name="The Wasp"),
            Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
            Hero(name="Carol Danvers", super_name="Captain Marvel"),
            Hero(name="Jean Grey", super_name="Dark Phoenix"),
            Hero(name="Ororo Munroe", super_name="Storm"),
            Hero(name="Kitty Pryde", super_name="Shadowcat"),
            Hero(name="Elektra Natchios", super_name="Elektra"),
        ]

        db.session.add_all(heroes)
        db.session.commit()

        print("Adding powers to heroes...")
        strengths = ["Strong", "Weak", "Average"]
        hero_powers = []
        for hero in heroes:
            # Randomly select a power for each hero
            power = random.choice(powers)
            hero_power = HeroPower(hero=hero, power=power, strength=random.choice(strengths))
            hero_powers.append(hero_power)
        
        db.session.add_all(hero_powers)
        db.session.commit()


        print("Done seeding!")
    
