"""
Name: David Amon
Date: 12/11/2022
Class: SDEV 140 - Introduction to Software Development
Program Purpose: Input Calorie consumption and expense - return daily calorie totals

Sources:
Images were sourced from https://clipartix.com/

Calorie data was sourced from the following:
https://sites.google.com/site/compendiumofphysicalactivities/tracking-guide
https://www.sportsrec.com/3201468/how-to-calculate-calories-burned

"""
from breezypythongui import *       # Imports the modules used for the GUI
import tkinter as tk                # Imports the modules used for the GUI
TkinterVar = tk                     # A little more understandable in the code to me
calorieOutputSum = 0                # Exercise'd calories overall sum holder
userTimeInHours = 0.0               # Stores the users input time in hours
optionSelectedValue = 0.0           # Assigns a value to the initial key in the dropdown menu
wasNotDigit = False                 # a flag for toggling a label
grandTotalInput = 0                 # final results grand total holder

class MAIN_CLASS(EasyFrame):
    """docstring"""
    def __init__(self):
        """Main window function - operates the GUI's infinite loop"""
        EasyFrame.__init__(self, title = "Calorie Calculator", width = 620, height = 500, resizable= False, background="#0069cc") # builds the main window

        # Defines the grid sizes for the main window
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
        imageLabel = self.addLabel(text="", row=0, column=2, columnspan =2, rowspan=1, sticky="nsew")   # creates a label container for the image
        self.image = TkinterVar.PhotoImage(file="homeveggies.gif") # image in a variable
        imageLabel["image"] = self.image                           # assigns the image variable to the label containter
        imageLabel.grid(sticky="nsew")                             # grid styling
        imageLabel.config(bg="#0069cc")                            # changes the containers background color to match the rest of the app

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
        self.sumOfFoodsButton = self.addButton(text = " Add Food Together", row = 7, column = 0, command = self.addsCalorieInput, columnspan=2)
        self.sumOfFoodsButton.grid(sticky="ne")

