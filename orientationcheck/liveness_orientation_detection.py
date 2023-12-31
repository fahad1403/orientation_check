import cv2
import f_liveness_detection
import cv2
import imutils
import time
import random

def challenge_result(question, orientation):
    if question == "turn face right":
        if orientation and len(orientation) == 0:
            challenge = "fail"
        elif orientation and orientation[0] == "right": 
            challenge = "pass"
        else:
            challenge = "fail"

    if question == "turn face left":
        if orientation and len(orientation) == 0:
            challenge = "fail"
        elif orientation and orientation[0] == "left": 
            challenge = "pass"
        else:
            challenge = "fail"

    return challenge

question = ["turn face right", "turn face left"]


def liveness_orientation_check(video_path = "test_vid.mp4"):
    ORIENTATION = None
    challenge_res1 = 'fail'
    frame_interval = 5

    input_type = "video"
    i = 1

    index_question = random.randint(0,1)
    question1 = question[index_question]

    print(f"\n\nQUESTIONS: {question1}\n\n")

    #----------------------------- Video ------------------------------
    if input_type == "video":
        vid = cv2.VideoCapture(video_path)
        while True:
            start_time = time.time()
            ret, im = vid.read()
            if not ret:
                break

            if i % frame_interval == 0:
                im = imutils.resize(im, width=720)
                out = f_liveness_detection.detect_liveness(im)
                boxes = out['box_face_frontal'] + out['box_orientation']

                orientation = out['orientation']
                if orientation and ORIENTATION is None:
                    ORIENTATION = orientation

                challenge_res1_temp = challenge_result(question1, ORIENTATION)
                if challenge_res1=='fail' and challenge_res1_temp=='pass':
                    challenge_res1 = challenge_res1_temp

            end_time = time.time() - start_time
            FPS = 1 / end_time
            i+=1
        
        print(f"\n\nCHALLENGE RESULT : {challenge_res1}\n\n")
        if challenge_res1 == "pass":
            print("\n\n------------- SUCCESS --------------\n\n")
        else:
            print("\n\n------------- FAIL --------------\n\n")
            
