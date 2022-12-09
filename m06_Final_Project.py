"""
Name: David Amon
Date: 12/05/2022
Class: SDEV 140 - Introduction to Software Development
Program Purpose: Input Calorie consumption and expense - return daily calorie totals

Sources:
Images were sourced from https://clipartix.com/

Calorie data was sourced from the following:
https://sites.google.com/site/compendiumofphysicalactivities/tracking-guide
https://www.sportsrec.com/3201468/how-to-calculate-calories-burned

"""
from breezypythongui import *
import tkinter as tk
TkinterVar = tk
calorieOutputSum = 0
userTimeInHours = 0.0
optionSelectedValue = 0.0
wasNotDigit = False
grandTotalInput = 0

class MainClass(EasyFrame):
    """docstring"""
    def __init__(self):
        """Main window function - operates the GUI's infinite loop"""
        EasyFrame.__init__(self, title = "Calorie Calculator", width = 620, height = 500, resizable= False, background="#0069cc")
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
        self.columnconfigure(6, minsize=20)
        self.rowconfigure(6, minsize=5)

        # Headline image
        imageLabel = self.addLabel(text="", row=0, column=2, columnspan =2, rowspan=1, sticky="nsew")
        self.image = TkinterVar.PhotoImage(file="homeveggies.gif")
        imageLabel["image"] = self.image
        imageLabel.grid(sticky="nsew")
        imageLabel.config(bg="#0069cc")

        # Total boxes
        self.totalCaloriesConsumedField = self.addTextField(text="0", row=1, column=1, columnspan=1, sticky="nsew")
        self.totalCaloriesConsumedField.configure(justify="center", bg="#5289ee", bd=3)
        self.addLabel(text = "Total Calories In", row = 2, column = 1, columnspan=1,background="#0069cc", sticky="wn")
        self.totalCaloriesConsumedField.config(state=DISABLED) # Disables the field so the user can't update directly
        self.totalCaloriesConsumedField.configure({"disabledbackground": "#5289ee", "disabledforeground": "#000000"}) # corrects the colors of the disabled field

        self.addLabel(text = "Total Calories Out", row = 2, column = 4, columnspan=1, background="#0069cc", sticky="ne")
        self.totalCaloriesExercisedField = self.addTextField(text="0", row=1, column=4, columnspan=1, sticky="nswe")
        self.totalCaloriesExercisedField.configure(justify="center",bg="#5289ee", bd=3)
        self.totalCaloriesExercisedField.config(state=DISABLED) # Disables the field so the user can't update directly
        self.totalCaloriesExercisedField.configure({"disabledbackground": "#5289ee", "disabledforeground": "#000000"}) # corrects the colors of the disabled field

        # Input and Labels for food calories
        self.addLabel(text = "Breakfast: ", row = 3, column = 0, columnspan=1,background="#0069cc", sticky="ne")
        self.breakfastInputField = self.addTextField(text="", row=3, column=1, columnspan=1)

        self.addLabel(text = "Lunch: ", row = 4, column = 0, columnspan=1,background="#0069cc", sticky="ne")
        self.lunchInputField = self.addTextField(text="", row=4, column=1, columnspan=1)

        self.addLabel(text = "Dinner: ", row = 5, column = 0, columnspan=1,background="#0069cc", sticky="ne")
        self.dinnerInputField = self.addTextField(text="", row=5, column=1, columnspan=1)

        self.addLabel(text = "Snacks: ", row = 6, column = 0, columnspan=1,background="#0069cc", sticky="ne")
        self.snacksInputField = self.addTextField(text="", row=6, column=1, columnspan=1)

        # Add input calories together button
        self.sumOfFoodsButton = self.addButton(text = " Add Food Together", row = 7,\
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
                self.labelVar = self.addLabel(text = "Must be an Integer   ⇓⇓", row = 2, column = 3, columnspan=2, background="red", sticky="news")
                global wasNotDigit
                wasNotDigit = True
            else:
                if wasNotDigit == True:
                    self.labelVar.grid_remove()
                userWeightStored = int(self.weightTextField.get()) # Stores the entered information in a global variable
                print(str(userWeightStored) + " userWeightStored")
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
                print(str(singleExerciseSum) + " Single Exercise Sum")
                print(str(calorieOutputSum) + " Calorie Output Sum")
                self.totalCaloriesExercisedField.config(state=NORMAL)
                self.totalCaloriesExercisedField.setText(int(round(calorieOutputSum)))
                self.totalCaloriesExercisedField.config(state=DISABLED)
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
                                 column = 5, columnspan=2, command = close)
        self.exitButton.grid(sticky="nw")

