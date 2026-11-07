energy = int(0)
click_quantity = int(1)
upgrade_price = int(10)
upgrade_quantify = int(1)

def show_statistics():
    print(f"===IDLE CLICKER===\nEnergia: {energy}\nIlość za kliknięcie: {click_quantity}\n1.Kliknij (+{click_quantity} energii)\n2.Kup ulepszenie - +1 więcej energii co klik (Cena: {upgrade_price})\n3.Sprawdź statsytyki.\n4.Wyjdź z gry.")

show_statistics()

while True:
    answer = str(input(""))
    if answer == '1':
        energy += click_quantity
        print(f"Dodana energia: {click_quantity}, Balans: {energy}")
    elif answer == '2':
        if energy < upgrade_price:
            print(f"Nie możesz tego kupić, masz za mało energii\nEnergia: {energy}, Cena ulepszenia: {upgrade_price}")
        else:
            energy -= upgrade_price
            click_quantity += 1
            print(f"Zakupiłeś ulepszenie! Teraz dostajesz {click_quantity} energii za kliknięcie!\nEnergia: {energy}")
    elif answer == '3':
        show_statistics()
    elif answer == '4':
        print("Szkoda, że już kończysz grę :(")
        break
    

    
