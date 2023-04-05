people = {"person1": 17, "person2": 20, "person3": 19}
for person in people:
    print("------")
    print(person)  # tieku klāt vārdam
    print(people[person])  # tieku klāt vecumam

    if people[person] >= 18:
        print(f"{person} ir pilngadīgs(-a)")
    else:
        print(f"{person} nav pilngadīgs(-a)")
