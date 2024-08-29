# Define the Student class
class Student:
    # Method to print a greeting message
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
    
    # Method to print the phrase "Pick me!"
    def raise_hand(self):
        print("Pick me!")

# Define the ChattyStudent class, which inherits from Student
class ChattyStudent(Student):
    # Method that overrides the hello() method from Student
    def hello(self):
        # Call the hello() method from the superclass (Student)
        super().hello()
        # Print additional chatty messages
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? "
              "You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    # Method that overrides the raise_hand() method from Student
    def raise_hand(self):
        # Call the raise_hand() method from the superclass (Student) 10 times
        for _ in range(10):
            super().raise_hand()
