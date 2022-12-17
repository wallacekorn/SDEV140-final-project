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
https://www.healthline.com/nutrition/2000-calorie-diet
"""
from breezypythongui import *       # Imports the modules used for the GUI
import tkinter as tk                # Imports the modules used for the GUI
from tkinter import font

calorieOutputSum = 0                # Exercise'd calories overall sum holder
userTimeInHours = 0.0               # Stores the users input time in hours
optionSelectedValue = 0.0           # Assigns a value to the initial key in the dropdown menu
wasNotDigit = False                 # a flag for toggling a label
grandTotalInput = 0                 # final results grand total holder

class MAIN_CLASS(EasyFrame):
    """Main Class - GUI Interface - operates the GUI's infinite loop"""
    def __init__(self):
        """Initializes the GUI interface and displays elements"""
        EasyFrame.__init__(self, title = "Calorie Calculator", width = 620, height = 500, resizable= False, background="#0069cc") # builds the main window

        # Defines the grid sizes for the main window and visually show the working columns
        self.columnconfigure(0, minsize=100)
        self.columnconfigure(1, minsize=100)
        self.columnconfigure(2, minsize=100)
        self.columnconfigure(3, minsize=100)
        self.columnconfigure(4, minsize=100)
        self.columnconfigure(5, minsize=100)
        self.columnconfigure(6, minsize=20)
        self.rowconfigure(0, minsize=5)
        self.rowconfigure(1, minsize=5)
        self.rowconfigure(2, minsize=5)
        self.rowconfigure(3, minsize=5)
        self.rowconfigure(4, minsize=5)
        self.rowconfigure(5, minsize=5)
        self.rowconfigure(6, minsize=5)

        # Headline image
        imageLabel = self.addLabel(text="", row=0, column=2, columnspan =2, rowspan=1, sticky="nsew")   # creates a label container for the image
        self.image = tk.PhotoImage(file="homeveggies.gif") # image in a variable
        imageLabel["image"] = self.image                           # assigns the image variable to the label containter
        imageLabel.grid(sticky="nsew")                             # grid styling
        imageLabel.config(bg="#0069cc")                            # changes the containers background color to match the rest of the app

        # Directions Button and Window
        def jumpToDirections():
            directionsWindow = tk.Toplevel()                    # Creates directions window
            directionsWindow.geometry("500x450")                # sets the windows dimensions
            directionsWindow.title("Directions")                # sets the windows title bar text
            directionsWindow.grab_set()                         # makes sure the master window cant be interacted with while the directions window is open
            directionsWindow.resizable(height = False, width = False)
            directionsWindow.configure( bg="#0069cc") # sets the background color for the window
            
            # Grid for the final window - primarily to ensure the columns are a consistent width and visually show the working columns
            directionsWindow.columnconfigure(0, minsize=10)      # Column 1(0)
            directionsWindow.columnconfigure(1, minsize=480)     # Column 2
            directionsWindow.columnconfigure(2, minsize=10)      # Column 3
            directionsWindow.rowconfigure(0, minsize=10)         # Row 1(0)
            directionsWindow.rowconfigure(1, minsize=380)        # Row 2
            directionsWindow.rowconfigure(2, minsize=50)         # Row 3


            # Directions Content
            directionsHeader = tk.Label(directionsWindow, background="#0069cc", font=('Rockwell Extra Bold', 20), text= "\nDirections")
            directionsHeader.grid(row = 0, column = 1, columnspan=1, rowspan=1, sticky= "n")
            directionsN1 = tk.Label(directionsWindow, anchor=N, background="#0069cc", text="--To Begin--\n1. Input User's Weight in the designated box \n2. 'Lock in' the weight - which unlocks the other buttons \n3. Enter Calorie and Exercise data \n4. Press 'Calculate Total to Display calories remaining \n\nThe resulting number is the total calories  that can be \nconsumed to reach base 0 calorie burn for the day \n A negative number would indicate a weight gain for the day\n\n\n--Calorie Intake--\n1. Enter daily calorie intake for each of the meals \n2. Press the 'Add Food Together' button \n3. The total will display at the top \n4. Press again to Clear \n\n--To Enter Exercise--\n1.Select the exercise activity from the drop-down menu\n2. Enter the number of minutes the activity was performed \n3. Click 'Add to total' to add to the overall exercise total (displayed at top) \n4. Press the 'Clear Total' button to clear the overall exercise calorie total ")
            directionsN1.grid(row = 1, column = 0, columnspan=3, rowspan=1, sticky= "nsew")

            # Exit Button for Directions Window
            exitButtonDirections = tk.Button(directionsWindow, width= 25, text='Close Window', command= directionsWindow.destroy)   # Exit program button
            exitButtonDirections.grid(row = 1, column = 1, sticky="s", pady=(0, 7))                                                # grid positioning for the button





        # The Directions Button Itself
        self.directionsButton = self.addButton(text = "    Directions    ", row = 0, column = 0, command = jumpToDirections, columnspan=2)
        self.directionsButton.grid(sticky="nw", padx=(16, 0))                               # grid styling for the directions button

        # Total boxes
        self.totalCaloriesConsumedField = self.addTextField(text="0", row=1, column=1, columnspan=1, sticky="nsew")
        self.totalCaloriesConsumedField.configure(justify="center", bg="#5289ee", bd=3)
        self.addLabel(text = "Total Consumed", row = 2, column = 1, columnspan=1,background="#0069cc", sticky="wn")
        self.totalCaloriesConsumedField.config(state=DISABLED) # Disables the field so the user can't update directly
        self.totalCaloriesConsumedField.configure({"disabledbackground": "#5289ee", "disabledforeground": "#000000"}) # corrects the colors of the disabled field

        self.addLabel(text = "Total Exercise", row = 2, column = 4, columnspan=1, background="#0069cc", sticky="nw")
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
        self.sumOfFoodsButton.config(state=DISABLED)     # toggles the field's state while being updated


