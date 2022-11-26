import json


def readProject():
    with open('projects.json', 'r') as file:
        data = file.read()
        print(data)


def createProject():
    id = input("Enter Project id :")
    name = input("Enter Project Name :")
    budget = input("Enter Project Budget :")
    p = {
        "id": id,
        "name": name,
        "budget": budget
    }
    with open('projects.json', "r") as file:
        data = json.load(file)

    data.append(p)

    with open('projects.json', 'w') as f:

        json.dump(data, f)
        # f.write("\n")
        f.close()
    # except Exception as e:
    # print(e)


def deleteProject():
    i = input("Please Enter id of Project :")
    if i.isdigit():
        with open('projects.json', "r") as file:
            data = json.load(file)
            for index, p in enumerate(data):
                if p['id'] == i:
                    data.pop(index)
                    print("Projects With Deleted")
                else:
                    print("There NOt project with This id")

        with open('projects.json', 'w') as f:

            json.dump(data, f)
            # f.write("\n")
            f.close()
    # except Exception as e:
    # print(e)
    else:
        print("Invalid Input Try Again")
        deleteProject()


def editProject():
    i = input("Please Enter id of Project :")
    if i.isdigit():
        with open('projects.json', "r") as file:
            data = json.load(file)
            for index, p in enumerate(data):
                if p['id'] == i:
                    p['name'] = input("Edit Project Name :")
                    p['budget'] = input("Edit Project budget :")
                else:
                    print("There NOt project with This id")

        with open('projects.json', 'w') as f:

            json.dump(data, f)
            # f.write("\n")
            f.close()
    # except Exception as e:
    # print(e)
    else:
        print("Invalid Input Try Again")
        deleteProject()


def searchProject():
    i = input("Please Enter id of Project :")
    if i.isdigit():
        with open('projects.json', "r") as file:
            data = json.load(file)
            for index, p in enumerate(data):
                if p['id'] == i:
                    print("Edit Project Name :", p['name'])
                    print("Edit Project budget :", p['budget'])
                else:
                    print("There NOt project with This id")
    else:
        print("Invalid Input")
        searchProject()


def afterLogin():
    x = input("1 -Read All Projects \n 2- Create \n 3-Edit \n 4-Delete \n 5-Search ")
    if x in ['1', '2', '3', '4', '5']:
        if x == '1':
            readProject()
            closeOrNot()
        elif x == '3':
            editProject()
            closeOrNot()
        elif x == '4':
            deleteProject()
            closeOrNot()
        elif x == '5':
            searchProject()
            closeOrNot()
        else:
            createProject()
            closeOrNot()
    else:
        print("Invalid Input")
        afterLogin()


def closeOrNot():
    x = input('Want To close :[y/n]')
    if x in ['n', 'y', 'Y', 'N']:
        if x in ['n', 'N']:
            afterLogin()
        else:
            exit()
    else:
        print("Invalid Iput")
        closeOrNot()
