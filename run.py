from app import app
from app.model import Employess 

if __name__ == "__main__":
    Employess.Base.metadata.create_all(Employess.engine)
    # executa a aplicação
    app.run(debug=True)