# dropdown menu
        optionSelected = TkinterVar.StringVar()
        optionSelected.set("Click to Choose")
        drop = TkinterVar.OptionMenu(self, optionSelected, *exerciseOptions, command = dropDownItemWasSelected)
        drop.grid(row = 5, column = 3, sticky = "en", pady = 2, columnspan=2)
        drop.config(width = 14, bg="#0069cc", borderwidth=0)
       

# Final Results Button
        def finalWindow():
            global calorieInputSum
            global calorieOutputSum

            newWindow = TkinterVar.Toplevel(self) # creates a new window
            newWindow.geometry("500x250")
            newWindow.title("Final Result")
            newWindow.grab_set() # makes sure the master window cant be interacted with while the results window is open
            
            # Grid for the final window
            newWindow.columnconfigure(0, minsize=100)
            newWindow.rowconfigure(0, minsize=50)
            newWindow.columnconfigure(1, minsize=100)
            newWindow.rowconfigure(1, minsize=50)
            newWindow.columnconfigure(2, minsize=100)
            newWindow.rowconfigure(2, minsize=50)
            newWindow.columnconfigure(3, minsize=100)
            newWindow.rowconfigure(3, minsize=50)
            newWindow.columnconfigure(4, minsize=100)
            newWindow.rowconfigure(4, minsize=50)
            
            # Final Results Output
            aboveResultsOutput = TkinterVar.Label(newWindow, text="Calories Remaining")
            aboveResultsOutput.grid(row = 4, column = 1, sticky = "", columnspan=1, rowspan=1)
            finalResultsOutput = TkinterVar.Label(newWindow, text="0")
            finalResultsOutput.grid(row = 4, column = 2, sticky = "", columnspan=1, rowspan=1)

            try: # input validation for testing
                calorieInputSum
            except NameError:
                calorieInputSum = 0
            finalResultsOutput["text"] = str((int(calorieOutputSum) + 2000) - int(calorieInputSum))

            # Exit Button
            exitButton = TkinterVar.Button(newWindow, text='Close Window', command=newWindow.destroy)
            exitButton.grid(row = 4, column = 4, sticky = W)

            # Image
            heartImageContainer = TkinterVar.Label(newWindow, text="")
            self.imageFinale = TkinterVar.PhotoImage(file="heartperson.gif")
            heartImageContainer["image"] = self.imageFinale
            heartImageContainer.config(bg="#0069cc", justify="center", width=500)
            heartImageContainer.grid(row = 0, column = 0, sticky = "nsew", pady = 2, columnspan=5, rowspan=4)

        self.finalWindowButton = self.addButton(text = "Calculate Total", row = 1,\
                                    column = 2, columnspan=2,command = finalWindow)
        



# Adds all the 4 Meal Calorie boxes together when pressed
    def addsCalorieInput(self):
        """adds the 4 calorie input boxes together"""
        global calorieInputSum
        calorieInputSum=0
        breakfastNoms = self.breakfastInputField.getText()
        lunchNoms = self.lunchInputField.getText()
        dinnerNoms = self.dinnerInputField.getText()
        snacksNoms = self.snacksInputField.getText()

        #replaces nulls with 0's for processing
        if breakfastNoms == "" or breakfastNoms.isdigit() != True:
            self.breakfastInputField.setText(0)
            breakfastNoms = self.breakfastInputField.getText()
        if lunchNoms == "" or lunchNoms.isdigit() != True:
            self.lunchInputField.setText(0)
            lunchNoms = self.lunchInputField.getText()
        if dinnerNoms == "" or dinnerNoms.isdigit() != True:
            self.dinnerInputField.setText(0)
            dinnerNoms = self.dinnerInputField.getText()
        if snacksNoms == "" or snacksNoms.isdigit() != True:
            self.snacksInputField.setText(0)
            snacksNoms = self.snacksInputField.getText()
        calorieInputSum = int(breakfastNoms) + int(lunchNoms) + int(dinnerNoms) + int(snacksNoms)

        if calorieInputSum != 0:
            self.sumOfFoodsButton["text"] = "Press Again to Clear"
        if calorieInputSum == 0:
            self.sumOfFoodsButton["text"] = "Add Food Together"
        self.breakfastInputField.setText("")
        self.lunchInputField.setText("") # Clears the fields so the user can tell they successfully submitted
        self.dinnerInputField.setText("")
        self.snacksInputField.setText("")
        self.totalCaloriesConsumedField.config(state=NORMAL)
        self.totalCaloriesConsumedField.setText(calorieInputSum) # sets the banner text to the total sum
        self.totalCaloriesConsumedField.config(state=DISABLED)

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