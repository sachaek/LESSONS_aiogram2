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
    price=5,
    photo_link="https://hips.hearstapps.com/hmg-prod/images/2020-porsche-taycan-4s-vs-2020-tesla-model-s-long-range-202-1621386342.jpg?crop=0.842xw:0.711xh;0,0.161xh&resize=1200:*")


Tesla_X = Item(
    id=2,
    title="Tesla X",
    description="""The Tesla Model X is an electric SUV that offers exceptional power and versatility. Its all-wheel 
    drive system provides unmatched traction and acceleration, and it has a range of up to 371 miles on a single 
    charge. The Model X is equipped with advanced technology such as Tesla's Autopilot system, which includes 
    features like adaptive cruise control and automatic emergency braking. The Falcon Wing doors are a unique and 
    practical feature that make getting in and out of the vehicle a breeze.""",
    price=5,
    photo_link="https://hips.hearstapps.com/hmg-prod/images/2020-porsche-taycan-4s-vs-2020-tesla-model-s-long-range-202-1621386342.jpg?crop=0.842xw:0.711xh;0,0.161xh&resize=1200:*")

Iphone_XS = Item(
    id=3,
    title="Iphone XS",
    description="""The iPhone is Apple's flagship smartphone that combines sleek design with powerful features. Its 
    advanced camera system and high-resolution display make it the perfect device for capturing and viewing photos 
    and videos.""",
    price=5,
    photo_link="https://hips.hearstapps.com/hmg-prod/images/2020-porsche-taycan-4s-vs-2020-tesla-model-s-long-range-202-1621386342.jpg?crop=0.842xw:0.711xh;0,0.161xh&resize=1200:*"
)

items = [Tesla_S, Tesla_X, Iphone_XS]