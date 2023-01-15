# %% [markdown]
# ### Part 1: Develop Mortgage Payment Calculator in Python (10 points):
# Consider the calculator at: https://www.myfico.com/credit-education/calculators/loan-savings-calculator/Links to an external site.
# 
# Your goal is to create a similar calculator with same user inputs and stored values (in your code) for interest rates based on credit score
# 
# Assume that customers have a 15 year fixed-interest rate loan with loan term of their choice in Georgia.
# 
# 
# Consider the following user inputs: loan-duration, loan-amount, and FICO score
# Use two separate functions to estimate the monthly and total payment amounts
# 
# here is additional information on how to calculate the monthly payments: https://time.com/nextadvisor/loans/personal-loans/how-to-calculate-loan-payments-and-costs/
# 
# #### myfico calculator provides an idea for these analysis that you have to print.
# (print) an analysis on how much will a customer pay/month and pay/loan-term more/less if their credit score was 50 points higher or 50 points lower
# 
# (print) an analysis on how much will a customer pay more/less and pay/loan-term if they put a 0%, 10%, 20%, 30% down payment (change their loan amount)

# %%
loan_duration = int(input("Enter your loan term: \n"))
                          
#loan_amount = principal                        
loan_amount = int(input("Enter your loan amount: \n"))
                          
FICO_score = int(input("Enter your credit score: \n"))

#Assume that customers have a 15 year fixed-interest rate loan
interest_rate = 15


#monthly payment amount
#Use APR formula = P = A * (r/12)/(1-(1+r/12)**(-n))
monthly_payment_amount = loan_amount * (interest_rate/12)/(1-(1+interest_rate/12) ** (loan_duration))
print("Monthly loan payment amount: $" + str(monthly_payment_amount))

# %%
loan_duration = int(input("Enter your loan term: \n"))
                          
#loan_amount = principal                        
loan_amount = int(input("Enter your loan amount: \n"))
                          
FICO_score = int(input("Enter your credit score: \n"))

#Assume that customers have a 15 year fixed-interest rate loan
interest_rate = 15


#total payment amount
#P = A * (r)/(1-(1+r)**(-n))
total_amount = loan_amount * (interest_rate)/(1-(1+interest_rate) ** (loan_duration))
print("Total loan payment amount: $" + str(total_amount))

# %% [markdown]
# #### how much will a customer pay monthly and pay/loan-term more if their credit score was 50 points higher?

# %%
#Assume that my loan duration on months is 4  
loan_duration = 4
                          
#Assume that my loan is 1000                       
loan_amount = 1000000
                          
#Assume that my credit score is 700 and it's 50 points higher
FICO_score = 700 + 50

#Assume that customers have a 15 year fixed-interest rate loan
interest_rate = 15


#monthly payment amount
monthly_payment_amount = loan_amount * (interest_rate/12)/(1-(1+interest_rate/12) ** (loan_duration))
print("Monthly loan payment amount: $" + str(monthly_payment_amount))

# %%
#pay/loan-term = (Monthly payment * total loan duration)
#we need to get total loan duration from total payment amount
total_amount = loan_amount * (interest_rate)/(1-(1+interest_rate) ** (loan_duration))
print("Total loan payment amount: $" + str(total_amount))

pay_over_loan_term = monthly_payment_amount * loan_duration

# %% [markdown]
# #### how much will a customer pay monthly and pay/loan-term less if their credit score was 50 points lower?

# %%
#Assume that my loan duration on months is 4  
loan_duration = 4
                          
#Assume that my loan is 1000                       
loan_amount = 1000000
                          
#Assume that my credit score is 700 and it's 50 points lower
FICO_score = 700 - 50

#Assume that customers have a 15 year fixed-interest rate loan
interest_rate = 15


#monthly payment amount
monthly_payment_amount = loan_amount * (interest_rate/12)/(1-(1+interest_rate/12) ** (loan_duration))
print("Monthly loan payment amount: $" + str(monthly_payment_amount))

# %%
#total payment amount
total_amount = loan_amount * (interest_rate)/(1-(1+interest_rate) ** (loan_duration))
print("Total loan payment amount: $" + str(total_amount))

# %%
#pay/loan-term = (Monthly payment * total loan duration)
#we need to get total loan duration from total payment amount
pay_over_loan_term = monthly_payment_amount * loan_duration
print("pay/loan_term: $" + str(pay_over_loan_term))

# %% [markdown]
# ### how much will a customer pay more/less and pay/loan-term if they put a 0% down payment?

# %%
#Assume that my loan duration on months is 4  
loan_duration = 4
                          
#Assume that my loan is 1000000                       
loan_amount = 1000000
                          
#Assume that my credit score is 700
FICO_score = 700

#Assume that customers have a 15 year fixed-interest rate loan
interest_rate = 15


#0% down payment is the same as total loan amount 
#we need to get total loan duration from total payment amount
total_amount = loan_amount * (interest_rate)/(1-(1+interest_rate) ** (loan_duration))
print("Total loan payment amount: $" + str(total_amount))


def getTotalPayment(loan_amount, interest_rate, loan_duration):
    return loan_amount * (interest_rate)/(1-(1+interest_rate) ** (loan_duration))
print("total payments for (1000000,15,4): ", total payments for (1000000,15,4))

# %%
#pay/loan-term = (Monthly payment * total loan duration)
#we need to get total loan duration from total payment amount
pay_over_loan_term = monthly_payment_amount * loan_duration
print("pay/loan_term: $" + str(pay_over_loan_term))

