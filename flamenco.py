import random
import string
from fpdf import FPDF

class FlamencoRoutineGenerator:
    """
    Generates flamenco dance routines based on the style and duration.

    Attributes:
        styles (list): List of available flamenco styles.
        steps (dict): Dictionary of steps for each flamenco style.
        durations (list): List of available durations.

    Methods:
        generate_routine(style, duration): Generates a flamenco routine based on the style and duration.
        display_routine(routine): Displays the generated routine.
        save_routine_to_pdf(name, style, duration, routine, comment, pdf): Saves the generated routine to a PDF file.
    """

    def __init__(self):
        self.styles = ['Solea', 'Bulerias', 'Tangos', 'Alegrias']
        self.steps = {
            'Solea': ['Salida', 'Marcaje', 'Escobilla', 'Llamada', 'Final'],
            'Bulerias': ['Salida', 'Marcaje', 'Falseta', 'Llamada', 'Final'],
            'Tangos': ['Entrada', 'Marcaje', 'Llamada', 'Letra', 'Final'],
            'Alegrias': ['Salida', 'Marcaje', 'Escobilla', 'Silencio', 'Final']
        }
        self.durations = ['Short', 'Medium', 'Long']

    def generate_routine(self, style, duration):
        """
        Generates a flamenco routine based on the style and duration.

        Args:
            style (str): The style of the routine.
            duration (str): The duration of the routine.

        Returns:
            list: The generated routine.

        Raises:
            ValueError: If the style or duration is invalid.
        """
        if style not in self.styles:
            raise ValueError(f"Invalid style. Choose from: {', '.join(self.styles)}")
        if duration not in self.durations:
            raise ValueError(f"Invalid duration. Choose from: {', '.join(self.durations)}")

        num_steps = {
            'Short': 2,
            'Medium': 4,
            'Long': 5
        }[duration]

        routine = random.sample(self.steps[style], num_steps)
        return routine

    def display_routine(self, routine):
        """
        Displays the generated routine.

        Args:
            routine (list): The generated routine.
        """
        print("Generated Flamenco Routine:")
        for i, step in enumerate(routine):
            print(f"Step {i + 1}: {step}")

    def save_routine_to_pdf(self, name, style, duration, routine, comment, pdf):
        """
        Saves the generated routine to a PDF file.

        Args:
            name (str): The name of the user.
            style (str): The style of the routine.
            duration (str): The duration of the routine.
            routine (list): The generated routine.
            comment (str): The comment for the routine.
            pdf (FPDF): The PDF object.
        """
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt=f"Name: {name}", ln=True, align='L')
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Flamenco Routine - {style} ({duration})", ln=True, align='C')
        pdf.ln(10)
        for i, step in enumerate(routine):
            pdf.cell(200, 10, txt=f"Step {i + 1}: {step}", ln=True, align='L')
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Comment: {comment}", ln=True, align='L')


def generate_random_name(length):
    """
    Generates a random name of the given length.

    Args:
        length (int): The length of the name.

    Returns:
        str: The generated name.
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def main():
    """
    Main function that runs the Flamenco Routine Generator.
    """
    generator = FlamencoRoutineGenerator()

    print("Welcome to the Flamenco Routine Generator!")
   
    name = input("Please enter your name: ")

    pdf = FPDF()

    while True:
        print("1. Generate a routine")
        print("2. Create a custom routine")
        choice = input("Please choose an option: ")

        if choice == "1":
            style_input = input("Please enter a flamenco style between Solea, Bulerias, Tangos or Alegrias: ")
            while style_input not in generator.styles:
                print("Invalid style. Please try again.")
                style_input = input("Please enter a flamenco style between Solea, Bulerias, Tangos or Alegrias: ")

            duration_input = input("Please enter a Duration between Short, Medium and Long: ")
            while duration_input not in generator.durations:
                print("Invalid duration. Please try again.")
                duration_input = input("Please enter a Duration between Short, Medium and Long: ")

            style = style_input
            duration = duration_input
            routine = generator.generate_routine(style, duration)
            generator.display_routine(routine)
            comment = input("Please enter a comment for the routine: ")
            generator.save_routine_to_pdf(name, style, duration, routine, comment, pdf)

        elif choice == "2":
            custom_style = input("Please enter the name of the custom routine: ")
            num_steps = int(input("Please enter the number of steps for the custom routine: "))
            custom_routine = []
            for i in range(num_steps):
                step = input(f"Please enter step {i + 1}: ")
                custom_routine.append(step)
            comment = input("Please enter a comment for the routine: ")
            generator.save_routine_to_pdf(name, custom_style, "Custom", custom_routine, comment, pdf)

        cont = input("Do you want to generate another routine? (yes/no): ")
        if cont.lower() != "yes":
            break

    pdf_name = f"flamenco_routine_{generate_random_name(10)}.pdf"
    pdf.output(pdf_name)
    print(f"PDF saved as {pdf_name}")


if __name__ == "__main__":
    main()



