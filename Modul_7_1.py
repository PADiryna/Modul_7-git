from faker import Faker
f = Faker()


class BaseContact:
    def __init__(self, name, surname, phone_number_priv, email):
        self.name = name
        self.surname = surname
        self.phone_number_priv = phone_number_priv
        self.email = email

      
    def __str__(self):
        return f'{self.name} {self.surname} {self.phone_number_priv} {self.email}'
      
    def contact(self):
        return "I dial the phone number {} and call {} {}".format(self.phone_number_priv, self.name, self.surname) 
      
    @property
    def label_length(self):
      return len(self.name + " " + self.surname)
     
    def __lt__(self, other):
      if select == 1:
        return self.name < other.name
      elif select == 2:
        return self.surname < other.surname

class BusinessContact(BaseContact):
    def __init__(self, post, company, phone_number_company,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.post = post
        self.company = company
        self.phone_number_company = phone_number_company

    def __str__(self):
        return f'{self.name} {self.surname} {self.phone_number_priv} {self.email} {self.post} {self.company} {self.phone_number_company}'  

    def contact(self):
        return "I dial the phone number {} and call {} {}".format(self.phone_number_company, self.name, self.surname)

        

def create_contacts(card_type, number):

    contacts = []
      
    for i in range(number):
        if card_type == 1:
            contact = BaseContact(
              name = f.first_name(),
              surname = f.last_name(),
              phone_number_priv = f.phone_number(),
              email = f.email()
            )
            contacts.append(contact)
        elif card_type == 2:
            contact = BusinessContact(
              name = f.first_name(),
              surname = f.last_name(),
              phone_number_priv = f.phone_number(),
              email = f.email(),
              post = f.job(),
              company = f.company(),
              phone_number_company = f.phone_number()
            )
            contacts.append(contact)
          
    return contacts   
  

if __name__ == "__main__":   
    
    card_type = int(input("Enter a card type. Priv - 1, business - 2: "))
    number = int(input("Enter a number of cards: "))
    select = int(input("Enter a type of sort. Name - 1, surname - 2: "))
    contacts = create_contacts(card_type, number)
   
    for contact in sorted(contacts):
        print(contact)
      
    action = input("Enter name to whom would you like to call: ")
   
   