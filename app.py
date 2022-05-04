from website import create_app

# in __init__.py
app = create_app()

if __name__ == "__main__":
  app.run(debug=True)
