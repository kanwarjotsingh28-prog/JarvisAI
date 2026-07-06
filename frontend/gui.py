import customtkinter as ctk

from backend.core.jarvis import JarvisCore


class JarvisGUI:

    def __init__(self):

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.jarvis = JarvisCore()

        self.root = ctk.CTk()

        self.root.title("JARVIS AI")

        self.root.geometry("1000x700")

        self.root.resizable(False, False)

        self.build()

    def build(self):

        title = ctk.CTkLabel(
            self.root,
            text="JARVIS AI",
            font=("Arial", 30, "bold")
        )

        title.pack(pady=20)

        self.chat = ctk.CTkTextbox(
            self.root,
            width=900,
            height=500,
            font=("Consolas", 16)
        )

        self.chat.pack()

        self.entry = ctk.CTkEntry(
            self.root,
            width=700,
            height=40,
            placeholder_text="Ask Jarvis..."
        )

        self.entry.pack(pady=20)

        self.entry.bind("<Return>", self.send)

        self.button = ctk.CTkButton(
            self.root,
            text="Send",
            command=lambda: self.send(None)
        )

        self.button.pack()

    def send(self, event=None):

        command = self.entry.get().strip()

        if command == "":
            return

        self.chat.insert("end", f"\n🧑 You : {command}\n")

        self.entry.delete(0, "end")

        result = self.jarvis.execute(command)

        response = result.get("response", "Done.")

        self.chat.insert("end", f"🤖 Jarvis : {response}\n")

        self.chat.see("end")

    def run(self):

        self.root.mainloop()