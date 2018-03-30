from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = create_engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

category1 = Category(name = 'Soccer')

session.add(category1)
session.commit()

# categoryItem1 = CategoryItem(name = 'Soccer Cleats', description = 'An item of footwear worn when playing soccer, designed for grass fields with studs on the outsole to aid grip.', category = category1)

# session.add(categoryItem1)
# session.commit()
#
# categoryItem2 = CategoryItem(name = 'Shin Guards', description = 'Sock inserts to protect the shins from stray kicks', category = category1)
#
# session.add(categoryItem2)
# session.commit()

category2 = Category(name = 'Baseball')

session.add(category2)
session.commit()

# categoryItem1 = CategoryItem(name = 'Bat', description = 'Made of wood or aluminum. Used by the batter/hitter to hit the baseball.', category = category2)
#
# session.add(categoryItem1)
# session.commit()
#
# categoryItem2 = CategoryItem(name = 'Helmet', description = 'Protects the hitter from stray pitches.', category = category2)
#
# session.add(categoryItem2)
# session.commit()

category3 = Category(name = 'Basketball')

session.add(category3)
session.commit()

# categoryItem1 = CategoryItem(name = 'Sneakers', description = 'Ideal show for basketball. Gives the player optimal grip on wood and concrete courts.', category = category3)
#
# session.add(categoryItem1)
# session.commit()
#
# categoryItem2 = CategoryItem(name = 'Jersey', description = "Light, breathable material, usually representative of the player's team.", category = category2)

# session.add(categoryItem2)
# session.commit()

category4 = Category(name = 'Frisbee')

session.add(category4)
session.commit()

# categoryItem1 = CategoryItem(name = 'Frisbee', description = 'Plastic disc used to play Frisbee. When thrown properly it can soar long distances.', category = category4)
#
# session.add(categoryItem1)
# session.commit()

category5 = Category(name = 'Snowboarding')

session.add(category5)
session.commit()

# categoryItem1 = CategoryItem(name = 'Snowboard', description = 'Best for any terrain and conditions. All-mountain snowboards perform anywhere on a mountain, groomed runs, back country, even park and pipe. They may be directional (meaning downhill only) or twin-tip (for riding switch, meaning either direction). Most boarders ride all-mountain boards. Because of their versatility, ', category = category5)
#
# session.add(categoryItem1)
# session.commit()

category6 = Category(name = 'Rock Climbing')

session.add(category6)
session.commit()

category7 = Category(name = 'Hockey')

session.add(category7)
session.commit()

category8 = Category(name = 'Skating')

session.add(category8)
session.commit()

category9 = Category(name = 'Foosball')

session.add(category9)
session.commit()
