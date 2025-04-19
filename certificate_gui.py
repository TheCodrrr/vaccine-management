import tkinter as tk
from PIL import Image, ImageTk

def generate_certificate(recipient_data, vaccine_data):
    root = tk.Tk()
    root.geometry("600x750")
    root.maxsize(600, 750)
    root.minsize(600, 750)
    root.configure(bg="white")
    root.title(f"{vaccine_data[0].lower()}_vaccination_certificate")

    image = Image.open("logo.jpeg")
    image = image.resize((150, 75))
    pic = ImageTk.PhotoImage(image)
    heading = tk.Label(image=pic, borderwidth=0, pady=20)
    heading.pack()

    heading = tk.Label(text=f"Final Certificate for {vaccine_data[0].upper()} Vaccination", bg="white", font="cominsansms 12 bold", fg="darkblue")
    heading.pack()

    heading = tk.Label(text="Recipient Details".upper(), bg="white", fg="blue", font="cominsansms 10 bold").place(x=30, y=125)

    heading = tk.Label(text="Recipient Name:", bg="white").place(x=50, y=155)
    heading = tk.Label(text="Father's Name:", bg="white").place(x=50, y=185)
    heading = tk.Label(text="Mother's Name:", bg="white").place(x=50, y=215)
    heading = tk.Label(text="Age:", bg="white").place(x=50, y=245)
    heading = tk.Label(text="Gender:", bg="white").place(x=50, y=275)
    heading = tk.Label(text="Reference Id:", bg="white").place(x=50, y=305)

    value = tk.Label(text=f"{recipient_data[0]}", bg="white", font="comicsansms 9 bold").place(x=300, y=155)
    value = tk.Label(text=f"{recipient_data[1]}", bg="white", font="comicsansms 9 bold").place(x=300, y=185)
    value = tk.Label(text=f"{recipient_data[2]}", bg="white", font="comicsansms 9 bold").place(x=300, y=215)
    value = tk.Label(text=f"{recipient_data[3]}", bg="white", font="comicsansms 9 bold").place(x=300, y=245)
    value = tk.Label(text=f"{recipient_data[4]}", bg="white", font="comicsansms 9 bold").place(x=300, y=275)
    value = tk.Label(text=f"{recipient_data[5]}", bg="white", font="comicsansms 9 bold").place(x=300, y=305)

    heading = tk.Label(text="Vaccination Details".upper(), bg="white", fg="blue", font="cominsansms 10 bold").place(x=30, y=345)

    heading = tk.Label(text="Disease Name:", bg="white").place(x=50, y=375)
    heading = tk.Label(text="Vaccine Name:", bg="white").place(x=50, y=405)
    heading = tk.Label(text="Date of Dose:", bg="white").place(x=50, y=435)
    heading = tk.Label(text="Dose Number:", bg="white").place(x=50, y=465)

    value = tk.Label(text=f"{vaccine_data[0]}", bg="white", font="comicsansms 9 bold").place(x=300, y=375)
    value = tk.Label(text=f"{vaccine_data[1]}", bg="white", font="comicsansms 9 bold").place(x=300, y=405)
    value = tk.Label(text=f"{vaccine_data[2]}", bg="white", font="comicsansms 9 bold").place(x=300, y=435)
    value = tk.Label(text=f"{vaccine_data[3]}", bg="white", font="comicsansms 9 bold").place(x=300, y=465)

    image2 = Image.open("end_image.jpeg")
    image2 = image2.resize((600, 250))
    pic2 = ImageTk.PhotoImage(image2)
    heading = tk.Label(image=pic2, borderwidth=0)
    heading.pack(side=tk.BOTTOM)

    image_tagline = tk.Label(text=f"Together, India will defeat", bg="#E8ECEF", font="comicsansms 11").place(x=147, y=545)
    image_tagline = tk.Label(text=f" {vaccine_data[0]}", bg="#E8ECEF", font="comicsansms 11").place(x=145, y=565)

    root.mainloop()