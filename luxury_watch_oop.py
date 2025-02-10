class LuxuryWatch:
    __watches_created = 0
    __watch_lst = []
    def __init__(self, brand: str):
        self.brand = brand
        LuxuryWatch.__watches_created += 1

    def __str__(self) -> str:
        return f"Brand: {self.brand}"

    @classmethod #Alternative constructor to add an engraving.
    def alt_constructor(cls, brand: str, engrave: str):
        _watch = cls(brand)
        _watch.engrave = engrave
        return _watch
    
    @classmethod
    def get_number_of_watches_created(cls):
        if cls.__watches_created == 1:
            print(f"There is {cls.__watches_created} watch created.")
        elif cls.__watches_created > 1:
            print(f"There are {cls.__watches_created} watches created.")
        else:
            print(f"No watches created yet.")

    @classmethod
    def add_to_watch_lst(cls, new_watch):
        cls.__watch_lst.append(new_watch)
        print("Watch successfully added.")

    @classmethod
    def get_watch_lst(cls):
        for i, j in enumerate(cls.__watch_lst):
            print(i + 1, j)

    @staticmethod
    def validate_engrave(engrave: str) -> bool:
        return len(engrave) <= 40 and engrave.isalnum()

    @staticmethod
    def valid_brand(brand: str) -> bool:
        if brand.capitalize() in ('Rolex', 'Casio', 'Tommy', 'Fossil'):
            return True
        else:
            return False
        
print("Welcome to our Luxury watch store.")
while True:
    inpt_brand = input("Type the brand of the watch: ")
    if LuxuryWatch.valid_brand(inpt_brand):
        if input("Do you want to add an engraving? Type y or yes to accept / anything to skip this step. ").lower() in ('yes', 'y'):
            engraving = input("Type the engraving for your watch: ")
            if LuxuryWatch.validate_engrave(engraving):
                print(f"Adding your {inpt_brand} watch with the engraving {engraving}.")
                LuxuryWatch.add_to_watch_lst(LuxuryWatch.alt_constructor(inpt_brand, engraving))
            else:
                print("The engraving can't have +40 characters and must only have letters and numbers.")
                print(f"Adding your {inpt_brand} watch without an engraving.")
                LuxuryWatch.add_to_watch_lst(LuxuryWatch(inpt_brand))
        else:
            print(f"Adding your {inpt_brand} watch.")
            LuxuryWatch.add_to_watch_lst(LuxuryWatch(inpt_brand))
    else:
        print("That brand is not available.")
    if input("Do you want to check another brand? Type n or no to exit / anything to continue. ").lower() in ('no', 'n'):
        print("Thanks for shopping with us.")
        LuxuryWatch.get_number_of_watches_created()
        LuxuryWatch.get_watch_lst()
        break
    else:
        LuxuryWatch.get_number_of_watches_created()
        LuxuryWatch.get_watch_lst()