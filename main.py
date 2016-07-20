# main.py
from app import app
from models import Note
import views
import os 

port = os.getenv('PORT', '5000')
if __name__ == '__main__':
    Note.create_table(True)
    app.run(host='0.0.0.0', port=int(port))
