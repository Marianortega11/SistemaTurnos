from config import database, seed

def register(app):
    @app.cli.command("reset-db")
    def reset_db():
        database.reset()

    @app.cli.command("seed-db")
    def seed_db():
        seed.run()
        print("Base de datos sembrada")