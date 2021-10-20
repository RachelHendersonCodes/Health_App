import time

from Person import Person

person = Person(0)


class Authenticator:

    def __init__(self):
        pass

    @staticmethod
    def test_num(num_option, value):
            try:
                int(value)
            except ValueError:
                print("Error! You need to enter a numeric value for {}.".format(num_option))
                return False
            else:
                return True

    @staticmethod
    def validate_age_range(value):
        age = int(value)
        if 150 > age > 0:
            return True
        else:
            print("That age doesn't seem to be right. Please try entering it again:")
            return False

    @staticmethod
    def test_gender(gender):
        if gender.lower() == "female" or gender.lower() == "male":
            return True
        else:
            return False

    @staticmethod
    def set_height_range(usage, value):
        height_in_feet = int(value)
        height_in_inches = int(value)
        height_in_cm = int(value)
        if (usage == "feet"):
            if (10 > height_in_feet > 0):
                return True
            else:
                return False
        elif (usage == "inches"):
            if (12 > height_in_inches >= 0):
                return True
            else:
                return False
        elif (usage == "cm"):
            if 250 > height_in_cm > 0:
                return True
            else:
                return False

    @staticmethod
    def set_weight_range_lb(value):
        weight = int(value)
        if 2000 > weight > 0:
            return True
        else:
            print("Something doesn't seem right with your weight. Please try entering it again")
            return False

    @staticmethod
    def set_weight_range_kg(value):
        weight = int(value)
        if 908 > weight > 0:
            return True
        else:
            print("Something doesn't seem right with your weight. Please try entering it again")
            return False

    def take_bmr(self, bmr):
        return

    def finalize_bmr(self, measurement_system, age, gender):
        while_loop = False
        if measurement_system == "imperial":
            height_in_feet = input("How many feet tall are you?:").replace(" ", "").replace('\t', "")
            while not while_loop:
                feet_good_to_go = Authenticator.test_num("height_in_feet",
                                                         height_in_feet) and Authenticator.set_height_range(
                    "feet", height_in_feet)
                if not feet_good_to_go:
                    height_in_feet = input("Please enter the correct number of feet to calculate: ").replace(" ",
                                                                                                             "").replace(
                        '\t', "")
                    while_loop = False
                    continue
                else:
                    break
            height_in_feet = int(height_in_feet)
            height_in_inches = input("How many inches are left over?:").replace(" ", "").replace('\t', "")
            while not while_loop:
                inches_good_to_go = Authenticator.test_num("height_in_inches",
                                                           height_in_inches) and Authenticator.set_height_range(
                    "inches", height_in_inches)
                if not inches_good_to_go:
                    height_in_inches = input(
                        "If your height in inches isn't correct, your BMR calculation will be "
                        "off: ").replace(" ", "").replace('\t', "")
                    while_loop = False
                    continue
                else:
                    break
            height_in_inches = int(height_in_inches)
            weight_in_lbs = input("How many pounds do you weigh?").replace(" ", "").replace('\t', "")
            while while_loop == False:
                lbs_good_to_go = Authenticator.test_num("weight_in_lbs",
                                                        weight_in_lbs) and Authenticator.set_weight_range_lb(
                    weight_in_lbs)
                if not lbs_good_to_go:
                    weight_in_lbs = input("Please enter the correct weight in pounds: ").replace(" ", "").replace('\t',
                                                                                                                  "")
                    while_loop = False
                    continue
                else:
                    break
            weight_in_lbs = int(weight_in_lbs)
            calculated_bmr = Person.bmr_formula_imperial(person, weight_in_lbs, height_in_inches,
                                                         height_in_feet, age, gender)
            print("Your BMR is: " + str(calculated_bmr))
            time.sleep(1)
            return [True, calculated_bmr, weight_in_lbs, height_in_feet, height_in_inches]
        elif measurement_system == "metric":
            height_in_cm = input("How many centimeters tall are you?:").replace(" ", "").replace('\t', "")
            while while_loop == False:
                cm_good_to_go = Authenticator.test_num("height_in_cm", height_in_cm) and Authenticator.set_height_range(
                    "cm", height_in_cm)
                if not cm_good_to_go:
                    height_in_cm = input("Please write your correct total height in centimeters: ").replace(" ",
                                                                                                            "").replace(
                        '\t', "")
                    while_loop = False
                    continue
                else:
                    break
            weight_in_kg = input("How many kilograms do you weigh?:").replace(" ", "").replace('\t', "")
            while while_loop == False:
                kg_good_to_go = Authenticator.test_num("weight_in_kg",
                                                       weight_in_kg) and Authenticator.set_weight_range_kg(weight_in_kg)
                if not kg_good_to_go:
                    weight_in_kg = input("Please enter the correct weight in kilograms: ").replace(" ", "").replace(
                        '\t', "")
                    while_loop = False
                    continue
                else:
                    break
            if cm_good_to_go and kg_good_to_go:
                calculated_bmr = Person.bmr_formula_metric(person, int(weight_in_kg), int(height_in_cm), int(age),
                                                           gender)
                print(
                    "your BMR is: " + str(calculated_bmr))
                return [True, calculated_bmr, int(weight_in_kg), int(height_in_cm)]

    def tdee_error(self):
        pass

    @staticmethod
    def set_waist_range_in(value):
        waist = float(value)
        if 15 < waist < 120:
            return True
        else:
            print("Something doesn't seem right with your waist measurement. Please try entering it again")
            return False

    @staticmethod
    def set_waist_range_cm(value):
        waist = float(value)
        if 39 < waist < 305:
            return True
        else:
            print("Something doesn't seem right with your waist measurement. Please try entering it again")
            return False

    @staticmethod
    def set_hip_range_in(value):
        hip = float(value)
        if hip < 95 and hip > 5:
            return True
        else:
            print("Something doesn't seem right with your hip measurement. Please try entering it again")
            return False

    @staticmethod
    def set_hip_range_cm(value):
        hip = float(value)
        if hip < 241 and hip > 13:
            return True
        else:
            print("Something doesn't seem right with your hip measurement. Please try entering it again")
            return False


    @staticmethod
    def set_wrist_range_in(value):
        wrist = float(value)
        if wrist > 0 and wrist < 13:
            return True
        else:
            print("Something doesn't seem right with your wrist measurement. Please try entering it again")
            return False

    @staticmethod
    def set_wrist_range_cm(value):
        wrist = float(value)
        if wrist > 0 and wrist < 33:
            return True
        else:
            print("Something doesn't seem right with your wrist measurement. Please try entering it again")
            return False

    @staticmethod
    def set_forearm_range_in(value):
        forearm = float(value)
        if forearm > 0 and forearm < 20:
            return True
        else:
            print("Something doesn't seem right with your forearm measurement. Please try entering it again")
            return False

    @staticmethod
    def set_forearm_range_cm(value):
        forearm = float(value)
        if forearm > 0 and forearm < 51:
            return True
        else:
            print("Something doesn't seem right with your forearm measurement. Please try entering it again")
            return False

    @staticmethod
    def set_loss_goal_range(measurement_in, weight, goal):
        goal = goal
        weight = int(weight)
        goal = int(goal)
        if measurement_in == "imperial":
            if goal < weight and goal > 80:
                return True
            else:
                print("Something doesn't seem right with your goal weight. Please try entering it again")
                return False
        elif measurement_in == "metric":
            if goal < weight and goal > 36:
                return True
            else:
                print("Something doesn't seem right with your goal weight. Please try entering it again")
                return False

