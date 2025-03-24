# Import necessary libraries
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import uuid
import os

# Function to get user input
def get_user_input(description):
    """
    This function gets user input in the form of a list of numbers separated by spaces.
    The user can enter multiple lists of numbers, and type 'generate' to finish.
    The function yields a numpy array of the input data.
    """
    while True:
        try:
            # Prompt the user to enter a list of numbers
            user_input = input("Please enter a list of numbers separated by spaces (or type 'generate' to finish, if you want to add decimal numbers, you should use '.' as separator): ")
            
            # Check if the user wants to finish
            if user_input.lower() == 'generate':
                break
            
            # Convert the input string to a list of floats
            data = list(map(float, user_input.strip().split()))
            
            # Yield a numpy array of the input data
            yield np.array(data).reshape(-1, 1)
        except ValueError:
            # Handle invalid input
            print("Please enter a list of numbers separated by spaces (or type 'generate' to finish, if you want to add decimal numbers, you should use '.' as separator).")

# Function to calculate statistical metrics
def calculate_statistics_metrics(data):
    """
    This function calculates the mean, median, variance, and standard deviation of the input data.
    """
    # Calculate the mean
    mean = np.mean(data)
    
    # Calculate the median
    median = np.median(data)
    
    # Calculate the variance
    variance = np.var(data)
    
    # Calculate the standard deviation
    std_dev = np.std(data)
    
    # Return the calculated metrics
    return mean, median, variance, std_dev

# Function to generate a PDF report
def generate_pdf(all_data, description, filename):
    """
    This function generates a PDF report of the input data and their statistical metrics.
    """
    # Create a PDF canvas
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Get the width and height of the page
    width, height = letter
    
    # Draw the title of the report
    c.drawString(100, height - 40, "Statistic Metrics Report")
    
    # Draw the description of the data
    c.drawString(100, height - 60, "Description:")
    c.drawString(100, height - 80, description)
    
    # Initialize the y-position
    y_position = height - 100
    
    # Iterate over the input data
    for idx, data in enumerate(all_data, 1):
        # Calculate the statistical metrics
        mean, median, variance, std_dev = calculate_statistics_metrics(data)
        
        # Draw the data set title
        c.drawString(100, y_position, f"Data Set {idx}:")
        y_position -= 20
        
        # Draw the original data
        c.drawString(100, y_position, "Original Data:")
        c.drawString(250, y_position, str(data.flatten()))
        
        # Draw the statistical metrics title
        c.drawString(100, y_position, "Statistical Metrics:")
        y_position -= 20
        
        # Draw the mean
        c.drawString(120, y_position, f"Mean: {mean}")
        y_position -= 20
        
        # Draw the median
        c.drawString(120, y_position, f"Median: {median}")
        y_position -= 20
        
        # Draw the variance
        c.drawString(120, y_position, f"Variance: {variance}")
        y_position -= 20
        
        # Draw the standard deviation
        c.drawString(120, y_position, f"Standard Deviation: {std_dev}")
        y_position -= 40
        
        # Check if we need to start a new page
        if y_position < 40:
            c.showPage()
            y_position = height - 40
    
    # Save the PDF
    c.save()

# Main function
def main():
    """
    This is the main function of the script.
    It gets user input, calculates statistical metrics, and generates a PDF report.
    """
    # Print a welcome message
    print("Welcome to the Data Transformation Script!")
    
    # Get the description of the data from the user
    description = input("Please enter a description of the data: ")
    
    # Initialize an empty list to store the input data
    all_data = []
    
    # Get user input
    for data in get_user_input(description):
        all_data.append(data)
    
    # Check if we have any data
    if not all_data:
        print("No data entered")
        return
    
    # Generate a random PDF filename
    filename = f"report_{uuid.uuid4()}.pdf"
    
    # Print the statistical metrics for each data set
    for idx, data in enumerate(all_data, 1):
        mean, median, variance, std_dev = calculate_statistics_metrics(data)
        
        print(f"\nData Set {idx}:")
        print("\nOriginal Data:")
        print(data.flatten())
        
        print("\nStatistical Metrics:")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Variance: {variance}")
        print(f"Standard Deviation: {std_dev}")
    
    # Generate the PDF report
    generate_pdf(all_data, description, filename)
    print(f"The results have been saved to {os.path.abspath(filename)}")      

# Call the main function
main()