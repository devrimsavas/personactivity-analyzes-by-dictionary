from dictionary_people import person_dict
import matplotlib.pyplot as plt
import numpy as np

#get keys
def get_names(dictionary):
    
    names=dictionary.keys()
    for no,name in enumerate(names):
        print(f'{no+1}- {name}')
        

#add new person

def add_new_person(dictionary):
    new_name=input('Enter the new name: ')
    
    if new_name in dictionary:
        print('This name already exists in the dictionary')
        return
    hobbies=[]
    while True:
        hobby=input(f'{new_name}: new record ( 0 to exit): ')
        if hobby in hobbies:
            print('this entry has already entered try another')
            hobby=input(f'{new_name}: new record ( 0 to exit): ')
            
        if hobby=='0':
            break
        hobbies.append(hobby)
    dictionary[new_name]=hobbies
    print(f' {new_name} has been added to the dictionary')
                           
def show_dict(dictionary):
    for no,keys in enumerate(dictionary):
        values=dictionary[keys]
        print(f'{no+1}- {keys}, {values}')

def search_person(dictionary):
    person_to_search = input('Person to search: ').strip()
    if not person_to_search:
        return

    found = False
    for person, hobbies in dictionary.items():
        if person_to_search.lower() in person.lower():
            found = True
            print(f"{person} - {hobbies}")

    if not found:
        print("Person not found.")

def search_activity(dictionary):
    activity_to_search=input('Activity to search:').strip()
    if not activity_to_search:
        return

    found=False
    for person, hobbies in dictionary.items():
        if any(activity_to_search.lower() in hobby.lower() for hobby in hobbies[1:]):
            found=True
            print(f'{person}-{hobbies} {activity_to_search}')

    if not found:
        print('activity not found')
    
        
        

def search_item(dictionary):
    search_text=input(f'Enter search text:    \n' )
    search_text_freq=0
    found=False 

    for name, values in dictionary.items():
        if any(search_text.lower()  in value.lower()for value in values[1:]):
            
            search_text_freq+=1
            print(f'{name} has: {search_text}')
            found=True
    print(f'\ntotally {search_text_freq} person has {search_text}')
    if not found:
        print(f' NOT FOUND')
        
def add_record_to_existed_person(dictionary):
    show_dict(dictionary)
    person=input('Person ?')
    male_gender='male'
    female_gender='female'
    if person not in dictionary.keys():
        print('this person is not in the dictionary. Open a new entry for this person')
        return
    while True:
        new_hobby=input('New hobby ? 0 for exit ')
        if new_hobby=='0':
            break
        if new_hobby=="":
            print('you entered empty query try again')
            new_hobby=input('New hobby ? 0 for exit ')
            
        if new_hobby not in dictionary[person]:
            dictionary[person].append(new_hobby)
        else:
            print('try another record. this is already in the list')
            
    
    
def gender_analysis(dictionary):
    population_number=len(dictionary)
    print(f'population number: {population_number}')
    total_num_males=0
    total_num_females=0
    male_word="male"
    female_word="female"

    for name,values in dictionary.items():
        if male_word in values:
            total_num_males+=1
        elif female_word in values:
            total_num_females+=1
    

    ages=[int(values[1]) for values in dictionary.values()]
    print(ages)
    total_age=sum(ages)
    min_age=min(ages)
    max_age=max(ages)
    average_age=round(total_age/population_number,3)
    median=np.median(ages)
    standard_deviation=np.std(ages)
    print(f'males: {total_num_males}\nfemales: {total_num_females}')
    print(f'minimum age: {min_age}')
    print(f'maximum age: {max_age}')
    print(f'average age: {average_age}')
    print(f'median     : {median}')
    print(f'standard deviation: {standard_deviation}')

    labels=['Males','Females']
    sizes=[total_num_males,total_num_females]
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    axs[0].axis('equal')
    axs[0].set_title('Gender Distribution')

    # plot histogram on second subplot
    axs[1].hist(ages,bins=5)
    axs[1].set_xlabel('AGE')
    axs[1].set_ylabel('FREQUENCY')
    axs[1].set_title('Age Distribution')

# adjust spacing between subplots and show the plot
    plt.subplots_adjust(wspace=0.4)
    plt.show()

   

def meta_analyzing(dictionary):
    freq_list=[]
    word_freq={}
    for values in dictionary.values():
        for value in values[2:]:
            word_freq[value]=word_freq.get(value,0)+1

    sorted_word_freq=sorted(word_freq.items(),key=lambda x: x[1],reverse=True)
            

    for word,freq in word_freq.items():
        print(f'{word}: {freq}')

    grafik=input('do you want to see it on a Pie Chart? ')

    if grafik=='y':
        fig1,ax1=plt.subplots()
        
        plt.pie(word_freq.values(),labels=word_freq.keys())
        plt.show()

    

def analyzing_activity(dictionary):
    all_activities=[]
    outside_activities=[]
    inside_activities=[]
     
                  
    
    #get list of all activities
    for values in dictionary.values():
        for value in values[2:]:
            if value not in all_activities:
                all_activities.append(value)

    for no,activity in enumerate(all_activities):
        print(f'{no}-{activity}')
        activity_type=input('is it outside or inside ? (o/i) 0 for exit')
        if activity_type=='o':
            if activity in outside_activities :
                print('already registered')
            else:
                outside_activities.append(activity)
            
        if activity_type=='i':
            if activity in  inside_activities:
                print('alread registered')
            else:
                inside_activities.append(activity)
        if activity_type=='0':
            break
        
    inside_scores = {}
    outside_scores = {}
    for person, values in dictionary.items():
        name = person
        inside_count = sum([1 for value in values[2:] if value in inside_activities])
        outside_count = sum([1 for value in values[2:] if value in outside_activities])
        inside_score = round(inside_count / len(inside_activities), 2) if inside_count != 0 else 0
        outside_score = round(outside_count / len(outside_activities), 2) if outside_count != 0 else 0
        inside_scores[name] = inside_score
        outside_scores[name] = outside_score

    get_names(dictionary)

    while True:
        person_index=int(input('Person index ?'))
        if person_index==0:
            break

    

        for key,inside_value in inside_scores.items():
            if key==list(inside_scores.keys())[person_index-1]:
                person_name=key
                person_inside_value=inside_value

        for key,outside_value in outside_scores.items():
            if key==list(outside_scores.keys())[person_index-1]:
                person_outside_value=outside_value

        print(f'person :{person_name}\inside value: {person_inside_value}\noutside value: {person_outside_value}\n')
        print(f'{dictionary[person_name]}')

    
        
        
    
menu_text="""
-----SELECT------
1- Get Names
2- Add new Person
3- Show Dictionary
4- Search in Dictionary
5- Add new object to existing People
6- Gender and Age Analyzing
7- Meta Analyzing
8- Analyzing_activity
9- Search a Person
10-Search Activity
0- Exit
------------------------
"""

while True:
    print(menu_text)
    user=input('-->>> ')

    if user=='1':
        get_names(person_dict)

    elif user=='2':
        add_new_person(person_dict)

    elif user=='3':
        show_dict(person_dict)

    elif user=='4':
        search_item(person_dict)

    elif user=='5':
        add_record_to_existed_person(person_dict)

    elif user=='6':
        gender_analysis(person_dict)

    elif user=='7':
        meta_analyzing(person_dict)
        
    elif user=='8':
        analyzing_activity(person_dict)
    
        
        

    elif user=='9':
        search_person(person_dict)


    elif user=='10':
        search_activity(person_dict)

    else:
        exit=input('you want to exit ? y/n')
        if exit=='y':
            break 
