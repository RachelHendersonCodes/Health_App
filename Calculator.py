from Person import Person
from Authenticator import Authenticator

# create person object to reference later
person = Person(0)
authenticator = Authenticator()

# application title
print("Weight Change Predictor")
print()
# application introduction
person.UI_messages("welcome message")
name = input("Please let us know what we should call you:")
# personalize UX by referring to user by name
print("Hey {}! Let's get started. Please fill out the sections below".format(name.capitalize()))
print()
# begin BMR section
person.UI_messages("bmr_intro")
print()
# begin user input to plug into BMR equation
while True:
    age = input("Please insert your age:").replace(" ", "").replace('\t', "")
    good_to_go = authenticator.test_num("age", age) and authenticator.validate_age_range(age)
    age = int(age)
    if good_to_go:
        break
    else:
        continue

# list all permitted user inputs for measurement system
while_loop = False
imperial_or_metric = ""

while not while_loop:
    imperial_or_metric = input("Would you like to calculate in the imperial or metric system?").replace(" ", "").replace(
        '\t', "")
    if imperial_or_metric.lower() == "imperial":
        while_loop = True
        break
    elif imperial_or_metric.lower() == "metric":
        while_loop = True
        break
    else:
        print("Error! Please enter your measurement system")
        continue

while True:
    gender = input("Please indicate your sex by entering either male or female:").replace(" ", "").replace('\t', "")
    gender_good_to_go = authenticator.test_gender(gender)
    if gender_good_to_go:
        break
    else:
        continue

# while while_loop:
#     gender_good_to_go = authenticator.test_gender(gender)
#     if not gender_good_to_go:
#         gender = input("Please indicate your sex by entering either male or female:").replace(" ", "").replace('\t', "")
#         while_loop = True
#         continue
#     else:
#         break

bmr_good_to_go = True
while bmr_good_to_go:

    bmr_array = authenticator.finalize_bmr(imperial_or_metric, age, gender)
    bmr_good_to_go = bmr_array[0]
    person.bmr = bmr_array[1]
    if bmr_good_to_go:
        break
    else:
        continue
# end BMR section

# begin TDEE section
person.UI_messages("tdee_intro")

level_select = person.tdee_select().replace(" ", "").replace('\t', "")
tdee = person.tdee_formula(level_select, person.bmr)

print("")
person.UI_messages("bmi_intro")

print("")
if imperial_or_metric.lower() == "imperial":
    bmi = person.imperial_bmi_formula(bmr_array[2], bmr_array[3], bmr_array[4], name)
elif imperial_or_metric.lower() == "metric":
    bmi = person.metric_bmi_formula(bmr_array[2], bmr_array[3], name)

print("")
person.UI_messages("optional_measurement_intro")

alt_measurement = person.alt_meas_select()

person.alt_formula(alt_measurement)

bai = 0
if imperial_or_metric == "imperial" and alt_measurement == "1":
    bai = person.imperial_bai_calc(bmr_array[3], bmr_array[4])
    person.bai_category(age, gender, bai)
elif imperial_or_metric == "metric" and alt_measurement == "1":
    bai = person.metric_bai_calc(bmr_array[2])
    person.bai_category(age, gender, bai)
elif alt_measurement == "2":
    person.waist_hip_calc(gender)
elif imperial_or_metric == "imperial" and alt_measurement == "3":
    person.imperial_body_fat_calc(bmr_array[2], gender, authenticator)
elif imperial_or_metric == "metric" and alt_measurement == "3":
    person.metric_body_fat_calc(bmr_array[2], gender, authenticator)

goal = person.goal_setting(name)
goal_weight = person.goal_reaching(imperial_or_metric, goal, bmr_array[2], authenticator)
calorie_deficit = 0
calorie_surplus = 0
if goal == "1":
    calorie_deficit = person.goal_cal(goal_weight, bmr_array[2], goal, imperial_or_metric, tdee)
elif goal == "3":
    calorie_surplus = person.goal_cal(goal_weight, bmr_array[2], goal, imperial_or_metric, tdee)
person.macros(goal, calorie_deficit, tdee, calorie_surplus)
