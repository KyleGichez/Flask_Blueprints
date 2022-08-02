from app import create_app

app = create_app()
app.config.from_object("config.DevelopmentConfig")
print(app.config)

if __name__ == '__main__':
    app.run(debug = True)
