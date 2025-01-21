import tkinter as tk
from tkinter import messagebox

#dane o wydarzeniach
events = {
    "Koncert Kanye West": {"data": "2025-02-10", "miejsca": 50},
    "Koncert Travis Scott": {"data": "2025-02-14", "miejsca": 30},
    "Koncert 21 savage": {"data": "2025-03-01", "miejsca": 20},
}

#funk do wyswetlania wydarzen
def show_events():
    event_list.delete(0, tk.END)
    for event, details in events.items():
        event_list.insert(tk.END, f"{event} - Data: {details['data']} - Dostępne miejsca: {details['miejsca']}")

#funk dodawania nowego wydarzenia
def add_event():
    name = entry_name.get()
    date = entry_date.get()
    seats = entry_seats.get()

    if name and date and seats.isdigit():
        events[name] = {"data": date, "miejsca": int(seats)}
        show_events()
        entry_name.delete(0, tk.END)
        entry_date.delete(0, tk.END)
        entry_seats.delete(0, tk.END)
        messagebox.showinfo("Sukces", "Wydarzenie zostało dodane.")
    else:
        messagebox.showerror("Błąd", "Proszę wprowadzić poprawne dane.")

#funk rezerwacju miejsc
def book_tickets():
    selected_event = event_list.get(tk.ACTIVE)
    if not selected_event:
        messagebox.showerror("Błąd", "Proszę wybrać wydarzenie.")
        return

    event_name = selected_event.split(" - ")[0]
    tickets = entry_tickets.get()

    if tickets.isdigit() and event_name in events:
        tickets = int(tickets)
        if events[event_name]["miejsca"] >= tickets:
            events[event_name]["miejsca"] -= tickets
            show_events()
            entry_tickets.delete(0, tk.END)
            messagebox.showinfo("Sukces", f"Zarezerwowano {tickets} bilet(y/ów) na {event_name}.")
        else:
            messagebox.showerror("Błąd", "Nie ma wystarczającej liczby miejsc.")
    else:
        messagebox.showerror("Błąd", "Proszę wprowadzić poprawną liczbę biletów.")

#glowne okno
root = tk.Tk()
root.title("System Rezerwacji Wydarzeń")

#lista wyd.
event_list = tk.Listbox(root, width=60, height=10)
event_list.pack(pady=10)
show_events()

# Formularz dodawania wydarzenia
frame_add = tk.Frame(root)
frame_add.pack(pady=10)

tk.Label(frame_add, text="Nazwa:").grid(row=0, column=0)
entry_name = tk.Entry(frame_add)
entry_name.grid(row=0, column=1)

tk.Label(frame_add, text="Data (YYYY-MM-DD):").grid(row=1, column=0)
entry_date = tk.Entry(frame_add)
entry_date.grid(row=1, column=1)

tk.Label(frame_add, text="Miejsca:").grid(row=2, column=0)
entry_seats = tk.Entry(frame_add)
entry_seats.grid(row=2, column=1)

tk.Button(frame_add, text="Dodaj wydarzenie", command=add_event).grid(row=3, columnspan=2, pady=5)

#rezerwacja biletow
frame_book = tk.Frame(root)
frame_book.pack(pady=10)

tk.Label(frame_book, text="Liczba biletów:").grid(row=0, column=0)
entry_tickets = tk.Entry(frame_book)
entry_tickets.grid(row=0, column=1)

tk.Button(frame_book, text="Zarezerwuj", command=book_tickets).grid(row=1, columnspan=2, pady=5)

# Uruchomienie aplikacji
root.mainloop()
