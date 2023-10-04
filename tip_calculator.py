# tip_calculator.py

# TODO: Create a function named calculate_tip
try:  #DO NOT MODIFY

    def tip_calculator():
    # TODO:
        # Get these user inputs
        # total_cost (float): The cost of the meal (without tax)
        total_cost = float(input('What is the pre-tax cost of the meal? '))
        num_people = int(input('How many people are splitting the bill? '))
        tip_percentage = float(input('What is the tip percentage? '))
        # num_people (int): The number of people splitting the bill
        # tip_percentage (float): The tip percentage

    
    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
        # Convert to float: The total bill (including tip and sales tax).
        total_bill = total_cost * 1.10 + (total_cost * tip_percentage/100)
        total_bill = float(total_bill)
    # NOTE: Calculate the tip and tax separately. 
     
    # TODO: 
        # Calculate how much each person should pay.
        # Convert to float: The amount each person should pay.   
        cost_per = total_bill / num_people
        cost_per = float(cost_per)
    # TODO:
        # Using an f-string, print two different statements 
        # Total bill: $0.00
        # Each person should pay: $0.00
        print(f'Total bill: ${total_bill:.2f}')
        print(f'Each person should pay: ${cost_per:.2f}')

    # NOTE: The amounts are displayed with 2 decimals only

except: # TODO: modify this except to include a Built-in Exception
       print('input is invalid') # TODO: Print an statement telling the user their input is invalid 
    
    
if __name__ == "__main__": # DO NOT MODIFY
    tip_calculator() # DO NOT MODIFY
