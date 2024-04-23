class customer:
      def __init__(self,name,email,phone,profile,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address
        self.profile=profile
      def update_profile(self, name = None, email = None, phone = None,address = None, profile = None):
        if name:
            self.name=name
        if email:
            self.email=email
        if phone:
            self.phone=phone
        if address:
            self.address=address
        if profile: 
            self.profile=profile
      def display_profile(self):
        print("Name:",self.name)
        print("email:",self.email)
        print("phone:",self.phone)
        print("address:",self.address)
        print("profile:",self.profile)
customer2=customer("sameeksha","sameeksha.p@gmail.com", '356375767',"customer","krpuram")
customer2.display_profile()
