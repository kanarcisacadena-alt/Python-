import requests
from sys import exit 


#----------------------------------------------------------------

def main():

    while True:
        searching = get_book()

        info = api_conection(searching)

        search(info)

        cont = input("Press \"1\" to continue. Press any other key to exit.\n").strip()

        if cont != "1":
            exit("Thanks you for using the program!!!")


#----------------------------------------------------------------


def get_book():
    searching = ""

    while not any(char.isalnum() for char in searching):
        try:
            searching = input("What book (or author) do you want to search?\n").title()
            if not any(char.isalnum() for char in searching):
                raise ValueError
        except ValueError:
            print("Invalid input, enter a book (or author) name")
        else:
            return searching
        

#----------------------------------------------------------------


def api_conection(searching):
    url = "https://openlibrary.org/search.json"

    parameters = {
        "q": searching,
        "limit": 5,
    }

    try:
        response = requests.get(url, params=parameters)
        info = response.json()
        return info 
    except requests.exceptions.RequestException:
        exit("Problems to stablish connection with the API")


#----------------------------------------------------------------


def search(info):
    try:
        if len(info["docs"]) > 0:
            print("----------------------------------------------------------------")
            for c in info["docs"]:
                    if "author_name" in c:
                        print(f"* Author: {c["author_name"][0]}")

                    if "title" in c:
                        print(f"* Title: \"{c["title"]}\"")

                    if "first_publish_year" in c:
                        print(f"* First Publish Year: {c["first_publish_year"]}")

                    if "language" in c:
                        print(f"* Language: {c["language"]}")

                    print("\n")

        else:
            raise KeyError   
        
    except KeyError:
        print("There is not that book in this library")


#----------------------------------------------------------------

if __name__ == "__main__":
    main()