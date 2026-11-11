import time
from database import init_db, load_player, save_player, create_player

init_db()
player = load_player(1)

if player is None:
    create_player(0)
    player = load_player(1)

energy = player["energy"]
click_quantity = player["click_quantity"]
upgrade_price = player["upgrade_price"]
all_clicks = player["all_clicks"]
upgrade_quantity = player["upgrade_quantity"]
generators_quantity = player["generators_quantity"]
factory_price = player["factory_price"]
factory_energy_quantity = generators_quantity
energy_given = 0

start = time.time()
print(start)
last_time = time.time()

last_save = time.time()
    
def click(): 
    global energy, all_clicks
    
    energy += click_quantity
    all_clicks += 1
    print(f"Dodana energia: {click_quantity}, Balans: {energy}")

def stop():
    print("Szkoda, że już kończysz grę :(")

def show_statistics():
    print(f"===IDLE CLICKER===\nEnergia: {energy}\nIlość za kliknięcie: {click_quantity}\nWszystkie kliknięcia: {all_clicks}\nKupione ulepszenia: {upgrade_quantity}\nGeneratory: {generators_quantity}\nProdukcja: {factory_energy_quantity} energii/s\n1.Kliknij (+{click_quantity} energii)\n2.Kup ulepszenie - +1 więcej energii co klik (Cena: {upgrade_price})\n3.Kup generator energii (Cena: {factory_price})\n4.Odbierz energię z generatorów (do odebrania: {int(energy_given)})\n5.Sprawdź statsytyki.\n6.Wyjdź z gry.")

show_statistics()

while True:
    answer = str(input(""))
    if factory_energy_quantity > 0:
        current_time = time.time()
        seconds_passed = current_time - last_time
        energy_given += seconds_passed * factory_energy_quantity
        last_time = current_time
    if answer == '1':
        click()
    elif answer == '2':
        if energy < upgrade_price:
            print(f"Nie możesz tego kupić, masz za mało energii\nEnergia: {energy}, Cena ulepszenia: {upgrade_price}")
        else:
            energy -= upgrade_price
            click_quantity += 1
            upgrade_price = int(upgrade_price * 1.5)
            upgrade_quantity += 1
            print(f"Zakupiłeś ulepszenie! Teraz dostajesz {click_quantity} energii za kliknięcie!\nEnergia: {energy}\nNastępna cena ulepszenia: {upgrade_price}")
    elif answer == '3':
        if energy < factory_price:
            print(f"Przykro mi :( Nie możesz zakupić generatora. Masz tylko {energy} energii..\nCena fabryki: {factory_price}")
        else:
            factory_energy_quantity += 1
            generators_quantity += 1
            energy -= factory_price
            factory_price = factory_price * 2
            if generators_quantity == 1:
                last_time = time.time()
            print(f"Świetnie! Zakupiłeś generator! Od teraz będzie ci generował {factory_energy_quantity} energii na sekundę!\nNastępny generator kosztuję: {factory_price} energii.")
    elif answer == '4':
        collected_energy = int(energy_given)
        print(f"Pomyślnie odebrałeś {collected_energy} energii.")
        energy += collected_energy
        energy_given -= collected_energy
        print(f"Balans energii po zakupie: {energy}")
    elif answer == '5':
        show_statistics()
    elif answer == '6':
        save_player(1, energy, click_quantity, all_clicks, upgrade_quantity, upgrade_price, generators_quantity, factory_price)
        stop()
        break

    if time.time() - last_save >= 30:
        save_player(1, energy, click_quantity, all_clicks, upgrade_quantity, upgrade_price, generators_quantity, factory_price)
        last_save = time.time()
    

    
