DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    
    # Using List Comprehension
    all_python_devs = [worker['name'] for worker in DATA if worker['language']=='python']

    # Using filter-map and lamda funtion
    # all_python_devs = list(filter(lambda worker:worker["language"]=="python",DATA))
    # all_python_devs= list(map(lambda worker:worker["name"] , all_python_devs))

    # Using List Comprehension
    # all_platzi_workers= [worker['name'] for worker in DATA if worker['organization']=='Platzi']

    # Using filter-map and lamda funtion
    # all_platzi_workers = list(filter(lambda worker: worker["organization"]=="Platzi",DATA))
    # all_platzi_workers= list(map(lambda worker: worker["name"], all_platzi_workers))

    # Using filter-map and lamda funtion
    # adults = list(map(lambda worker:worker['name'],adults))
    # adults = list(filter(lambda worker : worker['age']>18  , DATA))

    # Using List Comprehension
    # adults = [worker["name"] for worker in DATA if worker["age"]>18]

    # Using filter-map and lamda funtion
    # olds = list(map(lambda worker : worker | {"old":worker['age']>70},DATA)) # | simbolo pipe (agrega un dicccionario mas). Solo funciona con Python 3.9 o superior

    # Using List Comprehension
    # olds = [worker | {"old":worker["age"]>70} for worker in DATA]



    for worker in all_python_devs:
        print(worker)
    
    # for worker in all_platzi_workers:
    #     print(worker)

    # for worker in adults:
    #     print(worker)

    # for worker in olds:
    #     print(worker)




if __name__=="__main__":
    run()