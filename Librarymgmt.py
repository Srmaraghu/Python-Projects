class Library:
    def __init__(self,listOfbooks) :
        self.books = listOfbooks

    def display_avail_books(self):
        print("These books present in the library are: ")
        for book in self.books:
            print(f"\t*{book}")
    
    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"Your Book {bookname} has been issued. Please keep it safe and return it within 30 days!")
            self.books.remove(bookname)
            return True
        else:
            print(f"Sorry! {bookname} isn't available ")
            return False

    def returnBook(self,bookname):
        self.books.append(bookname)
        print("Your Book has returned successfully!")
        
        
class Student:
    # def __init__(self):
    #     self.booklist=[]
        
    def requestBook(self):
       self.book =input("Enter the book you wanna borrow: ")
       return self.book
    
    def returnBook(self):
       self.book =input("Enter the book you wanna add/return: ")
       return self.book
        

if __name__=="__main__":
    student=Student()
    centrallibrary= Library(["Algorithms","Django","Python","Clrs"])
    # centrallibrary.display_avail_books()
    welcomeMsg ='''=======Welcome to Library=======
        Please choose an option:
        1.List all the books
        2.Request a book
        3.Donate or Return a book to the library.
        4. Exit the Library'''
    print(welcomeMsg)

    while(True):
        a=int(input("Enter your choice(1,2,3,4): "))
        if a==1:
            centrallibrary.display_avail_books()
        elif a==2:
            centrallibrary.borrowBook(student.requestBook())
        elif a==3:
            centrallibrary.returnBook(student.returnBook())
        elif a==4:
            print("\nThanks for visiting the library. See you soon!")
            exit()
        else:
            print("\nInvalid Choice!")

        
