import tkinter as tk
from tkinter import messagebox, simpledialog


class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")
        self.root.geometry("700x500")
        self.root.config(bg="#f4f6f8")

        # Flashcards
        self.flashcards = [
            {
                "question": "What is Python?",
                "answer": "Python is a high-level, interpreted programming language."
            },
            {
                "question": "What is a variable?",
                "answer": "A variable is used to store data in a program."
            },
            {
                "question": "What does HTML stand for?",
                "answer": "HTML stands for HyperText Markup Language."
            }
        ]

        self.current_index = 0
        self.answer_visible = False

        self.create_ui()
        self.display_card()

    def create_ui(self):
        # Title
        title = tk.Label(
            self.root,
            text="📚 Flashcard Quiz",
            font=("Arial", 24, "bold"),
            bg="#f4f6f8",
            fg="#2c3e50"
        )
        title.pack(pady=20)

        # Card
        self.card = tk.Frame(
            self.root,
            bg="white",
            bd=2,
            relief="groove"
        )
        self.card.pack(
            padx=50,
            pady=10,
            fill="both",
            expand=True
        )

        # Question / Answer label
        self.content_label = tk.Label(
            self.card,
            text="",
            font=("Arial", 18),
            bg="white",
            fg="#2c3e50",
            wraplength=550,
            justify="center"
        )
        self.content_label.pack(
            expand=True,
            padx=30,
            pady=30
        )

        # Show Answer button
        self.show_button = tk.Button(
            self.root,
            text="Show Answer",
            command=self.show_answer,
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=8,
            relief="flat"
        )
        self.show_button.pack(pady=10)

        # Navigation buttons
        navigation_frame = tk.Frame(
            self.root,
            bg="#f4f6f8"
        )
        navigation_frame.pack(pady=5)

        tk.Button(
            navigation_frame,
            text="← Previous",
            command=self.previous_card,
            font=("Arial", 11),
            bg="#95a5a6",
            fg="white",
            padx=15,
            pady=6
        ).grid(row=0, column=0, padx=10)

        self.counter_label = tk.Label(
            navigation_frame,
            text="",
            font=("Arial", 11, "bold"),
            bg="#f4f6f8"
        )
        self.counter_label.grid(row=0, column=1, padx=20)

        tk.Button(
            navigation_frame,
            text="Next →",
            command=self.next_card,
            font=("Arial", 11),
            bg="#95a5a6",
            fg="white",
            padx=15,
            pady=6
        ).grid(row=0, column=2, padx=10)

        # Manage buttons
        manage_frame = tk.Frame(
            self.root,
            bg="#f4f6f8"
        )
        manage_frame.pack(pady=15)

        tk.Button(
            manage_frame,
            text="＋ Add",
            command=self.add_card,
            font=("Arial", 11, "bold"),
            bg="#27ae60",
            fg="white",
            padx=15,
            pady=6
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            manage_frame,
            text="✎ Edit",
            command=self.edit_card,
            font=("Arial", 11, "bold"),
            bg="#f39c12",
            fg="white",
            padx=15,
            pady=6
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            manage_frame,
            text="🗑 Delete",
            command=self.delete_card,
            font=("Arial", 11, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=15,
            pady=6
        ).grid(row=0, column=2, padx=5)

    # -----------------------------
    # Display current flashcard
    # -----------------------------
    def display_card(self):
        if not self.flashcards:
            self.content_label.config(
                text="No flashcards available.\n\nClick '+ Add' to create one."
            )
            self.counter_label.config(text="0 / 0")
            self.show_button.config(
                text="Show Answer",
                state="disabled"
            )
            return

        self.answer_visible = False

        card = self.flashcards[self.current_index]

        self.content_label.config(
            text=card["question"],
            fg="#2c3e50"
        )

        self.show_button.config(
            text="Show Answer",
            state="normal"
        )

        self.counter_label.config(
            text=f"{self.current_index + 1} / {len(self.flashcards)}"
        )

    # -----------------------------
    # Show answer
    # -----------------------------
    def show_answer(self):
        if not self.flashcards:
            return

        card = self.flashcards[self.current_index]

        if not self.answer_visible:
            self.content_label.config(
                text=card["answer"],
                fg="#27ae60"
            )

            self.show_button.config(
                text="Show Question"
            )

            self.answer_visible = True

        else:
            self.content_label.config(
                text=card["question"],
                fg="#2c3e50"
            )

            self.show_button.config(
                text="Show Answer"
            )

            self.answer_visible = False

    # -----------------------------
    # Next card
    # -----------------------------
    def next_card(self):
        if not self.flashcards:
            return

        if self.current_index < len(self.flashcards) - 1:
            self.current_index += 1
        else:
            self.current_index = 0

        self.display_card()

    # -----------------------------
    # Previous card
    # -----------------------------
    def previous_card(self):
        if not self.flashcards:
            return

        if self.current_index > 0:
            self.current_index -= 1
        else:
            self.current_index = len(self.flashcards) - 1

        self.display_card()

    # -----------------------------
    # Add flashcard
    # -----------------------------
    def add_card(self):
        question = simpledialog.askstring(
            "Add Flashcard",
            "Enter the question:"
        )

        if not question:
            return

        answer = simpledialog.askstring(
            "Add Flashcard",
            "Enter the answer:"
        )

        if not answer:
            return

        self.flashcards.append({
            "question": question,
            "answer": answer
        })

        self.current_index = len(self.flashcards) - 1

        self.display_card()

        messagebox.showinfo(
            "Success",
            "Flashcard added successfully!"
        )

    # -----------------------------
    # Edit flashcard
    # -----------------------------
    def edit_card(self):
        if not self.flashcards:
            messagebox.showwarning(
                "No Cards",
                "There are no flashcards to edit."
            )
            return

        card = self.flashcards[self.current_index]

        question = simpledialog.askstring(
            "Edit Flashcard",
            "Edit question:",
            initialvalue=card["question"]
        )

        if not question:
            return

        answer = simpledialog.askstring(
            "Edit Flashcard",
            "Edit answer:",
            initialvalue=card["answer"]
        )

        if not answer:
            return

        card["question"] = question
        card["answer"] = answer

        self.display_card()

        messagebox.showinfo(
            "Success",
            "Flashcard updated successfully!"
        )

    # -----------------------------
    # Delete flashcard
    # -----------------------------
    def delete_card(self):
        if not self.flashcards:
            messagebox.showwarning(
                "No Cards",
                "There are no flashcards to delete."
            )
            return

        confirm = messagebox.askyesno(
            "Delete Flashcard",
            "Are you sure you want to delete this flashcard?"
        )

        if confirm:
            self.flashcards.pop(self.current_index)

            if self.current_index >= len(self.flashcards):
                self.current_index = max(0, len(self.flashcards) - 1)

            self.display_card()


# -----------------------------
# Run application
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
