"""
Name: David Amon
Date: 12/05/2022
Class: SDEV 140 - Introduction to Software Development
Program Purpose: Input Calorie consumption and expense - return daily calorie total

"""
from breezypythongui import *
import tkinter as tk
root = tk

class MainClass(EasyFrame):
    """docstring"""
    def __init__(self):
        """docstring"""
        EasyFrame.__init__(self, title = "Calorie Calculator", width = 600, height = 500, resizable= False, background="#0069cc")
        self.columnconfigure(0, minsize=100)
        self.rowconfigure(0, minsize=10)
        self.columnconfigure(1, minsize=100)
        self.rowconfigure(1, minsize=10)
        self.columnconfigure(2, minsize=100)
        self.rowconfigure(2, minsize=10)
        self.columnconfigure(3, minsize=100)
        self.rowconfigure(3, minsize=10)
        self.columnconfigure(4, minsize=100)
        self.rowconfigure(4, minsize=10)
        self.columnconfigure(5, minsize=100)
        self.rowconfigure(5, minsize=10)
        #Headline
        self.addLabel(text = "Welcome!",background="#0069cc", row = 0, column = 2, columnspan=2, sticky="s")

        self.addLabel(text = "Total In", row = 2, column = 2, columnspan=1,background="#0069cc", sticky="w")
        self.addLabel(text = "Total Out", row = 2, column = 3, columnspan=1,background="#0069cc", sticky="e")
        self.addLabel(text = "Total Left", row = 1, column = 2, columnspan=2,background="#0069cc", sticky="s")

        # Input and Labels for food calories
        self.addLabel(text = "Breakfast: ", row = 3, column = 1, columnspan=1,background="#0069cc", sticky="ne")
        self.breakfastInputField = self.addTextField(text="", row=3, column=2, columnspan=1)

        self.addLabel(text = "Lunch: ", row = 4, column = 1, columnspan=1,background="#0069cc", sticky="ne")
        self.lunchInputField = self.addTextField(text="", row=4, column=2, columnspan=1)

        self.addLabel(text = "Dinner: ", row = 5, column = 1, columnspan=1,background="#0069cc", sticky="ne")
        self.dinnerInputField = self.addTextField(text="", row=5, column=2, columnspan=1)

        self.addLabel(text = "Snacks: ", row = 6, column = 1, columnspan=1,background="#0069cc", sticky="ne")
        self.snacksInputField = self.addTextField(text="", row=6, column=2, columnspan=1)

        self.sumOfFoodsButton = self.addButton(text = " Add food together", row = 7,\
                                 column = 1, command = self.addsCalorieInput, columnspan=2)
        self.sumOfFoodsButton.grid(sticky="ne")




        self.exerciseTextField = self.addTextField(text="Exercise in hours", row=4, column=3, columnspan=2, sticky="s")
        
        # Would like to make it so on click the initial text in the input field disappears 
        # def simpleFieldWiper():
        #     self.exerciseTextField.delete(0,"end") 
        # self.exerciseTextField.bind("<FocusIn>", simpleFieldWiper())
        
        
        exerciseOptions = [
            "Aerobics",
            "Bicycling",
            "Football",
            "Hiking",
            "Jogging",
            "Jumping Rope",
            "Pilates",
            "Rowing",
            "Running",
            "Swimming",
            "Tennis",
            "Walking",
            "Yoga"
        ]
        exerciseDictionary = {"Aerobics":7.3, "Basketball":6.5, "Bicycling":7.0, "Football":8.0, "Hiking":5.3,\
            "Jogging":7.0, "Jumping Rope":11.8, "Pilates":3.0, "Rowing":8.5, "Running":9.2, "Swimming":5.8, "Tennis":7.3, "Walking":4.8, "Yoga":6.0}

        def printerthing():
            variableator=optionSelected.get()
            print(variableator + " yo")

# dropdown menu
        optionSelected = root.StringVar()
        optionSelected.set("Click to Choose")
        drop = root.OptionMenu(self, optionSelected, *exerciseOptions, command=printerthing())
        drop.grid(row = 5, column = 3, sticky = "n", pady = 2, columnspan=2)
        drop.config(width = 14, bg="#0069cc", borderwidth=0)
        
# Function that takes the output text from the options menu, checks it against the keys in the encyclopedia - then returns the calorie info

# Function that takes the returned calorie info, and calculates it further into the desired output


        
# Adds all the 4 Meal Calorie boxes together when pressed
    def addsCalorieInput(self):
        """docstring"""
        calorieInputSum = int(self.breakfastInputField.getText()) + int(self.lunchInputField.getText()) + int(self.dinnerInputField.getText()) + int(self.snacksInputField.getText())
        print( calorieInputSum) #make it return the value, also make it clear the text fields

# Calorie calculator Function (input minus output)

    def finalSummation(calorieInputSum, calorieOutputSum):
        """docstring"""
        calorieInputSum = 1
        calorieOutputSum = 1
        return calorieInputSum + (calorieOutputSum + 2000) # could make this 2000 calorie thing a changable variable



# Code Below Operates the GUI infinite loop
def main():
    """Instantiate and pop up the window."""
    MainClass().mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")