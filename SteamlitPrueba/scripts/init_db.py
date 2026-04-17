from dotenv import load_dotenv
load_dotenv()

from scripts.database import engine, Base
from scripts import models  

if __name__ == "__main__":
    print("Creando tablas en Supabase...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas verificadas/creadas correctamente")