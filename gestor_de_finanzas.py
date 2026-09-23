import json
import datetime

#------------------------------------------------------------------

#Para no borrar la informacion al crear el programa
try:
    with open('data.json', 'r') as file:
        data = json.load(file)


#por si la informacion no existe, se crea un archivo json con la informacion basica        
except FileNotFoundError:
    
    user_data = [

        #income
        [],

        #expenses
        []
    ]
    
    with open('data.json', 'w') as file:
        json.dump(user_data,file, indent = 4)

        data = user_data

#------------------------------------------------------------------

opcions = 0

while True:

    print("""


================================
    FINANCE TRACKER
================================

1. Add income
2. Add expense
3. Show total balance
4. Show Income and Expenses
5. Exit

Choose an option:""")

    opcions = int(input())
    if opcions == 1:

        category = input("Enter the category of income: ").strip()
        amount = float(input("Enter the amount of income: $"))

        data[0].append(
            {
                "date": str(datetime.date.today()),
                "category": category,
                "amount": amount
            }
        )


    if opcions == 2:

        category = input("Enter the category of expense: ").strip()
        amount = float(input("Enter the amount of expense: $"))
            
        data[1].append(
            {
                "date": str(datetime.date.today()),
                "category": category,
                "amount": amount
            }
        )

    # se guarda la informacion en un archivo json para que no se pierda al cerrar el programa
    with open('data.json', 'w') as file:
        json.dump(data,file, indent = 4)


    if opcions == 3:
        total_income = sum(i['amount'] for i in data[0])
        total_expenses = sum(j['amount'] for j in data[1])
        balance = total_income - total_expenses
        print(f"Total income: ${total_income:.2f}")
        print(f"Total expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}")


    if opcions == 4:
        print("Income and expenses: \n")
        for i in data:

            # aqui los ingresos, imprime el titulo de ingresos
            if i == data[0]:
                print("Income:")

            # al pasar los ingresos vienen los gastos, imprime el titulo de gastos
            elif i == data[1]:
                print("Expenses:")

        # recore las listas dentro de la lista "income" y "expenses" para imprimir los datos de cada uno
            for j in i:
                print(f"""
    date: {j['date']}
    category: {j['category']}
    amount: {j['amount']:.2f}
                """)

    if opcions == 5:
        print("Exiting the program...")
        break
                                # aunque opciones ya se fuerza a ser int deseo volver a verificar el dato
    if (opcions < 1 or opcions > 5) and type(opcions) is int:
        print("Invalid option, please try again.")

#------------------------------------------------------------------

print("""

The exited was successful, 
Thank you for using the program.

""")
        