import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Глобальная переменная для хранения результатов
results = ""

def calculate_pythagorean_numbers(day, month, year):
    # Пересмотренный расчёт без отрицательных чисел
    sum_day_month = day + month
    sum_year = sum(map(int, str(year)))
    first_working_number = sum(map(int, str(sum_day_month + sum_year)))  # Обеспечиваем однозначный результат

    if day >= 10:
        day_first_digit = int(str(day)[0])
    else:
        day_first_digit = day
    third_working_number = sum(map(int, str(2 * day_first_digit)))  # Изменено для избежания отрицательных результатов

    second_working_number = sum(map(int, str(first_working_number)))  # Обеспечиваем однозначный результат
    fourth_working_number = sum(map(int, str(third_working_number)))  # Обеспечиваем однозначный результат
    
    return first_working_number, second_working_number, third_working_number, fourth_working_number

def calculate_and_show():
    global results
    date_str = entry_date.get()
    try:
        birth_date = datetime.strptime(date_str, "%d.%m.%Y")
        day, month, year = birth_date.day, birth_date.month, birth_date.year
        first, second, third, fourth = calculate_pythagorean_numbers(day, month, year)
        
        results = f"1-е рабочее число: {first}\n2-е рабочее число: {second}\n"\
                  f"3-е рабочее число: {third}\n4-е рабочее число: {fourth}"
                  
        messagebox.showinfo("Результаты", results)
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный формат даты. Используйте ДД.ММ.ГГГГ")

def open_email_window():
    if not results:
        messagebox.showerror("Ошибка", "Сначала рассчитайте результаты.")
        return

    def send_email():
        email = email_entry.get()
        messagebox.showinfo("Отправка", f"Результаты были бы отправлены на {email} (функция не реализована).")
        email_window.destroy()
    
    email_window = tk.Toplevel(root)
    email_window.title("Отправить результаты на почту")
    email_window.geometry("300x200")
    email_window.configure(bg='light blue')
    
    tk.Label(email_window, text="Введите адрес электронной почты:", bg='light blue', fg='dark blue').pack(pady=10)
    email_entry = tk.Entry(email_window)
    email_entry.pack(pady=10)
    
    send_button = tk.Button(email_window, text="Отправить", command=send_email, bg='dark blue', fg='white')
    send_button.pack(pady=20)

# Создание GUI
root = tk.Tk()
root.title("Расчет по методу Пифагора")
root.geometry("300x600")
root.configure(bg='light blue')

tk.Label(root, text="Введите дату рождения (ДД.ММ.ГГГГ):", bg='light blue', fg='dark blue').pack(pady=(20, 0))
entry_date = tk.Entry(root)
entry_date.pack(pady=(0, 20))

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_and_show, bg='dark blue', fg='white')
calculate_button.pack(pady=(0, 20))

email_button = tk.Button(root, text="Отправить результат", command=open_email_window, bg='dark blue', fg='white')
email_button.pack(pady=(0, 20))

root.mainloop()