# %% [markdown]
# ### how much will a customer pay more/less and pay/loan-term if they put a 10% down payment?

# %%
#Assume that my loan duration on months is 4  
loan_duration = 4
                          
#Assume that my loan is 1000000                       
loan_amount = 1000000
                          
#Assume that my credit score is 700
FICO_score = 700

#Assume that customers have a 15 year fixed-interest rate loan
interest_rate = 15


#10% down payment for monthly payment
def getMonthlyPayment(loan_amount - (loan_amount*0.1), interest_rate, loan_duration):
    return loan_amount * (interest_rate/12)/(1-(1+interest_rate/12) ** (loan_duration))
print("monthly payments for (1000000,15,4): ", total payments for (1000000,15,4))


# %%
#10% down payment for total payment 
def getTotalPayment(loan_amount - (loan_amount*0.1), interest_rate, loan_duration):
    return loan_amount * (interest_rate)/(1-(1+interest_rate) ** (loan_duration))
print("total payments for (1000000,15,4): ", total payments for (1000000,15,4))

# %%
#pay/loan-term = (Monthly payment * total loan duration)
#we need to get total loan duration from total payment amount
pay_over_loan_term = monthly_payment_amount * loan_duration
print("pay/loan_term: $" + str(pay_over_loan_term))

# %% [markdown]
# ### how much will a customer pay more/less and pay/loan-term if they put a 20% down payment?

# %%
#Assume that my loan duration on months is 4  
loan_duration = 4
                          
#Assume that my loan is 1000000                       
loan_amount = 1000000
                          
#Assume that my credit score is 700
FICO_score = 700

#Assume that customers have a 15 year fixed-interest rate loan
interest_rate = 15


#20% down payment for monthly payment
def getMonthlyPayment(loan_amount - (loan_amount*0.2), interest_rate, loan_duration):
    return loan_amount * (interest_rate/12)/(1-(1+interest_rate/12) ** (loan_duration))
print("monthly payments for (1000000,15,4): ", total payments for (1000000,15,4))

# %%
#20% down payment for total payment 
def getTotalPayment(loan_amount - (loan_amount*0.2), interest_rate, loan_duration):
    return loan_amount * (interest_rate)/(1-(1+interest_rate) ** (loan_duration))
print("total payments for (1000000,15,4): ", total payments for (1000000,15,4))

# %%
#pay/loan-term = (Monthly payment * total loan duration)
#we need to get total loan duration from total payment amount
pay_over_loan_term = monthly_payment_amount * loan_duration
print("pay/loan_term: $" + str(pay_over_loan_term))

# %% [markdown]
# ### how much will a customer pay more/less and pay/loan-term if they put a 30% down payment?

# %%
#Assume that my loan duration on months is 4  
loan_duration = 4
                          
#Assume that my loan is 1000000                       
loan_amount = 1000000
                          
#Assume that my credit score is 700
FICO_score = 700

#Assume that customers have a 15 year fixed-interest rate loan
interest_rate = 15


#30% down payment for monthly payment
def getMonthlyPayment(loan_amount - (loan_amount*0.3), interest_rate, loan_duration):
    return loan_amount * (interest_rate/12)/(1-(1+interest_rate/12) ** (loan_duration))
print("monthly payments for (1000000,15,4): ", total payments for (1000000,15,4))

# %%
#30% down payment for total payment 
def getTotalPayment(loan_amount - (loan_amount*0.3), interest_rate, loan_duration):
    return loan_amount * (interest_rate)/(1-(1+interest_rate) ** (loan_duration))
print("total payments for (1000000,15,4): ", total payments for (1000000,15,4))

# %%
#pay/loan-term = (Monthly payment * total loan duration)
#we need to get total loan duration from total payment amount
pay_over_loan_term = monthly_payment_amount * loan_duration
print("pay/loan_term: $" + str(pay_over_loan_term))

# %% [markdown]
# ### Part 2: Create Basal Metabolic Rate (BMR) Calorie Calculator (10 points):
# 
# Use the following calculator and Mifflin-St Jeor equation for reference: https://www.calculator.net/bmr-calculator.htmlLinks to an external site.
# 
# Mifflin-St Jeor Equation for men: BMR = 10W + 6.25H - 5A + 5 
# 
# Mifflin-St Jeor Equation for women: BMR = 10W + 6.25H - 5A - 161 
# 
# Get input form user for gender, age, weight, and height. (let user enter height in inches and weight in lbs)
# Provide (print) a result on how many calories that individual should consume/day and an analysis on what would be the weight if that user consumes 10% more or 10% less calories.
# Use function to estimate the values.

# %%
W = int(input("Enter your weight in lb: \n"))
#convert lb to kg
kg = W * 2.22
print("Weight in kg:", kg)


H = int(input("Enter your height in inches: \n"))
#convert in to cm
cm = H * 2.54
print("Height in cm:", cm)


A = int(input("Enter your age in years: \n"))


G = str(input("Are you male? (y/n)"))
if G == "y":
    G = True
elif G == "n":
    G = False
else:
    print("Error")
    quit()
if G:
    BMR = 10W + 6.25H - 5A + 5
else:
    BMR = 10W + 6.25H - 5A - 161

print("BMR:" + BMR)

# %%
#what would be the weight if that user consumes 10% more or less calories?
#bmr = recommended calorie consumption

if BMR > (BMR+(BMR*0.1)):
    print("Weight:", kg)
else:
    print("Weight:", kg)


