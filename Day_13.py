#Day_13
#Test Evaluator

testName = input("What is the name of the test? ")
maxScore = int(input("What is the maximum score? "))
score = int(input("What is your score? "))
percentage = round(score / maxScore * 100, 2)
grade = ""

if score > maxScore:
  print("Nani sore! ( ◡̀_◡́)ᕤ")
else:
  
  if percentage >= 90:
    grade = "A+"
  if percentage < 90 and percentage >= 80:
    grade = "A"
  if percentage < 80 and percentage >= 70:
    grade = "B"
  if percentage < 70 and percentage >= 60:
    grade = "C"
  if percentage < 60 and percentage >= 50:
    grade = "D"
  if percentage < 50:
    grade = "F"

  print("\n「Name of Exam: ", testName, "\n  Max. Possible Score: ", maxScore, "\n  Your Score: ", score, "\n  Percentage: ", percentage, "%.", "\n  Grade:" , grade + "」")

