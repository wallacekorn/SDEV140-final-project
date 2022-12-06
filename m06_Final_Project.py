"""
Name: David Amon
Date: 12/05/2022
Class: SDEV 140 - Introduction to Software Development
Program Purpose: Input Calorie consumption and expense - return daily calorie totals

"""
from breezypythongui import *
import tkinter as tk
root = tk
calorieOutputSum = 0
userTimeInHours = 0.0
optionSelectedValue = 0.0
wasNotDigit = False

class MainClass(EasyFrame):
    """docstring"""
    def __init__(self):
        """docstring"""
        EasyFrame.__init__(self, title = "Calorie Calculator", width = 600, height = 500, resizable= False, background="#0069cc")
        self.columnconfigure(0, minsize=100)
        self.rowconfigure(0, minsize=5)
        self.columnconfigure(1, minsize=100)
        self.rowconfigure(1, minsize=5)
        self.columnconfigure(2, minsize=100)
        self.rowconfigure(2, minsize=5)
        self.columnconfigure(3, minsize=100)
        self.rowconfigure(3, minsize=5)
        self.columnconfigure(4, minsize=100)
        self.rowconfigure(4, minsize=5)
        self.columnconfigure(5, minsize=100)
        self.rowconfigure(5, minsize=5)

        #Headline
        self.addLabel(text = "Welcome!",background="#0069cc", row = 0, column = 2, columnspan=2, sticky="s")

        # Temporary, just feeling out the layout until i split the windows
        self.addLabel(text = "Total In", row = 2, column = 1, columnspan=1,background="#0069cc", sticky="w")
        self.addLabel(text = "Total Out", row = 2, column = 3, columnspan=1,background="#0069cc", sticky="e")
        self.addLabel(text = "Total Left", row = 1, column = 2, columnspan=2,background="#0069cc", sticky="s")

        # Input and Labels for food calories
        self.addLabel(text = "Breakfast: ", row = 3, column = 0, columnspan=1,background="#0069cc", sticky="ne")
        self.breakfastInputField = self.addTextField(text="", row=3, column=1, columnspan=1)

        self.addLabel(text = "Lunch: ", row = 4, column = 0, columnspan=1,background="#0069cc", sticky="ne")
        self.lunchInputField = self.addTextField(text="", row=4, column=1, columnspan=1)

        self.addLabel(text = "Dinner: ", row = 5, column = 0, columnspan=1,background="#0069cc", sticky="ne")
        self.dinnerInputField = self.addTextField(text="", row=5, column=1, columnspan=1)

        self.addLabel(text = "Snacks: ", row = 6, column = 0, columnspan=1,background="#0069cc", sticky="ne")
        self.snacksInputField = self.addTextField(text="", row=6, column=1, columnspan=1)

        self.sumOfFoodsButton = self.addButton(text = " Add food together", row = 7,\
                                 column = 0, command = self.addsCalorieInput, columnspan=2)
        self.sumOfFoodsButton.grid(sticky="ne")

