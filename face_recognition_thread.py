import sys
from recognise_face import *
import threading
import time
from queue import Queue
from conversation import *



class Example():
    def __init__(self):
        self.method_1()

    def method_1(self):

        def run(self):
            threading.Thread(target = function_a, args = (self,)).start()
            time.sleep(1)
            threading.Thread(target = function_b, args = (self,)).start()

        def function_a(self):
            fn_1()


        def function_b(self):
            fn_2()


        run(self)


        

def fn_1():

    while True :

        
        face_loc=[]
        frm=[]
        sml_frm=[]

        while True:



            if queue1.empty() and queue2.empty() and queue4.empty():
                break


            if not queue1.empty():
                frm = queue1.get()


            if not queue2.empty():
                face_loc = queue2.get()
 

            if not queue4.empty():
                sml_frm = queue4.get()



        name=""
        if len(face_loc)!=0:



            name=face_recognition_fn(sml_frm, face_loc, frm)

            if queue3.full():
                queue3.get()
            queue3.put(name)

            abc=""
            while (abc != "bye" and abc != "off"):
                abc = convo(name)
                
            if queue3.full():
                queue3.get()
            queue3.put("")

            time.sleep(1)

        

            if abc=="off":
                if queue3.full():
                    queue3.get()
                queue3.put("off")  
                sys.exit()             


        else:
            
            print ("No FACE")


            time.sleep(1)



        


        



def fn_2():

    naam=""

    while True:

        frm, sml_frm = pre_process_image()
        face_loc = face_detection(sml_frm)
    
        if queue1.full():
            queue1.get()
        queue1.put(frm)

        if queue2.full():
            queue2.get()

        queue2.put(face_loc)

        if queue4.full():
            queue4.get()
            
        queue4.put(sml_frm)

        
        if not queue3.empty():
            naam = queue3.get()
        
        if naam == "off":
            sys.exit()
            

        display_cam(naam, face_loc, frm)



        
        





queue1 = Queue(maxsize=10)
queue2 = Queue(maxsize=10)
queue3 = Queue(maxsize=10)
queue4 = Queue(maxsize=10)
Example()



