#1. Write a program that asks user to enter a city name and it should tell which country the city belongs to
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
print(india+pakistan+bangladesh)
city=input("Enter the name of city from above mentioned names :-")
if city in india:
    print(f"{city} is in India")
elif city in pakistan:
    print(f"{city} is in Pakistan")
elif city in bangladesh:
    print(f"{city} is in Bangladesh")
else:
    print(f"Sorry {city} is not mentioned in the above list")