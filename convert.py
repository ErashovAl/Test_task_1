import os

os.makedirs("чеки_за_год", exist_ok=True)

monthly_cheques = {}
services = set()
months = set()

with open("чеки.txt", encoding='UTF-8-sig') as f:
    cheques = f.read().splitlines()
    
    for cheque_line in cheques:
        cheque_line = cheque_line.lstrip('\ufeff')
        service_name, month = cheque_line.split("_")
        month = month.split('.')[0]

        month_folder = os.path.join("чеки_за_год", month)
        os.makedirs(month_folder, exist_ok=True)
        new_cheque_path = os.path.join(month_folder, cheque_line)
        open(new_cheque_path, 'w').close()
        
        services.add(service_name)
        months.add(month)


not_paid_services = {}

for month in months:
    not_paid = []
    
    files_in_folder = os.listdir(os.path.join("чеки_за_год", month))
    
    for service_name in services:
        if f"{service_name}_{month}.pdf" not in files_in_folder:
            not_paid.append(service_name)
    
    if not_paid:
        not_paid_services[month] = not_paid 


with open("чеки_без_оплаты.txt", "w") as file:
    month_order = ['январь', 'февраль', 'март', 'апрель', 'май', 
                   'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    
    for month in month_order:
        if month in not_paid_services:
            services = not_paid_services[month]
            file.write(f"не оплачены:\nмесяц: {month}\n")
            # file.write(f"месяц: {month}\n")
            file.write("\n".join(services))
            file.write("\n\n")


    