# Calorie Output Fields
        # User Weight field and label
        self.addLabel(text = "User Weight (Lbs)", row = 3, column = 2, columnspan=2,background="#0069cc", sticky="e")
        self.weightTextField = self.addTextField(text="", row=3, column=4, columnspan=1, sticky="w", state="normal", width= 20)
        
        # User Weight Lock-in Button Function
        def userWeightLockIn():
            """button function that 'locks in' the users weight by disabling the input field"""           
            global userWeightStored
            if self.weightTextField.get().isdigit() == False:           # Displays an error label if an integer is not entered in the weight field         
                self.labelVar = self.addLabel(text = "Must be an Integer   ⇓⇓", row = 2, column = 3, columnspan=2, background="red", sticky="news")
                global wasNotDigit
                wasNotDigit = True                                      # a tracker so the 'must be an integer' label can be removed later
            else:
                if wasNotDigit == True:                                 # removes the 'must be an integer' label if a successful integer is entered
                    self.labelVar.grid_remove()
                userWeightStored = int(self.weightTextField.get())      # Stores the entered information in a global variable
                print(str(userWeightStored) + " userWeightStored")      # testing
                currentFieldState = self.weightTextField["state"]       # stores the field state in a variable for comparison
                if currentFieldState == 'disabled':                     # if current state is disabled, it enables the button on press
                    self.weightTextField.configure(state="normal")
                    self.weightLockIn["text"] = "Lock-In Weight"
                else:                                                   # if current state is normal, disables the button on press
                    self.weightTextField.configure(state="disabled")
                    self.weightLockIn["text"] = "Unlock Weight"
                    self.weightLockIn["width"] = 20

        # The weight lock-in button itself
        self.weightLockIn = self.addButton(text = "Lock-in Weight", row = 3, column = 5, command = userWeightLockIn, columnspan=1)
        self.weightLockIn.grid(sticky="e")
        
        # Exercise text input field and button

        self.addLabel(text = "Exercise (Minutes)", row = 4, column = 2, columnspan=2,background="#0069cc", sticky="e")
        self.exerciseTextField = self.addTextField(text="", row=4, column=4, columnspan=1, sticky="w")

        def exerciseTextFieldButtonFunction():
            """docstring"""
            global userTimeInHours                                  # lets just pretend these aren't here for now
            global optionSelectedValue                              # lets just pretend these aren't here for now
            global userWeightStored                                 # lets just pretend these aren't here for now
            print(str(calorieOutputSum) + " Calorie Output Sum exerciseTextFieldButtonFunction") # testing
           
            def singleExerciseCalorieCalculator():
                """
                Takes the Entered userWeightStored in pounds, divides by 2.2 to get KG
                Multiplies this against the MET - Metabolic Equivalent of Task
                Then multiplies this against the users entered time (converted into hours)
                to get a total caloric burn for the activity
                """
                global userTimeInHours                                      # lets just pretend these aren't here for now
                global optionSelectedValue                                  # lets just pretend these aren't here for now
                global userWeightStored                                     # lets just pretend these aren't here for now
                global singleExerciseSum                                    # lets just pretend these aren't here for now
                global calorieOutputSum                                     # lets just pretend these aren't here for now
                print(str(userWeightStored) + " userWeightStored")          # testing
                print(str(optionSelectedValue) + " optionSelectedValue")    # testing
                print(str(userTimeInHours) + " userTimeInHours")            # testing
                singleExerciseSum = ((userWeightStored/2.2) * optionSelectedValue) * userTimeInHours # calculates the exercise calorie count based on entered data
                calorieOutputSum += singleExerciseSum                                                # accumulates the overall calories burnt exercising
                print(str(singleExerciseSum) + " Single Exercise Sum")      # testing
                print(str(calorieOutputSum) + " Calorie Output Sum")        # testing
                self.totalCaloriesExercisedField.config(state=NORMAL)       # toggles the field's state while being updated
                self.totalCaloriesExercisedField.setText(int(round(calorieOutputSum)))  # updates the field with the total exercise calorie sum
                self.totalCaloriesExercisedField.config(state=DISABLED)     # toggles the field's state while being updated

            enteredMinutesOfExercise = self.exerciseTextField.get()          # stores the entered exercise minutes in a variable
            self.exerciseTextField.setText("")                               # clears the field once submitted
            userTimeInHours = round(int(enteredMinutesOfExercise) / 60,2)    # preps and stores the entered exercise time in hours
            singleExerciseCalorieCalculator()                                # calls the function for calculating and outputting the exercise total
            
        # Exercise "Add to total" button
        self.singleExerciseSubmitButton = self.addButton(text = "Add to Total", row = 4, column = 5, command = exerciseTextFieldButtonFunction, columnspan=1)
        self.singleExerciseSubmitButton.grid(sticky="e")        # grid positioning and style
        self.singleExerciseSubmitButton["width"] = 20           # sets the buttons width

        # Exercise Names stored in a list for the dropdown menu
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

        # Dictionary containing the exercises and their associated MET value
        exerciseDictionary = {"Aerobics":7.3, "Basketball":6.5, "Bicycling":7.0, "Football":8.0, "Hiking":5.3,\
            "Jogging":7.0, "Jumping Rope":11.8, "Pilates":3.0, "Rowing":8.5, "Running":9.2, "Swimming":5.8, "Tennis":7.3, "Walking":4.8, "Yoga":6.0}
        excerciseDictionaryLength = len(exerciseDictionary) # length of the dictionary stored in a variable for looping

# Function that takes the output text from the options menu, checks it against the keys in the dictionary - then returns the VALUE that matches the KEY
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
        self.exitButton = self.addButton(text = "Exit the Program", row = 0, column = 5, columnspan=2, command = close)
        self.exitButton.grid(sticky="nw")       # grid styling

# dropdown menu
        optionSelected = TkinterVar.StringVar()                                  # Assigns the string data type to the dropdown menu object
        optionSelected.set("Click to Choose")                                    # Sets the initial value of the dropdown text (what appears when its unclicked)
        drop = TkinterVar.OptionMenu(self, optionSelected, *exerciseOptions, command = dropDownItemWasSelected) # builds the dropdown menu
        drop.grid(row = 5, column = 3, sticky = "en", pady = 2, columnspan=2)    # grid settings for the dropdown menu
        drop.config(width = 14, bg="#0069cc", borderwidth=0)                     # style for the dropdown menu
       

