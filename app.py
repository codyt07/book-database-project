from models import (Base, session, 
                    Book, engine)
# main menu - add, search, analysis, exit, view
# add books to database
# edit books
# Detel books
# search function
# data cleaning
# loop runs program


if __name__ == "__main__":
    Base.metadata.create_all(engine)