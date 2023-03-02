from dataclasses import dataclass


@dataclass
class Item:
    id: int
    title: str
    description: str
    price: int
    photo_link: str


Tesla_S = Item(
    id=1,
    title="Tesla S",
    description="""The Tesla Model S is a premium electric sedan that combines sleek design with exceptional 
    performance. Its all-electric powertrain provides instantaneous acceleration and a range of up to 402 miles on a 
    single charge. The Model S is equipped with advanced technology such as a 17-inch touchscreen display, 
    over-the-air software updates, and Tesla's Autopilot system, which includes features like automatic lane changing 
    and self-parking.""",
    price=1,
    photo_link="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Tesla_Model_S_logo.svg/1200px-Tesla_Model_S_logo.svg.png")


Tesla_X = Item(
    id=2,
    title="Tesla X",
    description="""The Tesla Model X is an electric SUV that offers exceptional power and versatility. Its all-wheel 
    drive system provides unmatched traction and acceleration, and it has a range of up to 371 miles on a single 
    charge. The Model X is equipped with advanced technology such as Tesla's Autopilot system, which includes 
    features like adaptive cruise control and automatic emergency braking. The Falcon Wing doors are a unique and 
    practical feature that make getting in and out of the vehicle a breeze.""",
    price=80_000_000,
    photo_link="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Tesla_Model_X_logo.svg/1200px-Tesla_Model_X_logo.svg.png")

Iphone_XS = Item(
    id=3,
    title="Iphone XS",
    description="""The iPhone is Apple's flagship smartphone that combines sleek design with powerful features. Its 
    advanced camera system and high-resolution display make it the perfect device for capturing and viewing photos 
    and videos.""",
    price=5_000,
    photo_link="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Iphone_XS_logo.svg/1200px-Iphone_XS_logo.svg.png"
)

