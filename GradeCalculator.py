class GradeCalculator:

    @staticmethod
    def calculate_grade(percentage):
        percentage_int = int(percentage)
        if percentage_int >= 80 and percentage_int <=100:
            return 'A'
        elif percentage_int >= 70 and percentage_int < 80:
            return 'B+'
        elif percentage_int >=60 and percentage_int < 70:
            return 'B'
        elif percentage_int >= 55 and percentage_int < 60:
            return 'B-'
        elif percentage_int >= 50 and percentage_int < 55:
            return 'C+'
        elif percentage_int >= 40 and percentage_int < 50:
            return 'C'
        elif percentage_int >= 35 and percentage_int < 40:
            return 'D'
        elif percentage_int >= 0 and percentage_int < 35:
            return 'F'
        else:
            raise Exception('Percentage is not a valid value')