from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import GameCompany, Base, GameConsole, User

engine = create_engine('sqlite:///dbconsolecatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# method to add console and commit it to the table
def add_game_console(companyconsole):
    session.add(companyconsole)
    session.commit()

# Create player
player = User(name = 'player', email = 'player@player.com')
add_game_console(player)


# Create some companies
sony = GameCompany(name = 'Sony', user_id= 1)
add_game_console(sony)

microsoft = GameCompany(name = 'Microsoft', user_id= 1)
add_game_console(microsoft)

nintendo = GameCompany(name = 'Nintendo', user_id= 1)
add_game_console(nintendo)

pc = GameCompany(name = 'PC', user_id= 1)
add_game_console(pc)


# Add consoles to the companies
gameconsole = GameConsole(name = "Playstation 4", description = "Sony's latest console", price = "$299.99", gamecompany_id = 1, user_id=1)
add_game_console(gameconsole)

gameconsole = GameConsole(name = "Playstation 3", description = "Sony's most renovating console", price = "$250", gamecompany_id = 1, user_id=1)
add_game_console(gameconsole)

gameconsole = GameConsole(name = "PSP", description = "Sony's handheld console", price = "$200", gamecompany_id = 1, user_id=1)
add_game_console(gameconsole)

gameconsole = GameConsole(name = "Playstation 2", description = "Sony's highest sold console", price = "$200", gamecompany_id = 1, user_id=1)
add_game_console(gameconsole)

gameconsole = GameConsole(name = "Xbox One S", description = "Microsoft's latest console", price = "$279.99", gamecompany_id = 2, user_id=1)
add_game_console(gameconsole)

gameconsole = GameConsole(name = "Xbox One", description = "Microsoft's renovating console", price = "$250", gamecompany_id = 2, user_id=1)
add_game_console(gameconsole)

gameconsole = GameConsole(name = "Xbox 360", description = "Microsoft's highest sold console", price = "$199.99", gamecompany_id = 2, user_id=1)
add_game_console(gameconsole)

gameconsole = GameConsole(name = "Xbox", description = "Microsoft's debuting console", price = "$149.99", gamecompany_id = 2, user_id=1)
add_game_console(gameconsole)

gameconsole = GameConsole(name = "Switch", description = "Nintendo's latest console", price = "$299.99", gamecompany_id = 3, user_id=1)
add_game_console(gameconsole)

gameconsole = GameConsole(name = "3DS", description = "Nintendo's highest sold collection console", price = "$199.99", gamecompany_id = 3, user_id=1)
add_game_console(gameconsole)

gameconsole = GameConsole(name = "NES", description = "Nintendo's oldest console", price = "$99.95", gamecompany_id = 3, user_id=1)
add_game_console(gameconsole)

gameconsole = GameConsole(name = "Gamecube", description = "Nintendo's renovating console", price = "$149.99", gamecompany_id = 3, user_id=1)
add_game_console(gameconsole)

gameconsole = GameConsole(name = "Steam", description = "PC console", price = "$79.99", gamecompany_id = 4, user_id=1)
add_game_console(gameconsole)

print("added gaming consoles!")