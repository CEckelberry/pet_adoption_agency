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

katniss = Pet(
    name="Katniss",
    species="Cat",
    photo_url="https://pet-uploads.adoptapet.com/b/0/d/512306984.jpeg",
    age=8,
    notes="Hello, my name is Katniss and I came to CHA when my owners could no longer care for me. I am a sweet girl who likes to watch all around me while the other kitties play. I am a bit timid, but once I get to know you I love getting plenty of attention from you. I spend my days exploring my surroundings as well as finding the perfect spot to window watch. Come in and meet me today.",
)

jewel = Pet(
    name="Jewel",
    species="Horse",
    photo_url="https://s3.amazonaws.com/filestore.rescuegroups.org/6685/pictures/animals/9390/9390089/55740860_500x500.jpg",
    age=13,
    notes="Jewel is definitely one of the most beautiful girls in the 'neigh'borhood. Her breeding is Arabian and Saddlebred, which not only makes her extra fancy, but also extremely sensitive. She's so sensitive, in fact, that she needed to come to Best Friends for some specialized training as she had gotten dangerous for her (very experienced) owner to handle. She's made huge strides but will always be the type of horse who needs to be handled by someone with horse skills well above what most horse owners ever achieve.",
)

speedy = Pet(
    name="Speedy",
    species="Donkey",
    photo_url="https://s3.amazonaws.com/filestore.rescuegroups.org/6685/pictures/animals/9385/9385286/71755566_385x385.jpg",
    age=21,
    notes="Speedy is a wonderful donkey who was born in approximately 1997. He loves people and is very cuddly, with the cutest velvet donkey lips and magnificent ears. He was a breeding jack for most of his life and is quite opinionated about who he loves (anyone with long ears!) and where he wants to go, but we're working on his manners and we really enjoy being with him. (He was gelded upon arrival at the Sanctuary.) Speedy lives with another horse and they play all day long",
)

pixie = Pet(
    name="Pixie",
    species="Cat",
    photo_url="https://pet-uploads.adoptapet.com/d/2/4/512309212.jpeg",
    age=1,
    notes="Pixie is a tiny little cute kitty that loves to play with others and toys alike. Very easy going and has a cute pur.",
)

chuck = Pet(
    name="Chuck",
    species="Horse",
    photo_url="https://s3.amazonaws.com/filestore.rescuegroups.org/6685/pictures/animals/10672/10672464/65650947_385x385.jpg",
    age=9,
    notes="Chuck is a handsome dun Mustang born in approximately 2003. He was found running loose as an 8 year old stallion on the highway in the desert along the Arizona/Utah border, and eventually made his way to the Sanctuary (where he was promptly gelded). He was extremely skeptical of people (more so than the usual feral horse), but he has come a long way and has turned into a pretty wonderful fellow. We rode him for a while, and he was a great trail horse, but he has had several recurring soundness issues, so we've decided not to adopt him as a rideable horse. ",
)

mabel = Pet(
    name="Mabel",
    species="Cat",
    photo_url="https://pet-uploads.adoptapet.com/1/8/4/512301502.jpeg",
    age=4,
    notes="Hello, my name is Mabel. I came to CHA when my owner could no longer care for me. I am a sweet 5-year-old girl that loves getting attention from you. When I'm not getting pets and kisses I spend my day in a comfy spot watching all the commotion on the floor below.",
)


db.session.add(tux)
db.session.add(steele)
db.session.add(fifi)
db.session.add(brutus)
db.session.add(katniss)
db.session.add(jewel)
db.session.add(speedy)
db.session.add(pixie)
db.session.add(chuck)
db.session.add(mabel)


db.session.commit()
