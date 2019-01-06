import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Sport, CatalogItem

engine = create_engine('sqlite:///sportcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# sport 1
sport1 = Sport(name="Soccer")
session.add(sport1)
session.commit()

catalogItem1 = CatalogItem(name="Shinguards", description="Gear that protects
                           the shins", sport=sport1)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name="Jersey", description="A shirt that matches the
                           team.", sport=sport1)
session.add(catalogItem2)
session.commit()

# sport 2
sport2 = Sport(name="Basketball")
session.add(sport2)
session.commit()

catalogItem1 = CatalogItem(name="Basketball", description="A ball that is used
                           to throw into the basketball hoop.", sport=sport2)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name="Jersey", description="A shirt that matches the
                           team.", sport=sport2)
session.add(catalogItem2)
session.commit()

# sport 3
sport3 = Sport(name="Baseball")
session.add(sport3)
session.commit()

catalogItem1 = CatalogItem(name="Bat", description="A long object that is used
                           to swing at a baseball.", sport=sport3)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name="Baseball", description="A ball that is
                           hit with a baseball bat.", sport=sport3)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name="Mit", description="An oversized glove made of
                           leather. The mitt is used to protect the hand and
                           catch the ball. ", sport=sport3)
session.add(catalogItem3)
session.commit()

# sport 4
sport4 = Sport(name="Frisbee")
session.add(sport4)
session.commit()

catalogItem1 = CatalogItem(name="Frisbee", description="Wide range of flying
                           disc variants are available.", sport=sport4)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name="Jersey", description="A shirt that matches the
                           team.", sport=sport4)
session.add(catalogItem2)
session.commit()

# sport 5
sport5 = Sport(name="Snowboarding")
session.add(sport5)
session.commit()

catalogItem1 = CatalogItem(name="Goggles", description="Mask for covering the
                           eyes as protection from snow.", sport=sport5)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name="Snowboard", description="Best for any terrain"
                           "and conditions. All-mountain snowboards perform "
                           "anywhere on a mountain -- groomed runs, "
                           "backcountry, even park and pipe. They may be "
                           "directional (meaning downhill only) or twin-tip "
                           "(for riding switch, meaning either direction). "
                           "Most boarders ride all-mountain boards. Because "
                           "of their versatility, all-mountain boards are "
                           "good  for beginners who are still learning "
                           "terrain they like.", sport=sport5)
session.add(catalogItem2)
session.commit()

# sport 6
sport6 = Sport(name="Rock Climbing")
session.add(sport6)
session.commit()

catalogItem1 = CatalogItem(name="Rope", description="Thick rope to go through
                           the harness and the top of the rock or belay wall.",
                           sport=sport6)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name="Harness", description="Set of straps that are
                           adjustable. The straps go through both legs and sit
                           at your hips. The rope goes through the front circle
                           loop.", sport=sport6)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name="Rock Climbing Shoes", description="Shoes with
                           grip on the bottom to help you grab onto the wall.",
                           sport=sport6)
session.add(catalogItem3)
session.commit()

# sport 7
sport7 = Sport(name="Foosball")
session.add(sport7)
session.commit()

catalogItem1 = CatalogItem(name="Foosball Table", description="A table with 4
                           sticks attached with figurines on both side. The
                           table allows the players to turn the handles and try
                           to score a goal with the ball in the center.",
                           sport=sport7)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name="Foosball", description="A small ball that is
                           used during a game of foosball.", sport=sport7)
session.add(catalogItem2)
session.commit()

# sport 8
sport8 = Sport(name="Skating")
session.add(sport8)
session.commit()

catalogItem1 = CatalogItem(name="Skates", description="Shoes with blades on the
                           bottom. Most often, the shoes come with laces that
                           need to be criss-crossed before tying the laces.
                           After heavy use on the ice, the blades on the shoes
                           will need to be sharpen.", sport=sport8)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name="Jersey", description="A shirt that matches the
                           team.", sport=sport8)
session.add(catalogItem2)
session.commit()

# sport 9
sport9 = Sport(name="Hockey")
session.add(sport9)
session.commit()

catalogItem1 = CatalogItem(name="Stick", description="Stick held into the hands
                           when skating on ice.", sport=sport9)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name="Jersey", description="A shirt that matches the
                           team.", sport=sport9)
session.add(catalogItem2)
session.commit()

print "added catalog items!"
