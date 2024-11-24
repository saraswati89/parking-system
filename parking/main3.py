import dbhelper3




while True:
   print("Enter 1 for create table \n enter 2 for vehicle entry \n enter 3 show all vehicle records  \n enter 4 for vehicle exit" )

   option = int(input("Enter the option:"))


   if option==1:
      dbhelper3.create_query()

   elif option==2:
      dbhelper3.insert_query()

   elif option==3:
      dbhelper3.show_all()  

   elif option==4:
      dbhelper3.exit_parkinglot()

   else:
      print("Print invalid option")
      print("Please Enter again")
