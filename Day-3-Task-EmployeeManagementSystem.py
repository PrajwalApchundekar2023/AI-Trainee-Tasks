# Task - Employee Management System
# classes:
    # Employee()
    # Employee_Manage()
# Main function


class Employee:

    def __init__(self,emp_id,name,contact,post,salary):
        self.emp_id=emp_id;
        self.name=name;
        self.contact=contact;
        self.post=post;
        self.salary=salary;

    def __str__(self):
        return f"Employee-Id:{self.emp_id}\nName:{self.name}\nContact:{self.contact}\nPost:{self.post}\nSalary:{self.salary}"

class Employee_Manage:

    def __init__(self):
        self.employees=[];
        
        
    def add_employee(self,emp_id,name,contact,post,salary):
        new_emp=Employee(emp_id,name,contact,post,salary);
        self.employees.append(new_emp);
        print("Employee Added Successfully..");

    def view_employee(self):
        if not self.employees:
            print("\nNo Employee Found...");
            
        else:
            for emp in self.employees:
                 print(emp)
            

    def update_employee(self,emp_id):
        
        for emp in self.employees:
            if emp.emp_id == emp_id:
                name = input(f"Enter new name (current: {emp.name}): ") or emp.name
                post= input(f"Enter new position (current: {emp.post}): ") or emp.post
                salary = input(f"Enter new salary (current: ${emp.salary}): ") or emp.salary
                emp.name = name;
                emp.post = post;
                emp.salary=salary;
                print("Employee updated successfully......");
                return;

        print("\nEmployee not found...");

    def remove_employee(self,emp_id):

        for emp in self.employees:
            if emp.emp_id== emp_id:

                self.employees.remove(emp);
                print("\nEmployee removed Successsfully...")
                break

        print("\nEmployee not found....");

def main():

    employer= Employee_Manage();
    while True:
        print("\n---------Employee Management System--------")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Remove Employee")
        print("5. Exit");

        choice = input("Enter your choice: ");

        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            contact=input("Enter Employee Contact: ")
            post = input("Enter Employee Position: ")
            salary =input("Enter Employee Salary: ")
            employer.add_employee(emp_id, name,contact,post,salary)

        elif choice == '2':
            employer.view_employee();
            
        elif choice == '3':
            emp_id = input("Enter Employee ID to update: ")
            employer.update_employee(emp_id);
            
        elif choice == '4':
            emp_id = input("Enter Employee ID to remove: ")
            employer.remove_employee(emp_id);
            
        elif choice == '5':
            print("Exiting...");
            break
        else:
            print("Invalid choice, please try again.");
            

if __name__=="__main__":
    main();

    

        
        
                
                

                
        
        

    
        

        