# Calorie Output Fields
        # User Weight field and label
        self.addLabel(text = "User Weight (Lbs)", row = 3, column = 2, columnspan=2,background="#0069cc", sticky="e")
        self.weightTextField = self.addTextField(text="", row=3, column=4, columnspan=1, sticky="w", state="normal", width= 20)
        
        # User Weight Lock-in Button Function
        def userWeightLockIn():
            """button function that 'locks in' the users weight by disabling the input field"""           
            global userWeightStored
            if self.weightTextField.get().isdigit() == False:            # Displays an error label if an integer is not entered in the weight field         
                self.labelVar = self.addLabel(text = "Must be an Integer   ⇓⇓", row = 2, column = 3, columnspan=2, background="red", sticky="news")
                global wasNotDigit
                wasNotDigit = True                                       # A tracker so the 'must be an integer' label can be removed later
            else:
                if wasNotDigit == True:                                  # Removes the 'must be an integer' label if a successful integer is entered
                    self.labelVar.grid_remove()
                userWeightStored = int(self.weightTextField.get())       # Stores the entered information in a global variable
                print(str(userWeightStored) + " userWeightStored")       # Testing

                self.finalWindowButton.config(state=DISABLED)            ##
                self.singleExerciseSubmitButton.config(state=DISABLED)   # Disables the input submit buttons if user weight button is pressed to unlocked
                self.sumOfFoodsButton.config(state=DISABLED)             ## (they are initiated and then immediately disabled to begin with)

                currentFieldState = self.weightTextField["state"]        # stores the field state in a variable for comparison
                if currentFieldState == 'disabled':                      # if current state is disabled, it enables the button on press
                    self.weightTextField.configure(state=NORMAL)
                    self.weightLockIn["text"] = "Lock-In Weight"
                else:                                                    # if current state is normal, disables the button on press
                    self.weightTextField.configure(state=DISABLED)
                    self.weightLockIn["text"] = "Unlock Weight"
                    self.weightLockIn["width"] = 20
                    self.finalWindowButton.config(state=NORMAL)          # Enables the button when user weight is locked in
                    self.singleExerciseSubmitButton.config(state=NORMAL) # Enables the button when user weight is locked in
                    self.sumOfFoodsButton.config(state=NORMAL)           # Enables the button when user weight is locked in

        # The weight lock-in button itself
        self.weightLockIn = self.addButton(text = "Lock-in Weight", row = 3, column = 5, command = userWeightLockIn, columnspan=1)
        self.weightLockIn.grid(sticky="e")
        
        # Exercise text input field and button
        self.addLabel(text = "Exercise (Minutes)", row = 4, column = 2, columnspan=2,background="#0069cc", sticky="e")
        self.exerciseTextField = self.addTextField(text="", row=4, column=4, columnspan=1, sticky="w")

        def exerciseTextFieldButtonFunction():
            """Exercise Text Field Button Function, when the button is pressed this function """
            global userTimeInHours                                  # lets just pretend these aren't here for now
            global optionSelectedValue                              # lets just pretend these aren't here for now
            global userWeightStored                                 # lets just pretend these aren't here for now
            print(str(calorieOutputSum) + " Calorie Output Sum exerciseTextFieldButtonFunction") # testing
           
           
            def singleExerciseCalorieCalculator(): #
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
                print(str(optionSelectedValue) + " Selected MET Value")     # testing
                print(str(userTimeInHours) + " userTimeInHours")            # testing

                singleExerciseSum = ((userWeightStored/2.2) * optionSelectedValue) * userTimeInHours # calculates the exercise calorie count based on entered data
                calorieOutputSum += singleExerciseSum                                                # accumulates the overall calories burnt exercising

                print(str(singleExerciseSum) + " Single Exercise Sum")      # testing
                print(str(calorieOutputSum) + " Total Exercise Sum")        # testing

                self.totalCaloriesExercisedField.config(state=NORMAL)       # toggles the field's state while being updated
                self.totalCaloriesExercisedField.setText(int(round(calorieOutputSum)))  # updates the field with the total exercise calorie sum
                self.totalCaloriesExercisedField.config(state=DISABLED)     # toggles the field's state while being updated

            def timeConverter(enteredMinutesOfExercise):
                if enteredMinutesOfExercise.isdigit() == True:
                    return round(int(enteredMinutesOfExercise) / 60,2)
                else:
                    self.exerciseTextField.setText("")
                    return 0
            enteredMinutesOfExercise = self.exerciseTextField.get()          # stores the entered exercise minutes in a variable
            self.exerciseTextField.setText("")                               # clears the field once submitted
            userTimeInHours = timeConverter(enteredMinutesOfExercise)        # preps and stores the entered exercise time in hours
            singleExerciseCalorieCalculator()                                # calls the function for calculating and outputting the exercise total
            
        # Exercise "Add to total" button
        self.singleExerciseSubmitButton = self.addButton(text = "Add to Total", row = 4, column = 5, command = exerciseTextFieldButtonFunction, columnspan=1)
        self.singleExerciseSubmitButton.grid(sticky="e")        # grid positioning and style
        self.singleExerciseSubmitButton["width"] = 20           # sets the buttons width
        self.singleExerciseSubmitButton.config(state=DISABLED)

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
            for i in exerciseDictionary:                    # iterates over the dictionary to find a match

                if i == optionSelectedVar:                  # if a match is found, it assigns the key's value to a variable
                    
                    optionSelectedValue = exerciseDictionary[optionSelectedVar]

