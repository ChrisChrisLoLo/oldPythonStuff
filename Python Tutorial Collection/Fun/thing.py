number=0
Running = True
import time

request = input("'1 billion benchmark' v1.0 \nBegin? (y/n)\n")
if request == "y":
    print ("Running...")
    start_time = time.clock()
    while Running:
        if number == 1000000000:
            end_time = time.clock()
            net_time = end_time - start_time
            break
        else:
            number = number + 1
            ##percent = number/10000000000 * 100
            #make percent print less
            ##print ("{0:.2f}% Completed" .format(percent))
    print ("Benchmark complete. The time it took to complete the test is %.3f seconds." %net_time)
    print ("Finished")
    print("Ended.")