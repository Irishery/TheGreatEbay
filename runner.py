import os
from app import create_app
from dotenv import load_dotenv
# from flask_script import Manager, Shell
# from flask_migrate import MigrateCommand

load_dotenv()

app = create_app(os.getenv('FLASK_ENV') or 'config.DevelopementConfig')
app.debug = True
# manager = Manager(app)

def make_shell_context():
    return dict(app=app)

# manager.add_command('shell', Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run(debug=True)