# Calorie Output Fields
        # User Weight field and label
        self.addLabel(text = "User Weight (Lbs)", row = 3, column = 2, columnspan=2,background="#0069cc", sticky="e")
        self.weightTextField = self.addTextField(text="", row=3, column=4, columnspan=1, sticky="w", state="normal", width= 20)

        # User Weight Lock-in Button Function
        def userWeightLockIn():
            """docstring"""           
            global userWeightStored
            if self.weightTextField.get().isdigit() == False:                
                self.labelVar = self.addLabel(text = "Must be an Integer", row = 3, column = 2, columnspan=2, background="red", sticky="se")
                global wasNotDigit
                wasNotDigit = True
            else:
                if wasNotDigit == True:
                    self.labelVar.grid_remove()
                userWeightStored = int(self.weightTextField.get()) # Stores the entered information in a global variable
                print(userWeightStored)
                currentFieldState = self.weightTextField["state"]
                if currentFieldState == 'disabled':                 # if current state is disabled, it enables the button on press
                    self.weightTextField.configure(state="normal")
                    self.weightLockIn["text"] = "Lock-In Weight"
                else:                                               # if current state is normal, disables the button on press
                    self.weightTextField.configure(state="disabled")
                    self.weightLockIn["text"] = "Unlock Weight"
                    self.weightLockIn["width"] = 20

        # The weight lock-in button itself
        self.weightLockIn = self.addButton(text = "Lock-in Weight", row = 3,\
                            column = 5, command = userWeightLockIn, columnspan=1)
        self.weightLockIn.grid(sticky="e")
        
        # Exercise text input field and button

        self.addLabel(text = "Exercise (Minutes)", row = 4, column = 2, columnspan=2,background="#0069cc", sticky="e")
        self.exerciseTextField = self.addTextField(text="", row=4, column=4, columnspan=1, sticky="w")
        print(str(optionSelectedValue) + " initial optionSelectedValue")
        def exerciseTextFieldButtonFunction():
            """docstring"""
            global userTimeInHours
            global optionSelectedValue
            global userWeightStored
            print(str(calorieOutputSum) + " Calorie Output Sum exerciseTextFieldButtonFunction")
            def singleExerciseCalorieCalculator():
                """
                Takes the Entered userWeightStored in pounds, divides by 2.2 to get KG
                Multiplies this against the MET - Metabolic Equivalent of Task
                Then multiplies this against the users entered time (converted into hours)
                to get a total caloric burn for the activity
                """
                global userTimeInHours
                global optionSelectedValue
                global userWeightStored
                global singleExerciseSum
                global calorieOutputSum
                print(str(userWeightStored) + " userWeightStored")
                print(str(optionSelectedValue) + " optionSelectedValue")
                print(str(userTimeInHours) + " userTimeInHours")
                singleExerciseSum = ((userWeightStored/2.2) * optionSelectedValue) * userTimeInHours
                calorieOutputSum += singleExerciseSum
                print(str(calorieOutputSum) + " Calorie Output Sum singleexercisesum")
            enteredMinutesOfExercise = self.exerciseTextField.get()
            self.exerciseTextField.setText("")
            userTimeInHours = round(int(enteredMinutesOfExercise) / 60,2)
            singleExerciseCalorieCalculator()
            
        # the button
        self.singleExerciseSubmitButton = self.addButton(text = "Add to Total", row = 4,\
                                 column = 5, command = exerciseTextFieldButtonFunction, columnspan=1)
        self.singleExerciseSubmitButton.grid(sticky="e")
        self.singleExerciseSubmitButton["width"] = 20

        # Exercise Data stored in variables
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
        excerciseDictionaryLength = len(exerciseDictionary)

# Function that takes the output text from the options menu, checks it against the keys in the encyclopedia - then returns the VALUE that matches the KEY
        def dropDownItemWasSelected(optionSelected):
            """docstring"""
            optionSelectedVar = optionSelected
            global optionSelectedValue
            for i in exerciseDictionary: # iterates over the dictionary to find a match

                if i == optionSelectedVar: # if a match is found, it assigns the key's value to a variable
                    
                    optionSelectedValue = exerciseDictionary[optionSelectedVar]

# Exit button - function and button
        def close():
            """Closes the Application on execution"""
            self.quit()
        self.exitButton = self.addButton(text = "Exit the Program", row = 0,\
                                 column = 5, command = close)
        self.exitButton.grid(sticky="nw")

# dropdown menu
        optionSelected = root.StringVar()
        optionSelected.set("Click to Choose")
        drop = root.OptionMenu(self, optionSelected, *exerciseOptions, command = dropDownItemWasSelected)
        drop.grid(row = 5, column = 3, sticky = "en", pady = 2, columnspan=2)
        drop.config(width = 14, bg="#0069cc", borderwidth=0)
       
# Adds all the 4 Meal Calorie boxes together when pressed
    def addsCalorieInput(self):
        """adds the 4 calorie input boxes together"""
        #need to test for non-entrys and fill in with 0's
        global calorieInputSum
        calorieInputSum = int(self.breakfastInputField.getText()) + int(self.lunchInputField.getText()) + int(self.dinnerInputField.getText()) + int(self.snacksInputField.getText())
        self.breakfastInputField.setText("")
        self.lunchInputField.setText("") # Clears the fields so the user can tell they successfully submitted
        self.dinnerInputField.setText("")
        self.snacksInputField.setText("")

# Calorie calculator Function (input minus output)
    def finalSummation(calorieInputSum, calorieOutputSum):
        """Takes the calorie output sum and calorie input sum and combines them, adding in the estimated 2000 calories a day from BMR"""
        return (calorieOutputSum + 2000) - calorieInputSum # could make this 2000 calorie thing a changable variable if there is time



# Code Below Operates the GUI infinite loop
def main():
    """Instantiate and pop up the window."""
    MainClass().mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
            exit(0) # exits the program when 'quit()' is called instead of continually running
    except KeyboardInterrupt:
        print("\nProgram closed.")