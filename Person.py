import time


class Person:

    def __init__(self, bmr):
        self.bmr = bmr

    def UI_messages(self, use):
        if use == "welcome message":
            print(
                "So, you've decided you want to make a change! Whether that's gaining back control of your health,\n"
                "working to build more muscle, or simply just wanting to feel better - it's time.\n"
                ".. and.... you have no idea where to start\n")
            time.sleep(4)
            print("Well, Congratulations! You\'ve found yourself exactly where you need to be.\n"
                "We\'re going to start by learning a little more about you.\n"
                "In the next few sections of this application, you will tell us what we need to know\n"
                "not only to help you accomplish your goals, but so you can make those goals realistic,\n"
                "and, more importantly, so you can learn about your body, too!\n")
        if use == "bmr_intro":
            print(
                "We will begin by calculating your Basal Metabolic Rate, or \"BMR\", using the Mifflin St Jeor equation. \n Your BMR is, essentially, "
                "the number of "
                "calories your body burns throughout the day, without any additional physical activity. "
                "\n Sleeping, eating, and simple tasks you do throughout your day burn calories - even when you're "
                "considered to be at rest!")
        if use == "tdee_intro":
            print("Now that we know how many calories your body burns at rest, we can calculate your \n"
                  "Total Daily Energy Expenditure or \"TDEE\". \n ")
            time.sleep(3)
            print("Your TDEE factors in the calories burned in your unique lifestyle! \n"
                  "By bringing in your daily activity levels, we get a more accurate representation of how many\n "
                  "calories you're burning throughout your day in addition to your BMR! \n")
            time.sleep(4)

        if use == "bmi_intro":
            print(
                "Now that we know a little more about you and your lifestyle, we need to factor in little more "
                "baseline data. \n"
                "We will do this by taking a look at your Body mass index, or \"BMI\" \n")
            time.sleep(4)
            print("Your BMI will not be able to distinguish between weight that derives from muscle and fat.\n What BMI "
                "does, however, is take into account your height and weight and tell you, based solely on these \n"
                "numbers, whether you are in the "
                "\"underweight,\" \"healthy weight\", \"overweight\" or \"obese\" category.\n")
            time.sleep(5)
            print("These categories are not always truly defining of your health and shouldn't be your main focus,\n"
                "as all measures of body composition are imperfect.\n")
            time.sleep(4)
            print("While BMI is a traditional and well spread-system for the measurement of one's health, it's not a "
                "perfect formula. \n"
                "In fact, it's becoming increasingly more popular to rely on a *variety* of measurements for an overall "
                "assessment of one's health.\n")
            time.sleep(5)
            print("We are going to calculate your BMI and for the reasons explained above, we highly "
                "recommend you fill out at least one other method \n to give us a more accurate idea of which "
                "category you truly "
                "fall into.\n While it's not required, it will help us later on when it comes time for goal setting "
                "and tracking your achievements.")
            input("Press enter to view your BMI: ")
        if use == "optional_measurement_intro":
            print("Please remember that BMI doesn't have the ability to factor in the weight coming from body fat "
                  "versus muscle. \n"
                  "Below, you will have the option to pick from one of the following alternative methods for "
                  "calculating your health category. \n All of these categories, like BMI, will place you in "
                  "a health category based on the data you enter. \n")

    #Mifflin St Jeor equation
    def bmr_formula_imperial(self, weight_in_lbs, height_in_inches, height_in_feet, age, gender):
        imperial_height = (height_in_feet * 12) + height_in_inches
        if gender.lower() == "female":
            bmr = (4.536 * weight_in_lbs) + (15.88 * imperial_height) - (5 * age) - 161
            return int(bmr)
        elif gender.lower() == "male":
            bmr = (4.536 * float(weight_in_lbs)) + (15.88 * float(imperial_height)) - (5 * age) + 5
            return int(bmr)

    def bmr_formula_metric(self, weight_in_kg, height_in_cm, age, gender):
        if gender.lower() == "female":
            bmr = (10 * weight_in_kg) + (6.25 * height_in_cm) - (5 * age) - 161
            return int(bmr)
        elif gender.lower() == "male":
            bmr = (10 * weight_in_kg) + (6.25 * height_in_cm) - (5 * age) + 5
            return int(bmr)

    @staticmethod
    def tdee_select():
        print("[1] Sedentary - Little to no exercise or daily activity at work (desk job)\n"
              "[2] Lightly Active - Light Exercise such as walking 1-3 days a week\n"
              "[3] Moderately Active - Moderate Exercise 3-5 days a week\n"
              "[4] Very Active - Heavy Exercise 6 days a week\n"
              "[5] Extremely Active - Very Heavy Exercise and a hard labor job\n")
        activity_level = input("Please enter the number assigned to the activity level of your current lifestyle: ")
        return activity_level

    def tdee_formula(self, activity_level, bmr):
        tdee = ""
        while_loop = True
        while while_loop == True:
            if activity_level == "1":
                tdee = bmr * 1.2
                break
            elif activity_level == "2":
                tdee = bmr * 1.375
                break
            elif activity_level == "3":
                tdee = bmr * 1.55
                break
            elif activity_level == "4":
                tdee = bmr * 1.725
                break
            elif activity_level == "5":
                tdee = bmr * 1.9
                break
            else:
                activity_level = input("Error! Please select your activity level based on the numbers above: ").replace(
                    " ", "").replace('\t', "")
                while_loop = True
                continue
        tdee = int(tdee)
        print(
            "According to the data you entered, your TDEE is {}, meaning you burn {} calories each day. This is a great starting "
            "point.".format(
                tdee, tdee))
        input("Once you've reviewed your TDEE, press enter to learn about BMI. ")
        return tdee

    @staticmethod
    def imperial_bmi_formula(weight_in_lbs, height_in_feet, height_in_inches, name):
        imperial_height = (height_in_feet * 12) + height_in_inches
        bmi = (703 * weight_in_lbs) / (imperial_height * imperial_height)
        bmi = bmi.__round__()
        print("{}, based on the height and weight you previously entered, your BMI is ".format(name) + str(bmi))
        if bmi < 18.5:
            print("A BMI of {} places in the  underweight range.".format(bmi))
        elif 18.5 <= bmi <= 24.9:
            print("A BMI of {} places you in the healthy weight range.".format(bmi))
        elif 25 <= bmi <= 29.9:
            print("A BMI if {} places you in the overweight range".format(bmi))
        elif 30 <= bmi <= 39.9:
            print("A BMI of {} places you in the obese range")
        return bmi

    @staticmethod
    def metric_bmi_formula(weight_in_kg, height_in_cm, name):
        bmi = weight_in_kg / (height_in_cm * height_in_cm)
        bmi = bmi.__round__()
        print("{} based on the height and weight you previously entered, your BMI is: ".format(name.capitalize()) + str(bmi))
        if bmi < 18.5:
            print("A BMI of {} places in the  underweight range.".format(bmi))
        elif 18.5 <= bmi <= 24.9:
            print("A BMI of {} places you in the healthy weight range.".format(bmi))
        elif 25 <= bmi <= 29.9:
            print("A BMI if {} places you in the overweight range".format(bmi))
        elif 30 <= bmi <= 39.9:
            print("A BMI of {} places you in the obese range")
        return bmi

    def alt_meas_select(self):
        input("Please press enter to view your options.")
        print("[1] Body Adiposity Index (BAI): Rather than using your weight to calculate your health category, \n"
              "BAI estimates your body fat percentage by taking into account your hip circumference and height. \n"
              "BAI's intention is to define total body mass made only of fat tissues.\n"
              "This method will provide you with an estimated percentage value of body fat.\n"
              "You will need a measuring tape for this.\n"
              "[2] Waist to Height Ratio: This indicator of health takes into account your height and waist "
              "circumference,\n providing an estimated ratio and is used as an indicator of centralized "
              "obesity and cardiometabolic risk. \n By measuring your waist, it provides a measure of the "
              "distribution of body fat. \n The higher the ratio, the higher risk of obesity-related diseases "
              "associated with abdominal obesity. Inherently biased for people shorter or taller than the average "
              "population. \n"
              "You will need a measuring tape for this.\n"
              "[3] Body Fat Percentage and Lean body Mass Calculator (Boer Formula): A combination of two calculations "
              "to offer an estimate of what your body would weigh if \n "
              "it didn't have any body fat; therefore helping factor in weight coming from muscle. \n "
              "Begins by calculating body fat percentage based on measurements from multiple points on your body. \n"
              "You will need a tape measure for this.\n")
        alt_measurement = input("Please enter the number for which alternative measurement you'd like to use, "
                                "if you just want to move forward with only BMI, please enter 0: ")
        return alt_measurement

    def alt_formula(self, alt_measurement):
        if alt_measurement == "1":
            print(
                "You've selected the Body Adiposty Index(BAI). To calculate your BAI, you will need to measure your"
                "hip circumference. \n Be sure you place your tape measure around your hips, so it goes "
                "through the rise of the buttocks, viewed from the side.")
        elif alt_measurement == "2":
            print("You've selected the Weight to Height Ratio. \nTo calculate this, you will need to measure both your"
                  "waist and hip circumference. When measuring your waist circumference, you will need to place the"
                  "measuring tape\n at the natural waist, just above the belly button and beneath"
                  "the last rib.\n Hip circumference should be measured around the widest part of the buttocks.\n"
                  "Research suggests that people who carry more weight in their waists than in their hips can be "
                  "more susceptible to certain diseases, such as: diabetes, asthma, and alzheimer's.\n"
                  "Your waist to hip ratio will provide a health assessment based on low to high health risk.")
        elif alt_measurement == "3":
            print("You've selected the Body Fat Percentage Calculator. \n You will need to measure your"
                  "waist and hip circumference. \n Women will also need to measure their wrist and forearm. \n"
                  "When measuring your waist circumference, you will need to place the"
                  "measuring tape\n at the natural waist, just above the belly button and beneath"
                  "the last rib.\n Hip circumference should be measured around the widest part of the buttocks.\n")
        return alt_measurement

    def imperial_bai_calc(self, height_in_feet, height_in_inches):
        hip_circumference = input("Please enter your hip circumference in inches: ")
        while not hip_circumference == float:
            try:
                hip_circumference = float(hip_circumference)
            except ValueError:
                hip_circumference = input(
                    "Your hip circumference needs to be a number. Please enter your hip circumference in inches: ")
                continue
            break
        hip_circumference = hip_circumference * 2.54  # convert hip_circumference to centimeters
        imperial_height = (height_in_feet * 12) + height_in_inches
        m_height = imperial_height / 39.37  # convert imperial_height to meters
        bai = hip_circumference / (m_height ** 1.5) - 18
        bai = round(bai)
        print("According to your height and hip circumference, your bai is {}%".format(bai))
        print("")
        return bai

    def metric_bai_calc(self, height_in_cm):
        hip_circumference = input("Please enter your hip circumference in centimeters: ")
        while hip_circumference is not float:
            try:
                hip_circumference = float(hip_circumference)
            except ValueError:
                hip_circumference = input(
                    "Your hip circumference needs to be a number. Please enter your hip circumference in inches: ")
                continue
            break
        height = height_in_cm / 100  # convert height to meters
        bai = (hip_circumference / (height ** 1.5)) - 18
        bai = round(bai)
        print(bai)
        return bai

    def bai_category(self, age, gender, bai):
        age = int(age)
        gender = gender.lower()
        bai = bai
        if gender == "female":
            if age <= 39:
                if bai < 21:
                    print("A BAI of {}% places you in the underweight category".format(bai))
                elif 21 <= bai <= 33:
                    print("A BAI of {}% places you in the healthy weight category".format(bai))
                elif 33 < bai <= 39:
                    print("A BAI of {}% places you in the overweight category".format(bai))
                elif bai > 39:
                    print("A BAI of {}% places you in the obese weight category".format(bai))
            elif 40 < age <= 59:
                if bai < 23:
                    print("A BAI of {}% places you in the underweight category".format(bai))
                elif 23 <= bai <= 35:
                    print("A BAI of {}% places you in the healthy weight category".format(bai))
                elif 35 < bai < 41:
                    print("A BAI of {}% places you in the overweight category".format(bai))
                elif bai > 41:
                    print("A BAI of {}% places you in the obese weight category".format(bai))
            elif age >= 60:
                if bai < 25:
                    print("A BAI of {}% places you in the underweight category".format(bai))
                elif 25 <= bai <= 38:
                    print("A BAI of {}% places you in the healthy weight category".format(bai))
                elif 38 < bai <= 43:
                    print("A BAI of {}% places you in the overweight category".format(bai))
                elif bai > 43:
                    print("A BAI of {}% places you in the obese weight category.".format(bai))
        elif gender == "male":
            if age <= 39:
                if bai < 8:
                    print("A BAI of {}% places you in the underweight category.".format(bai))
                elif 8 <= bai <= 21:
                    print("A BAI of {}% places you in the healthy weight category.".format(bai))
                elif 21 < bai <= 26:
                    print("A BAI of {}% places you in the overweight category.".format(bai))
                elif bai > 26:
                    print("A BAI of {}% places you in the obese weight category.".format(bai))
            elif 40 <= age < 59:
                if bai < 11:
                    print("A BAI of {}% places you in the underweight category.".format(bai))
                elif 11 <= bai <= 23:
                    print("A BAI of {}% places you in the healthy weight category.".format(bai))
                elif 23 < bai <= 29:
                    print("A BAI of {}% places you in the overweight category.".format(bai))
                elif bai > 29:
                    print("A BAI of {}% places you in the obese weight category.".format(bai))
            elif age >= 60:
                if bai < 13:
                    print("A BAI of {}% places you in the underweight category.".format(bai))
                elif 13 <= bai <= 25:
                    print("A BAI of {}% places you in the healthy weight category".format(bai))
                elif 25 < bai <= 31:
                    print("A BAI of {}% places you in the overweight category".format(bai))
                elif bai > 31:
                    print("A BAI of {}% places you in the obese weight category".format(bai))

    def waist_hip_calc(self, gender):
        waist = input("Please input your waist measurement in either inches or centimeters: ")
        while not waist == float:
            try:
                waist = float(waist)
            except ValueError:
                waist = input(
                    "Your waist measurement needs to be a number. Please enter your waist circumference in inches: ")
                continue
            break
        hip = input("Please input your hip measurement in either inches or centimeters: ")
        while not hip == float:
            try:
                hip = float(hip)
            except ValueError:
                hip = input(
                    "Your hip measurement needs to be a number. Please enter your hip circumference in inches: ")
                continue
            break
        ratio = waist / hip
        print(ratio)
        if gender == "female":
            if ratio <= .80:
                print("Based on your haist to hip ratio, your health risk low.")
            elif ratio > .80 and ratio <= .85:
                print("Based on your waist to hip ratio, your health risk moderate.")
            elif ratio > .86:
                print("Based on your waist to hip ratio, your health risk is high.")
        elif gender == "male":
            if ratio <= .95:
                print("Based on your waist to hip ratio, your health risk is low.")
            elif ratio > .95 and ratio <= 1.0:
                print("Based on your waist to hip ratio, your health risk is moderate.")
            elif ratio > 1.0:
                print("Based on your waist to hip ratio, your health risk is high.")
        return ratio

    def imperial_body_fat_calc(self, weight, gender, authenticator):
        while_loop = False
        weight = weight
        gender = gender.lower()
        waist = input("Please enter your waist circumference in inches: ")
        while while_loop == False:
            waist_good_to_go = authenticator.test_num("waist", waist) and authenticator.set_waist_range_in(waist)
            if not waist_good_to_go:
                waist = input("Please enter the correct waist measurement in inches: ")
                while_loop = False
                continue
            else:
                break
        waist = float(waist)
        hip = input("Please enter your hip circumference in inches: ")
        while while_loop == False:
            hip_good_to_go = authenticator.test_num("hip", hip) and authenticator.set_hip_range_in(hip)
            if not hip_good_to_go:
                hip = input("Please enter the correct hip measurement in inches: ")
                while_loop = False
                continue
            else:
                break
        hip = float(hip)
        if gender == "female":
            wrist = input("Please enter your wrist size in inches: ")
            while while_loop == False:
                wrist_good_to_go = authenticator.test_num("wrist", wrist) and authenticator.set_wrist_range_in(wrist)
                if not wrist_good_to_go:
                    wrist = input("Please enter the correct wrist measurement in inches: ")
                    while_loop = False
                    continue
                else:
                    break
            wrist = float(wrist)
            forearm = input("Please enter your hip circumference in inches: ")
            while while_loop == False:
                forearm = authenticator.test_num("forearm", forearm)
                forearm_good_to_go = authenticator.set_forearm_range_in(forearm)
                if not forearm_good_to_go:
                    forearm = input("Please enter the correct forearm measurement in inches: ")
                    while_loop = False
                    continue
                else:
                    break
            forearm = float(forearm)
            lean_body_mass = round((weight * .732) + 8.987 + wrist / 3.140 - waist * .157 - hip * .249 + forearm * .434)
            print("Your lean body mass is {} pounds.".format(lean_body_mass))
            body_fat_weight = round(weight - lean_body_mass)
            print("Your body fat weight is {} pounds.".format(body_fat_weight))
            body_fat_percentage = round((body_fat_weight / weight) * 100)
            print("Meaning, your body fat percentage is {}%".format(body_fat_percentage))
        elif gender == "male":
            lean_body_mass = round((weight * 1.082) + 94.42 - (waist * 4.15))
            print("Your lean body mass is {} pounds.".format(lean_body_mass))
            body_fat_weight = round(weight - lean_body_mass)
            print("Your body fat weight is {} pounds.".format(body_fat_weight))
            body_fat_percentage = round((body_fat_weight / weight) * 100)
            print("Meaning, your body fat percentage is {}%".format(body_fat_percentage))

    def metric_body_fat_calc(self, weight_in_kg, gender, authenticator):
        while_loop = False
        weight_in_kg = weight_in_kg
        weight = weight_in_kg * 2.20462  # convert to lbs for the formula to work correctly.
        gender = gender.lower()
        waist = input("Please enter your waist circumference in centimeters: ")
        while while_loop == False:
            waist_good_to_go = authenticator.test_num("waist", waist) and authenticator.set_waist_range_cm(waist)
            if not waist_good_to_go:
                waist = input("Please enter the correct waist measurement in centimeters: ")
                while_loop = False
                continue
            else:
                break
        waist = float(waist)
        waist_in = waist * 2.54  # convert centimeters to inches for formula
        hip = input("Please enter your hip circumference in centimeters: ")
        while while_loop == False:
            hip_good_to_go = authenticator.test_num("hip", hip) and authenticator.set_hip_range_cm(hip)
            if not hip_good_to_go:
                hip = input("Please enter the correct hip measurement in centimeters: ")
                while_loop = False
                continue
            else:
                break
        hip = float(hip)
        hip_in = hip * 2.54  # convert centimeters to inches
        if gender == "female":
            wrist = input("Please enter your wrist size in centimeters: ")
            while while_loop == False:
                wrist_good_to_go = authenticator.test_num("wrist", wrist) and authenticator.set_wrist_range_cm(wrist)
                if not wrist_good_to_go:
                    wrist = input("Please enter the correct wrist measurement in inches: ")
                    while_loop = False
                    continue
                else:
                    break
            wrist = float(wrist)
            wrist_in = wrist * 2.54  # convert centimeters to inches
            forearm = input("Please enter your hip circumference in centimeters: ")
            while while_loop == False:
                forearm = authenticator.test_num("forearm", forearm)
                forearm_good_to_go = authenticator.set_forearm_range_cm(forearm)
                if not forearm_good_to_go:
                    forearm = input("Please enter the correct forearm measurement in inches: ")
                    while_loop = False
                    continue
                else:
                    break
            forearm = float(forearm)
            forearm_in = forearm * 2.54  # convert centimeters to inches
            lean_body_mass = round(
                (weight * .732) + 8.987 + wrist_in / 3.140 - waist_in * .157 - hip_in * .249 + forearm_in * .434)
            print("Your lean body mass is {} pounds.".format(lean_body_mass))
            body_fat_weight = round(weight - lean_body_mass)
            print("Your body fat weight is {} pounds.".format(body_fat_weight))
            body_fat_percentage = round((body_fat_weight / weight) * 100)
            print("Meaning, your body fat percentage is {}%".format(body_fat_percentage))
        elif gender == "male":
            lean_body_mass = round((weight * 1.082) + 94.42 - (waist_in * 4.15))
            print("Your lean body mass is {} pounds.".format(lean_body_mass))
            body_fat_weight = round(weight - lean_body_mass)
            print("Your body fat weight is {} pounds.".format(body_fat_weight))
            body_fat_percentage = round((body_fat_weight / weight) * 100)
            print("Meaning, your body fat percentage is {}%".format(body_fat_percentage))

    def goal_setting(self, name):
        print("This is where it gets fun, {}! Now's the time for you to set your current \n"
              "body composition goals. You can use what you've learned about your body from this \n"
              "application to help you make a choice. Your selection here will effect \n"
              "our recommended calorie intake and calorie outtake moving forward.".format(name.capitalize()))
        print("[1] Goal: Lose weight. In a caloric deficit, your body will burn excess body fat\n"
              "you will likely also lose some muscle mass, which can be rebuilt once the desired\n"
              "body fat is met.\n"
              "[2] Goal: Maintain weight. Being in a caloric maintenance will keep both your current\n"
              "body fat and current muscle mass in tact.\n"
              "[3] Goal: Gain weight. In a caloric surplus, your body will gain both body fat\n"
              "and build muscle mass.")
        goal = input("Please enter the number assigned to the goal you'd like to set for yourself: ")
        return goal

    @staticmethod
    def goal_reaching(measurement_in, goal, weight, authenticator):
        weight = weight
        goal_weight = ""
        if measurement_in == "imperial":
            goal_weight = input("Please enter your goal weight in pounds: ")
        elif measurement_in == "metric":
            goal_weight = input("Please enter your goal weight in kilograms: ")
        while_loop = False
        authenticator.test_num("goal_weight", goal_weight)
        goal_weight = int(goal_weight)
        loss_goal_good_to_go = authenticator.set_loss_goal_range(measurement_in, weight, goal_weight)
        maint_goal_good_to_go = goal_weight == weight
        gain_goal_good_to_go = goal_weight > weight
        while while_loop == False:
            if goal == "1" and not loss_goal_good_to_go:
                while_loop = False
                goal_weight = input("Please enter a weight loss goal for yourself: ")
                loss_goal_good_to_go = authenticator.set_loss_goal_range(measurement_in, weight, goal_weight)
                continue
            elif goal == "1" and loss_goal_good_to_go:
                print("Congratulations! You've just set a weight loss goal for yourself!\n")
                break
            elif goal == "2" and not maint_goal_good_to_go:
                while_loop = False
                goal_weight = input("Please enter a weight maintenance goal for yourself: ")
                continue
            elif goal == "2" and maint_goal_good_to_go:
                print("Congratulations! You've just set a maintenance goal for yourself!")
                break
            elif goal == "3" and not gain_goal_good_to_go:
                while_loop = False
                goal_weight = input("Please enter a weight gain goal: ")
                continue
            elif goal == "3" and gain_goal_good_to_go:
                print("Congratulations! You've just set a weight gain goal for yourself!")
                break
        return goal_weight

    def goal_cal(self, goal_weight, weight, goal, measurement_in, tdee):
        import datetime
        if goal == "1":  # weightlossgoal
            loss = int(weight) - int(goal_weight)
            calorie_deficit = tdee * .15
            calorie_deficit = tdee - calorie_deficit
            num_weeks = round(loss / 1.5)
            goal_date = datetime.date.today() + datetime.timedelta(weeks=num_weeks)
            if measurement_in == "imperial":
                goal_date = goal_date.__format__('%m/%d/%Y')
                print("In order to lose {} pounds and reach your goal weight of {}, your recommended daily calorie "
                      "intake is {} calories. \n "
                      "If you follow this plan, you will reach your goal in {} weeks from now, on {}.".format(loss,
                                                                                                              goal_weight,
                                                                                                              calorie_deficit,
                                                                                                              num_weeks,
                                                                                                              goal_date))
                return calorie_deficit
            elif measurement_in == "metric":
                goal_date = goal_date.__format__('%d/%m/%Y')
                print("In order to lose {} kilograms and reach your goal weight of {}, your recommended daily calorie "
                      "intake is {} calories. \n "
                      "If you follow this plan, you will reach your goal in {} weeks from now, on {}.".format(loss,
                                                                                                              goal_weight,
                                                                                                              calorie_deficit,
                                                                                                              num_weeks,
                                                                                                              goal_date))
                return calorie_deficit
        elif goal == "2":  # maintenancegoal
            print(
                "In order to maintain your current weight, your daily calorie intake, if you aren't going to be "
                "making\n "
                "adjustments to your level of physical activity, is {}.".format(tdee))
        elif goal == "3":  # gaingoal
            gain = goal_weight - weight
            calorie_surplus = tdee + 500
            num_weeks = round(gain / 1.5)
            goal_date = datetime.date.today() + datetime.timedelta(weeks=num_weeks)
            if measurement_in == "imperial":
                goal_date = goal_date.__format__('%m/%d/%Y')
                print("In order to gain {} pounds and reach your goal weight of {}, your recommended daily calorie "
                      "intake is {} calories. \n "
                      "If you follow this plan, you will reach your goal {} weeks from now, on {}.".format(gain,
                                                                                                           goal_weight,
                                                                                                           calorie_surplus,
                                                                                                           num_weeks,
                                                                                                           goal_date))
                return calorie_surplus
            elif measurement_in == "metric":
                goal_date = goal_date.format('%d,%m,%Y')
                print("In order to gain {} kilograms and reach your goal weight of {}, your recommended daily calorie "
                      "intake is {} calories. \n "
                      "If you follow this plan, you will reach your goal {} weeks from now, on {}.".format(gain,
                                                                                                           goal_weight,
                                                                                                           calorie_surplus,
                                                                                                           num_weeks,
                                                                                                           goal_date))
                return calorie_surplus

    @staticmethod
    def macros(goal, calorie_deficit, tdee, calorie_surplus):
        if goal == "1":
            protein = calorie_deficit * .30
            protein = round(protein / 4)
            carbs = calorie_deficit * .35
            carbs = round(carbs / 4)
            fat = calorie_deficit * .35
            fat = round(fat / 9)
            print(
                "Your recommended daily macro allotment is {} grams of protein, {} grams of carbs, and {} grams of fat".format(
                    protein, carbs, fat))
        elif goal == "2":
            protein = tdee * .30
            protein = round(protein / 4)
            carbs = tdee * .35
            carbs = round(carbs / 4)
            fat = tdee * .35
            fat = round(fat / 9)
            print("Your recommended daily macro allotment is {} grams of protein, {} grams of carbs, and {} grams of "
                  "fat".format(protein, carbs, fat))
        elif goal == "3":
            protein = calorie_surplus * .30
            protein = round(protein / 4)
            carbs = calorie_surplus * .35
            carbs = round(carbs / 4)
            fat = calorie_surplus * .35
            fat = round(fat / 9)
            print("Your recommended daily macro allotment is {} grams of protein, {} grams of carbs, and {} grams of "
                  "fat".format(protein, carbs, fat))
