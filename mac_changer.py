
print("                      ")
print("                                 WELCOME TO XO11                ")
print("                      ")
print("   ---------------------------------------------------------------------------")
print("  ----------------------------------------------------------------------------- ")
print("                                                            ")
print("            \\\        //  ||````````````||    //||    //|| ")
print("             \\\      //   ||            ||  //  ||  //  || ")
print("              \\\   //     ||            ||      ||      || ")
print("               \\\//       ||            ||      ||      || ")
print("               //\\\       ||            ||      ||      || ")
print("             //   \\\      ||            ||      ||      || ")
print("           //      \\\     ||            ||      ||      || ")
print("         //         \\\    ||,,,,,,,,,,,,||      ||      || ")
print("                                                                 ")
print(" ------------------------------------------------------------------------------- ")
print("   ---------------------------------------------------------------------------")
print("                                                                 ")
import subprocess
interface=input("Interface >")
new_mac = input("New Mac >")

subprocess.run(["ifconfig",interface,"down"])
subprocess.run(["ifconfig",interface,"hw"," ether",new_mac])
subprocess.run(["ifconfig",interface,"up"])
subprocess.run(["ifconfig"])