# Exit Program Button - Function and Button
        def close():
            """Closes the Application on execution"""
            self.quit()
        self.exitButton = self.addButton(text = "Exit the Program", row = 0, column = 5, columnspan=2, command = close)
        self.exitButton.grid(sticky="nw")                   # grid styling

# Dropdown menu
        optionSelected = tk.StringVar()                                          # Assigns the string data type to the dropdown menu object
        optionSelected.set("Click to Choose")                                    # Sets the initial value of the dropdown text (what appears when its unclicked)
        drop = tk.OptionMenu(self, optionSelected, *exerciseOptions, command = dropDownItemWasSelected) # builds the dropdown menu
        drop.grid(row = 5, column = 3, sticky = "en", columnspan=2)              # grid settings for the dropdown menu
        drop.config(width = 14, bg="#0069cc", borderwidth=0)                     # style for the dropdown menu
       
# Exercise Clear Button - Function and Button
        def clearButton():
            self.totalCaloriesExercisedField.setText("0") 
        clearButton = self.addButton(text = "Clear Total", row = 5, column = 5, command=clearButton)
        clearButton.grid(sticky = "nw")    # grid settings for the clear button menu

# Final Results Button(Window) - Function and Button
        def finalWindow():
            global calorieInputSum          # lets just pretend these aren't here for now
            global calorieOutputSum         # lets just pretend these aren't here for now

            resultsWindow = tk.Toplevel(self)         # creates a new window
            resultsWindow.geometry("500x250")         # sets the windows dimensions
            resultsWindow.title("Final Result")       # sets the windows title bar text
            resultsWindow.grab_set()                  # makes sure the master window cant be interacted with while the results window is open
            resultsWindow.resizable(height = False, width = False)
            
            # Grid for the final window - primarily to ensure the columns are a consistent width
            resultsWindow.columnconfigure(0, minsize=100)
            resultsWindow.rowconfigure(0, minsize=50)
            resultsWindow.columnconfigure(1, minsize=100)
            resultsWindow.rowconfigure(1, minsize=50)
            resultsWindow.columnconfigure(2, minsize=100)
            resultsWindow.rowconfigure(2, minsize=50)
            resultsWindow.columnconfigure(3, minsize=100)
            resultsWindow.rowconfigure(3, minsize=50)
            resultsWindow.columnconfigure(4, minsize=100)
            resultsWindow.rowconfigure(4, minsize=50)
            
            # Final Results Output
            aboveResultsOutput = tk.Label(resultsWindow, text="Calories Remaining")             # Final output results
            aboveResultsOutput.grid(row = 4, column = 1, sticky = "", columnspan=1, rowspan=1)
            finalResultsOutput = tk.Label(resultsWindow, text="0")                              # Final output results
            finalResultsOutput.grid(row = 4, column = 2, sticky = "", columnspan=1, rowspan=1)

            # input validation and for testing - prevents exception, don't have to enter data to see a version of the final results page
            try: 
                calorieInputSum
            except NameError:
                calorieInputSum = 0
            finalResultsOutput["text"] = str((int(calorieOutputSum) + 2000) - int(calorieInputSum))

            # Exit Button for results window
            exitButton = tk.Button(resultsWindow, text='Close Window', command=resultsWindow.destroy)   # Exit program button
            exitButton.grid(row = 4, column = 4, sticky = W)                                    # grid positioning for the button

            # Final Results Image
            heartImageContainer = tk.Label(resultsWindow, text="")                                      # Image label container created
            self.imageFinale = tk.PhotoImage(file="heartperson.gif")                                # Image set to a variable
            heartImageContainer["image"] = self.imageFinale                                         # Sets the labels image property to the image variable
            heartImageContainer.config(bg="#0069cc", justify="center", width=500)                   # Styling for the container
            heartImageContainer.grid(row = 0, column = 0, sticky = "nsew", columnspan=5, rowspan=4) # grid positioning for the container

        # Calculate Total/Final result button - pops up the final results window when pressed
        self.finalWindowButton = self.addButton(text = "Calculate Total", row = 1, column = 2, columnspan=2,command = finalWindow)
        self.finalWindowButton.config(state=DISABLED) # its initial state should be disabled until weight is locked in

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

        self.breakfastInputField.setText("")                        ##
        self.lunchInputField.setText("")                            # Clears the fields so the user can tell they successfully submitted
        self.dinnerInputField.setText("")                           #
        self.snacksInputField.setText("")                           ##

        self.totalCaloriesConsumedField.config(state=NORMAL)        # Toggles the field's state while updating the text
        self.totalCaloriesConsumedField.setText(calorieInputSum)    # Sets the banner text to the total sum
        self.totalCaloriesConsumedField.config(state=DISABLED)      # Toggles the field's state while updating the text

# Code Below Operates the GUI infinite loop and executes the main program
def main():
    """Instantiate and pop up the window."""
    MAIN_CLASS().mainloop()
if __name__ == "__main__":
    try:
        while True:
            main()
            exit(0) # exits the program when 'quit()' is called instead of continually running a blank shell
    except KeyboardInterrupt:
        print("\nProgram closed.")