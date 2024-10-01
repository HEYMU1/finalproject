abc = [[884, 569], [811, 504], [786, 405], [794, 321], [789, 257], [877, 336], [889, 245], [897, 192], [907, 144], [931, 346], [955, 254], [972, 199], [986, 151], [972, 371], [1006, 291], [1028, 239], [1046, 192], [1008, 407], [1047, 348], [1073, 308], [1096, 269]]



for i in range(21):
                if landmark_list[i] == abc[i]:
                    count = count + 1
            
            if count > 10 :
                gesture = "Hi"
            else :
                gesture = None




            if gesture :
                h, w, c = frame.shape
                y = h - 20
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 1
                text_size, _ = cv2.getTextSize(gesture, font, font_scale, 2)
                x = (w - text_size[0]) // 2
                cv2.putText(frame, gesture, (x,y), font, font_scale, (255, 255, 255), 2)



average_distance = np.mean(distances)
print(f"Average distance between landmarks: {average_distance:.2f}")

if average_distance < 50:  # adjust this threshold value as needed
    print("Landmark lists are matching")
else:
    print("Landmark lists are not matching")