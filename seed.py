from app import db
from models import Pet

db.drop_all()
db.create_all()

tux = Pet(
    name="Tux",
    species="Dog",
    photo_url="https://pet-uploads.adoptapet.com/d/4/b/311292963.jpg",
    age=6,
    notes="Meet Stu! He's a great dog with a big heart and whose favorite things to do is cuddle and receive belly rubs. He can be playful too so a fenced yard would be a plus but is not required, with a couple quick walks each day he does just fine",
)
steele = Pet(
    name="Steele",
    species="Dog",
    photo_url="https://pet-uploads.adoptapet.com/b/0/7/290194043.jpg",
    age=4,
    notes="Steele is a shy, 4year old pitbull mix who loves kids and just lounging around the house snuggling. He is also crate trained and enjoys some alone time. Steele needs a home with no other pets",
)
fifi = Pet(
    name="Fifi",
    species="Dog",
    photo_url="https://pet-uploads.adoptapet.com/1/a/d/511099304.jpg",
    age=1,
    notes="Shy yet charming canine searching for patient owner with relaxed lifestyle. Looking for gentle guidance to help me come out of my shell. Treat me sweet and kind and I'll blossom.",
)
brutus = Pet(
    name="Brutus",
    species="Dog",
    photo_url="https://pet-uploads.adoptapet.com/f/2/5/511366527.jpeg",
    age=2,
    notes="Hello, My name is Brutus and I am a big lover of Buckeye football.... OH - IO!! I came to CHA from a rural overcrowded shelter.",
)

db.session.add(tux)
db.session.add(steele)
db.session.add(fifi)
db.session.add(brutus)


db.session.commit()
