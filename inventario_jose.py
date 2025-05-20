Inventary = {1: {'Product': 'sal', 'Price': 3.000, 'Quantity': 3},
             2: {'Product': 'pan', 'Price': 3.000, 'Quantity': 3},
             3: {'Product': 'leche', 'Price': 3.000, 'Quantity': 3},
             4: {'Product': 'azucar', 'Price': 3.000, 'Quantity': 3},
             5: {'Product': 'panela', 'Price': 3.000, 'Quantity': 3}
}
Id = 5

#List inventary
def List():
    print("\033[34m\nInventary: ")
    print(f"\033[0m\n{Inventary}")

#Add product
def Add():
    global Id
    while True:
        
        print("\033[34m\n----- Add product -----")
        Id +=1
        
        while True:    
            Product = input("\033[0m\nEnter a product: ")
            if Product.isalpha():
                exist = any(Product.lower() == dat["Product"] for dat in Inventary.values())
                if not exist:
                    break
                else:
                    print("\033[93m\n### Prodct exist, enter an not exist ###")
            else:
                print("\033[91m\n### Enter only letters ###")
                
        
        while True:
            Price = input("\033[0m\nEnter a price: ")
            if Price.replace(".", "").isdigit():
                Price = float(Price) 
                break
            else:
                print("\033[91m\n### Enter only positive numbers ###")
                
        while True:
            Quantity = input("\033[0m\nEnter a quality: ")
            if Quantity.isdigit():
                break
            else:
                print("\033[91m\n### Enter only numbers ###")
        
        Dat = {"Product" : Product, "Price" : Price, "Quantity" : Quantity}
        Inventary[Id] = Dat
        
        option = input("\033[93m\nDesea agregar otro poducto? (1. Yes ó 2. No): ").strip()   
        if option.isdigit():    
            option = int(option)
            if option == 2:
                print("\033[92m\nSuccessfull")
                break
            else:
                print("\033[92m\nSuccessfull")
        else:
            print("\033[91m\n## Enter only numbers ##")
    
#Search product
def Search():
    while True:
        print("\033[34m\n----- Search product -----")
        product = input("\033[0m\nEnter product search: ").strip().lower()
        if product.lower().isalpha():
            for Id, dat in Inventary.items():
                if dat["Product"] == product:
                    print("\033[92m\nProduct found: ")
                    print(f"\033[0m\n{Id, dat}")
                    return
            else:
                print("\033[91m\n### Product no exist ###")
        else:
            print("\033[91m\n### Enter only letter ###")
            
#Update product
def Update():
    while True:
        print("\033[34m\n----- Update price -----")
        act = input("\033[0m\nEnter a product for update price: ")  
        if act.isalpha():    
            for Id, data in Inventary.items():    
                if data["Product"] == act:   
                    while True:
                        valor = input("\033[0m\nEnter new value: ")   
                        if valor.replace('.', '').isdigit():    
                            valor = float(valor)
                            data["Price"] = valor     
                            print("\033[92m\nUpdate price:")
                            print(f"\033[0m\n{Id, data}")
                            return
                        else:
                            print("\033[91m\n## Enter only positive numbers ##")    
            else:
                print("\033[91m\n## Product no exist ##")
        else:
            print("\033[91m\n## Enter only letter ##")
            
#Delete product
def Delete():
    while True:
        print("\033[34m\n----- Delete Product -----")
        dele = input("\033[0m\nEnter a product for delete: ")    
        if dele.isalpha():    
            for Id, dat in list(Inventary.items()):    
                if dat["Product"] == dele:
                    del(Inventary[Id])
                    print("\033[92m\nSuccessfully removed")
                    return
            else:
                print("\n### Product no exist ###") 
                
#Total inventary
def Values():
    total_value = 0
    for dat in Inventary.values():  
        try:
            total_value += float(dat["Price"]) * int(dat["Quantity"])
        except (ValueError, KeyError):
            print(f"Error en datos del producto: {dat}")
    print(f'\nValor total del inventario: ${total_value:.3f}')

#menu
def menu():
    while True:
        try:
        
            print("\033[34m\n------ Welcome inventary -----")
            print("\033[0m1. List product")
            print("\033[0m2. Add product")
            print("\033[0m3. Search product")
            print("\033[0m4. Update product")
            print("\033[0m5. Delete product")
            print("\033[0m6. total product")
            print("\033[0m7. Salir")
            
            Option = int(input("\033[0m\nEnter a option: "))
            
            if Option == 1:
                List()
            elif Option == 2:
                Add()
            elif Option == 3:
                Search()
            elif Option == 4:
                Update()
            elif Option == 5:
                Delete()
            elif Option == 6:
                Values()
            elif Option == 7:
                print("\n----- Good bye -----")
                break
            else:
                print("\033[91m\n### Option no valid ###")
        except ValueError:
            print("\033[91m\n### IEnter only numbers ###")
menu()