#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.vehicle import  Vehicle
from models.category import Category
from models.car_model import CarModel
from models.car_make import CarMake
from models.car_document import Document



all_classes = {"BaseModel": BaseModel, "User": User, "Vehicle": Vehicle, "Category":Category, "CarModel": CarModel, "CarMake":CarMake, "Document": Document}
stored_obj = storage.all()

class RegexpressCommand(cmd.Cmd): 

    prompt = "regexpressApi: "
    def do_create(self, line):
        args = line.split(" ")

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in all_classes.keys():
            print("** class doesn't exist **")   
        else:
            other_argument = args[1:]
            obj_arg ={}
            for argu in other_argument:
                new_argu = argu.split("=")
               
                if new_argu[1][0] == '\"' and new_argu[1][-1] == '\"':
                    new_argu[1] = new_argu[1].replace('_',' ')
                    obj_arg[new_argu[0]] = new_argu[1].replace('"','')
                elif "." in list(new_argu[1]):
                    obj_arg[new_argu[0]] = float(new_argu[1])
                else:
                    obj_arg[new_argu[0]] = int(new_argu[1])
            



            new_class = all_classes[args[0]](**obj_arg)
            new_class.save()
            print(new_class.id)

#create Document name="vehicle_license" Description="love it" category_id=70f6c337-cd7d-438b-8f7d-da16a1b66dd5 cost_price=50 selling_price=60


        
    def do_show(self, line):
        args = line.split(" ")

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in all_classes.keys():
            print("** class doesn't exist **") 

        elif len(args) != 2:
            print("** instance id missing **")

        else:
            class_name = args[0]
            instance_id = args[1]
            obj_id = f"{class_name}.{instance_id}"
            

            if obj_id not in stored_obj.keys():
                print("** no instance found **")
            else:
                print(stored_obj[obj_id])

    def do_destroy(self, line):
        args = line.split(" ")

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in all_classes.keys():
            print("** class doesn't exist **") 

        elif len(args) != 2:
            print("** instance id missing **")

        else:
            class_name = args[0]
            instance_id = args[1]
            obj_id = f"{class_name}.{instance_id}"
            

            if obj_id not in stored_obj.keys():
                print("** no instance found **")
            else:
                del stored_obj[obj_id]
                storage.save()

    def do_all(self, line):
        args = line.split(" ")

        if len(args) == 1 and args[0] != "":
            if args[0] not in all_classes:
                 print("** class doesn't exist **")
            else:
                for each in stored_obj.values():
                    if args[0] == each.__class__.__name__:
                        print(each)
        else:
            for each in stored_obj.values():
                        print(each)
        

    def do_stall(self, line):
        obj = storage.all(line)
        for ob, value in obj.items():
            print(value.to_dict())
        print("stall")
        

        
    def do_update(self, line):
        args = line.split(" ")
        

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in all_classes.keys():
            print("** class doesn't exist **") 

        elif len(args) <= 1:
            print("** instance id missing **")

        elif len(args) <= 2:
            print("** attribute name missing **")

        elif len(args) <= 3:
            print("** value missing **")

        
        else:
            class_name = args[0]
            instance_id = args[1]
            obj_id = f"{class_name}.{instance_id}"
            

            if obj_id not in stored_obj.keys():
                print("** no instance found **")

            else:
                for each in stored_obj.values():
                        if each.id ==  instance_id:
                            showed_class = each
                new_obj = showed_class

                setattr(new_obj, args[2], args[3].replace('"', ''))
                new_obj.save()
                print(new_obj)
        



    
    def do_EOF(self, line):
        return True
    
    def do_quit(self, line):
        return True
    


if __name__ == '__main__':
    try:
        RegexpressCommand().cmdloop()

    except KeyboardInterrupt:
        print("")
    
