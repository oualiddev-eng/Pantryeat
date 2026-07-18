# PantryEat 🥦

A pantry management app to reduce food waste — built in public from scratch.

We buy food, we forget about it, it expires. PantryEat helps you track 
what's in your pantry, when it expires, and what you've consumed.

---

## 🛠️ Technologies

- Python
- React 
- MySQL 

---

## ✨ Features

- **Track your ingredients** — Add ingredients with their category 
  (e.g. Tomato → Vegetable)
- **Manage your products** — Each product has a name, barcode, 
  quantity and unit (e.g. Tomato Sauce 500ml)
- **Monitor your pantry** — Know what's in your pantry, when it 
  expires and whether it's been consumed
- **Mark as consumed** — Toggle a product as consumed in one action
- **Recipe suggestions** — Get recipe ideas based on what's 
  currently available in your pantry

---

## 🗺️ The Process

I started by defining the core data models — the building blocks 
of the app.

First, I created the Ingredient class. Every product is made of 
ingredients, so it made sense to start there.

Then I built the Product class, which links to an ingredient and 
stores practical info like the barcode and quantity.

Finally, I created the PantryItem class — the heart of the app. 
It connects a product to a user, tracks the expiration date and 
whether the item has been consumed.

---

## 📚 What I Learned

- **Object-Oriented Programming** — Structuring real-world concepts 
  (ingredients, products, pantry items) into clean Python classes
- **Thinking before coding** — Designing the data model first saved 
  me a lot of refactoring later
- **Build in public** — Documenting the process forces you to truly 
  understand what you've built

---

## 🔮 How can it be improved?

- Add a MySQL database to persist data
- Build a REST API to expose the data
- Create a React frontend for a real user interface
- Add user authentication
- Add expiration date alerts

---

## ⚙️ Running the Project

1. Clone the repository
```bash
git clone https://github.com/oualiddev-eng/Pantryeat.git
```
2. Navigate to the project folder
```bash
cd Pantryeat
```
3. Run the test file
```bash
python main.py
```

---

## 📸 Follow the build

I'm documenting this entire journey on Instagram & Linkedin — every decision, 
every bug, every feature.

➡️ @oualiddev-eng

---
Built with ❤️ by [oualiddev-eng](https://github.com/oualiddev-eng)