# Final Results Button
        def finalWindow():
            global calorieInputSum          # lets just pretend these aren't here for now
            global calorieOutputSum         # lets just pretend these aren't here for now

            newWindow = TkinterVar.Toplevel(self) # creates a new window
            newWindow.geometry("500x250")         # sets the windows dimensions
            newWindow.title("Final Result")       # sets the windows title bar text
            newWindow.grab_set()                  # makes sure the master window cant be interacted with while the results window is open
            
            # Grid for the final window - primarily to ensure the columns are a consistent width
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
            aboveResultsOutput = TkinterVar.Label(newWindow, text="Calories Remaining")             # Final output results
            aboveResultsOutput.grid(row = 4, column = 1, sticky = "", columnspan=1, rowspan=1)
            finalResultsOutput = TkinterVar.Label(newWindow, text="0")                              # Final output results
            finalResultsOutput.grid(row = 4, column = 2, sticky = "", columnspan=1, rowspan=1)

            try: # input validation for testing - so i don't have to enter data to see a version of the final results page
                calorieInputSum
            except NameError:
                calorieInputSum = 0
            finalResultsOutput["text"] = str((int(calorieOutputSum) + 2000) - int(calorieInputSum))

            # Exit Button
            exitButton = TkinterVar.Button(newWindow, text='Close Window', command=newWindow.destroy)   # Exit program button
            exitButton.grid(row = 4, column = 4, sticky = W)                                            # grid positioning for the button

            # Final Results Image
            heartImageContainer = TkinterVar.Label(newWindow, text="")                      # Image label containter created
            self.imageFinale = TkinterVar.PhotoImage(file="heartperson.gif")                # Image set to a variable
            heartImageContainer["image"] = self.imageFinale                                 # Sets the labels image property to the image variable
            heartImageContainer.config(bg="#0069cc", justify="center", width=500)           # Styling for the container
            heartImageContainer.grid(row = 0, column = 0, sticky = "nsew", pady = 2, columnspan=5, rowspan=4) # grid positioning for the container

        # Calculate Total/Final result button - pops up the final results window when pressed
        self.finalWindowButton = self.addButton(text = "Calculate Total", row = 1, column = 2, columnspan=2,command = finalWindow)
        



# Adds all the 4 Meal Calorie boxes together when pressed
    def addsCalorieInput(self):
        """adds the 4 calorie input boxes together"""
        global calorieInputSum                              # lets just pretend these aren't here for now
        calorieInputSum=0                                   # Makes sure the variable is not accumulating
        breakfastNoms = self.breakfastInputField.getText()  # Stores the breakfast calorie information in an easier to read variable
        lunchNoms = self.lunchInputField.getText()          # Stores the lunch calorie information in an easier to read variable
        dinnerNoms = self.dinnerInputField.getText()        # Stores the dinner calorie information in an easier to read variable
        snacksNoms = self.snacksInputField.getText()        # Stores the snacks calorie information in an easier to read variable

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
        calorieInputSum = int(breakfastNoms) + int(lunchNoms) + int(dinnerNoms) + int(snacksNoms) # Adds all the values (integers) from the meal input fields together

        if calorieInputSum != 0:                                    # This changes the button's text so the it is clear what a consecutive press will do
            self.sumOfFoodsButton["text"] = "Press Again to Clear"
        if calorieInputSum == 0:                                    # This is to make it so the button doesn't change text if nothing is entered in any of the boxes
            self.sumOfFoodsButton["text"] = "Add Food Together"
        self.breakfastInputField.setText("")    #
        self.lunchInputField.setText("")        # Clears the fields so the user can tell they successfully submitted
        self.dinnerInputField.setText("")       #
        self.snacksInputField.setText("")       #
        self.totalCaloriesConsumedField.config(state=NORMAL)     # toggles the field's state while updating the text
        self.totalCaloriesConsumedField.setText(calorieInputSum) # sets the banner text to the total sum
        self.totalCaloriesConsumedField.config(state=DISABLED)   # toggles the field's state while updating the text

# Code Below Operates the GUI infinite loop
def main():
    """Instantiate and pop up the window."""
    MAIN_CLASS().mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
            exit(0) # exits the program when 'quit()' is called instead of continually running
    except KeyboardInterrupt:
        print("\nProgram closed.")