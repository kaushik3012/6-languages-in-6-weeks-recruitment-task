import sys
import threading
import time
import argparse

# Function to parse arguments
def ArgsParse():    
    parser = argparse.ArgumentParser(description='Help for multithreading.py')      
    parser.add_argument("--th", default=2, type=int, help="Number of Threads")      
    return parser.parse_args()

# Function to increment the global variable
def increment():                     
    global n
    n += 1  

# Function to perform task on the threads
def thread_task(lock):  
    while(time.perf_counter() - start<1):   # Loop until 1 second
        lock.acquire()                        # Acquire the lock
        increment()                          # Increment the global variable
        lock.release()                      # Release the lock

# Driver code
if __name__ == '__main__':
    args = ArgsParse()  # Parse arguments
    
    global n    
    n=0            # Initialize the global variable
    print("\nInitial Value of n: {}".format(n))   

    thread_list = []        # List of threads
    no_Threads = args.th-1      # Number of threads
    lock = threading.Lock()     # Lock for threading

    global start        
    start = time.perf_counter()     # Start time of the program
    
    if no_Threads == 0:     

        # If no. of threads is 0, then only one thread is created
        print("\nNo. of Active Threads: ",threading.active_count())  

        # Loop until 1 second
        while(time.perf_counter() - start<1):   
            increment()     # Increment n

    else:

        # Create threads
        for i in range(no_Threads):     
            # Instantiates the thread and append it to the threads list
            thread_list.append(threading.Thread(target=thread_task, args=(lock,)))  
            
        # Starts all threads
        for thread in thread_list:  
            thread.start()  
                
        print("\nNo. of Active Threads: ",threading.active_count())      # Prints the number of active threads

        # Waits for all threads to complete
        for thread in thread_list:
            thread.join()       

    end = time.perf_counter()       # End time of the program
    print("\nFinal Value of n: ", n)      # Print the final value of n
    print("\nTotal time taken: {} second(s)".format(round(end - start,2)))        # Print the total time taken
    input("\nPress Enter to Exit")
    sys.exit()