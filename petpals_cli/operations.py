from models import Base, Shelter, Animal, Application
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

class ShelterOperations:
    def __init__(self):
        engine = create_engine('sqlite:///petpals.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    def add_animal(self, name, species, breed, age, shelter_id):
        """Add new animal record"""
        new_animal = Animal(
            name=name,
            species=species,
            breed=breed,
            age=age,
            intake_date=date.today(),
            shelter_id=shelter_id
        )
        self.session.add(new_animal)
        self.session.commit()
        return new_animal
    
    def get_animals_by_species(self, species):
        """Filter animals by species"""
        return self.session.query(Animal).filter(
            Animal.species == species
        ).all()
    
    def process_application(self, animal_id, applicant_name, contact_info):
        """Handle new adoption applications"""
        application = Application(
            applicant_name=applicant_name,
            contact_info=contact_info,
            status="Pending",
            animal_id=animal_id
        )
        self.session.add(application)
        self.session.commit()
        return application