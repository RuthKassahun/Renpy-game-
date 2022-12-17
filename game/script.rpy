define config.rollback_enabled = False

python:
    flag = True
init python:
    import requests
    #import time
    from time import time

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
image bg hospital="hospital_1.jpg"
image Laplacian_filter=im.Scale("Laplacian_filter.jpg",621,308)
image bg white="bg_white_.jpg"
image supervisor="Supervisor_speaking_resi.png"
image angry_supervisor="Supervisor_disappointed_resized.png"
image happy_supervisor="Supervisor_happy_resized.png"
image mri=im.Scale("mri.jpg",643,271)
image mri2=im.Scale("mri3.jpg",443,171)
image bg radiology="radiology.jpg"
image medical note=im.Scale("Medical_Notes.png",512,512)
image dawson="dawson.jpg"
image normal_brain="normalBrain.jpg"
image other_brain="brain_other.PNG"
image saggital_brain="saggital_brain.PNG"
image saggital_brain_enhanced="saggital_brain_enhanced.PNG"
image t1t2="t1t2.PNG"
image accuracy="accuracy_paper.PNG"
image CNN="CNN.PNG"


image breast1="breast.PNG"
image breast2="breast_L_ML.png"
image breast3="metrics.PNG"
image breast4="confusion_matrix.PNG"
image breast5="dog.PNG"
image breast6="blob.PNG"


image break_time="break_time.jpg"
image insert_coin="insert_coin.jpg"


image equation_frequency= "frequency_equation.png"

# The game starts here.

default score = 0.0

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg hospital_1

    scene bg hospital
    with fade
    show supervisor
         
    show screen stat_screen(score) 
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue. 
    
    "Hello, I will be your supervisor on your first day as an intern in the MAIA Clinic."
    python:
        name = renpy.input("What's your name?")

        name = name.strip() or "Intern"
    "it's nice to meet you [name] !"
    "You will be working on a clinical case in which your background knowledge will be evaluated,"
    "you will also learn some of the most important aspects to be taken into account when addressing
    such problems."
    "This is the first case you will be working on. We have received in the radiology department a caucasian
    male patient aged 28 who works as a lawyer. "
    "He’s been referred from the neurological department
    since they suspect the kind of disease he might have, but the symptoms closely overlap with some
    other diseases."
    "Therefore, they would like to do further analysis and verify the patient’s diagnosis by
    using adequate advanced medical imaging techniques."
    "He has been facing the following symptoms:"
    "The patient refers to having fatigue and some visual problems (blurred sight) in his left eye."
    "He initially thought it was because of stress, but after two weeks he is feeling that tiredness
    was brought on by performing very simple tasks that were previously not as strenuous for
    him (working on the computer, reading documents)."
    "He also points out that the time spent
    working before the onset of fatigue had been decreasing drastically, causing the decrease in
    stamina to hamper his day to day activities quite severely."
    "He occasionally felt numb on his legs and arms. Issues related to his motor ability have been
    seen during the clinical examination by the referring neurologist."
    "The patient has been recently diagnosed with urinary tract infection which resulted in
    burning sensation during urination and sudden urge to urinate more frequently than ever
    before."
    " Patient does not go out a lot. He smokes socially and grandmother on the mother’s side has diabetes, and several relatives on the father’s side
    have heart conditions, with his grandfather having dementia."
    
    #scene bg hospital

    "Based on the case information/findings, what disease do you think the patient has?"
    python:
        start_time = time()
    menu:
        
        "Stroke":
            jump incorrect_1
        "Diabetes":

            jump incorrect_1
        "Neuromyelitis Optica Spectrum Disorder (Devic Disease)":

            jump incorrect_1
        "Multiple Sclerosis":

            jump correct_1

        "Parkinson\’s Disease":

            jump incorrect_1

    return

    


label incorrect_1:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100

    "That's incorrect. The patient most likely has multiple sclerosis"
    "There are many diseases that have symptoms that are quite common with multiple
    sclerosis, making it a difficult one to diagnose."
    "Conditions such as stroke can result in exactly the same
    symptoms of blurred vision and numbness in the limbs, with some crucial differences such as the time
    taken for the symptoms to appear being the clue."
    "Since the patient’s symptoms progressed gradually,
    they did not have a stroke despite his family history of heart conditions and his smoking habits."
    "Diabetes causes blurred vision and frequent urination, with diabetic neuropathy causing numbness in
    limbs due to nerve damage, which are similar to the symptoms the patient is exhibiting"
    "but the lack of the absence of severe thirst is crucial and rules out diabetes being the cause, especially since the
    patient had already been diagnosed with an UTI recently to explain why those symptoms occurred."
    "The symptoms of MS are also most similar to Neuromyelitis Optica Spectrum Disorder (NMOSD) since
    they are both neurodegenerative in nature, where the differentiating factor is that NMOSD affects
    both eyes at a time."
    "The regions affected by NMOSD are the optic nerves and the spinal cord, while in
    MS the brain is most frequently affected alongside optic nerves and spinal cord also being affected."
    "In MS, cognitive disabilities are frequent, while NMOSD does not cause any cognitive problems."
    "Parkinson’s usually appears in patients aged 60 or older, with symptoms being mostly related to
    physical disabilities, such as difficulty walking, appearing on one side of the body only. "
    "Given the patient’s age and prominent symptoms of blurred vision and fatigue on top of the numbness, it is
    unlikely that the patient has Parkinson’s disease."
    "Multiple Sclerosis is a neurodegenerative disease affecting the brain and spinal cord, and is most
    common in caucasians, with patients diagnosed commonly ranging from 20s to 50s."
    "There are more cases of the disease reported in the northern hemisphere, with lack of exposure to vitamin D being
    linked as one of the contributing factors, along with habits such as smoking."
    "Genetics also plays a role in the onset of MS, as the risk increases drastically if a direct relative (parent or sibling) has the
    disease."
    "The disease progresses slowly, and commonly affects cognitive abilities, while also causing physical symptoms such as fatigue,
    vision problems, numbness, etc."
    "The patient is thus suspected to have Multiple Sclerosis."


    jump q2


return

label correct_1:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100

    #$ minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)
    #$seconds = float(renpy.get_game_runtime())
    #$round_seconds= seconds*100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = 1.0 + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    #"Time spent [seconds_elapsed]"
    show screen stat_screen(score_round)  

    "Your answer is correct! Well done!"
    "There are many diseases that have symptoms that are quite common with multiple
    sclerosis, making it a difficult one to diagnose."
    "Conditions such as stroke can result in exactly the same
    symptoms of blurred vision and numbness in the limbs, with some crucial differences such as the time
    taken for the symptoms to appear being the clue."
    "Since the patient’s symptoms progressed gradually,
    they did not have a stroke despite his family history of heart conditions and his smoking habits."
    "Diabetes causes blurred vision and frequent urination, with diabetic neuropathy causing numbness in
    limbs due to nerve damage, which are similar to the symptoms the patient is exhibiting"
    "but the lack of the absence of severe thirst is crucial and rules out diabetes being the cause, especially since the
    patient had already been diagnosed with an UTI recently to explain why those symptoms occurred."
    "The symptoms of MS are also most similar to Neuromyelitis Optica Spectrum Disorder (NMOSD) since
    they are both neurodegenerative in nature, where the differentiating factor is that NMOSD affects
    both eyes at a time."
    "The regions affected by NMOSD are the optic nerves and the spinal cord, while in
    MS the brain is most frequently affected alongside optic nerves and spinal cord also being affected."
    "In MS, cognitive disabilities are frequent, while NMOSD does not cause any cognitive problems."
    "Parkinson’s usually appears in patients aged 60 or older, with symptoms being mostly related to
    physical disabilities, such as difficulty walking, appearing on one side of the body only. "
    "Given the patient’s age and prominent symptoms of blurred vision and fatigue on top of the numbness, it is
    unlikely that the patient has Parkinson’s disease."
    "Multiple Sclerosis is a neurodegenerative disease affecting the brain and spinal cord, and is most
    common in caucasians, with patients diagnosed commonly ranging from 20s to 50s."
    "There are more cases of the disease reported in the northern hemisphere, with lack of exposure to vitamin D being
    linked as one of the contributing factors, along with habits such as smoking."
    "Genetics also plays a role in the onset of MS, as the risk increases drastically if a direct relative (parent or sibling) has the
    disease."
    "The disease progresses slowly, and commonly affects cognitive abilities, while also causing physical symptoms such as fatigue,
    vision problems, numbness, etc."
    "The patient is thus suspected to have Multiple Sclerosis."

    

    
    
    screen stat_screen(score):
        frame:
            xpadding 40
            ypadding 20
            xpos 20
            ypos 50
            text "Score: [score]"
            
    
 
       
 

    jump q2


return

label q2:

 
    scene bg hospital
    with fade
    show supervisor

    "The patient is suspected to have MS. However, it is of great importance to actually confirm the
    presence of the disease and evaluate its current stage in order to design a suitable treatment for this
    patient. "
    "Based on the knowledge you have gained during the course of your Master’s, what would you
    say is the most suitable (the one that you would do in first place) medical imaging modality to start
    the screening of the patient?"
    python:
        start_time = time()
    menu:
        
        "CT scan":
            jump incorrect_2

        "MRI":
            jump correct_2

        "CSF Spinal Tap":
            jump incorrect_2
        "PET":
            jump incorrect_2
    return

label incorrect_2:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100

    "Well, The correct answer is MRI."
    "The gold standard imaging modality to assess the presence of axional inflammation in
    multiple sclerosis is MRI."

    jump q3

return

label correct_2:

    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100

    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)  

    "Awesome! As you saidThe gold standard imaging modality to assess the presence of axional inflammation in
    multiple sclerosis is MRI."
    
    jump q3

return

label q3:

    scene bg hospital
    with fade
    show supervisor

    "CT Scans are preferably used instead of MRI since they cost half the price and are much faster.
    However, why would you think MRI is preferred to be used when examining the brain for detecting
    diseases such as MS?" 
    python:
        start_time = time()
    menu:
        
        "MRI provides low tissue contrast, which makes it easier to spot lesions within soft tissue,
    `   whereas CT provides good tissue contrast, which makes it suitable for other applications such
        as detecting traumas in anatomical structures.":

            jump incorrect_3

        "MRI provides low tissue contrast, which makes it harder to spot lesions within soft tissue,
        whereas CT provides good tissue contrast, which makes it suitable for other applications such
        as detecting traumas in anatomical structures.":

            jump incorrect_3

        "MRI provides good tissue contrast, which makes it harder to spot lesions within soft tissue,
        whereas CT provides low tissue contrast, which makes it suitable for other applications such
        as detecting traumas in anatomical structures.":

            jump incorrect_3
        "MRI provides good tissue contrast, which makes it easier to spot lesions within soft tissue,
        whereas CT provides low tissue contrast, which makes it suitable for other applications such
        as detecting traumas in anatomical structures.":
            jump correct_3

    return

label incorrect_3:

    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    
    "That's not right. Well as compared to CT, MRI scans provide more pronounced image quality around white
    matter (where most of the lesions of MS are typically located), since they have excellent tissue contrast."
    "As the MS affects the myelin coats around the nerve, MRI can easily detect the regions
    where the myelin is missing. "
    "CT is mainly used for screening fractures, as it provides structural images
    of organs, tissues and bones. CSF spinal fluid tap testing is another important method to analyze a
    patient's auto immune around the brain and spinal cord."

    jump q4
return

label correct_3:

    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)

    "That's right. As compared to CT, MRI scans provide more pronounced image quality around white
    matter (where most of the lesions of MS are typically located), since they have excellent tissue contrast."
    "As the MS affects the myelin coats around the nerve, MRI can easily detect the regions
    where the myelin is missing. "
    "CT is mainly used for screening fractures, as it provides structural images
    of organs, tissues and bones. CSF spinal fluid tap testing is another important method to analyze a
    patient's auto immune around the brain and spinal cord."
    jump q4
return

label q4:

    scene bg hospital
    with fade
    show supervisor

    "Great! Now that we know we have to work with MRI, we are going to get started
    with the analysis of the patient data. He is going to get an MRI now."

    scene bg radiology
    "Patient gets MRI"

    scene bg hospital
    with fade
    show supervisor

    "From his clinical history we found out that he got another MRI done 3 years ago in this same hospital,
    which was diagnosed as normal. "
    "However, due to some confusions in the MRI lab, both images have
    been mixed up and therefore we are required to find out which one corresponds to normal and
    disease conditions. "
    "First of all, you will need to solve the puzzle to reconstruct both images: {a=https://puzzel.org/es/slidingpuzzle/play?p=-NITxrPB8MmtffXsOA7_}Use this link to construct the images{/a} "
    python:
        start_time = time()
    menu:
        
        "Both images corresponds to MS":
            jump incorrect_4

        "1 corresponds to normal, 2 corresponds to MS":
            jump incorrect_4

        "1 corresponds to MS, 2 corresponds to normal ":
            jump correct_4
        "Both images are normal":
            jump incorrect_4
    return

label incorrect_4:

    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "Well,as it can be observed, image one has some lesions around the area of white matter,
    so that one corresponds to MS. "

    jump q5
return

label correct_4:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "Well done! as it can be observed, image one has some lesions around the area of white matter,
    so that one corresponds to MS. "
    
    jump q5
return

label q5:
    scene bg hospital
    with fade
    show supervisor

    "Great! Image 1 corresponds to disease conditions. However, these images have been acquired with one of our oldest
    acquisition machines, which is about to be replaced in the next few weeks."
    "Our next goal is to study techniques to further analyze the lesions present in the image by means of image processing
    or machine/deep learning approaches."
    "In order to do this, it is required for the images to be pre-processed"
    "One of the key steps during pre-processing is noise and artifacts removal. Which of the following methods do you think 
    would allow us to get denoised images?"
    python:
        start_time = time()
    menu:
        "Histogram Equalization":
            jump incorrect_5

        "Filtering":
            jump correct_5

        "Thresholding":
            jump incorrect_5
    
    return
label incorrect_5:
    scene bg hospital
    show angry_supervisor:
         xpos 400
         ypos 100

    "That's incorrect.  Histogram equalization would improve the intensity distribution of the image in general, 
    but it would do nothing to remove the noise. Thresholding is used for segmentation, and it would not 
    remove and replace the noise."
    "Filtering would be the best option, as there are many kinds of filters amongst which we can select the one
    that is best suited for removal of this particular type of noise."

    jump q6
return

label correct_5:
    scene bg hospital
    show happy_supervisor:
         xpos 400
         ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "That's correct.Awesome! "
    
    jump q6
return

label q6:
    scene bg hospital
    with fade
    show supervisor

    "Since filtering is the correct method to get denoised images, which filter do you think would work best in 
    removing the type of noise that exists in these images?"
    python:
        start_time = time()
    menu:
        "Gaussian filter":
            jump incorrect_6

        "Bilinear filter":
            jump incorrect_6

        "Median filter":
            jump correct_6
    
    return
label incorrect_6:
    scene bg hospital
    show angry_supervisor:
         xpos 400
         ypos 100

    "The correct answer is median filter.   The type of noise that is present in these images is salt and pepper noise.
    Gaussian filter is actually a smoothing filter"
    "so it does not meet our requirements of preserving boundaries, and neither would it remove the noise since the 
    information presented by the noise would be taken into account during the smoothing."
    "While a bilinear filter would be an improvement compared to gaussian filtering, since edges are preserved"
    "this filter is more appropriate for removal of gaussian noise. While all of these filters can be fine-tuned 
    for the purpose of removing the noise to some extent, the median filter is the simplest and yet the most effective 
    in salt and pepper noise removal. "
    " It takes the median value from amongst the pixels that the kernel is applied to, so that outliers such as the sudden 
    occurrence of infrequent high and low values are removed."
    jump q7
return

label correct_6:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)

    "You're doing a great job. Indeed the correct answer is median filter.   The type of noise that is present in these images is salt and pepper noise.
    Gaussian filter is actually a smoothing filter"
    "so it does not meet our requirements of preserving boundaries, and neither would it remove the noise since the 
    information presented by the noise would be taken into account during the smoothing."
    "While a bilinear filter would be an improvement compared to gaussian filtering, since edges are preserved"
    "this filter is more appropriate for removal of gaussian noise. While all of these filters can be fine-tuned 
    for the purpose of removing the noise to some extent, the median filter is the simplest and yet the most effective 
    in salt and pepper noise removal. "
    " It takes the median value from amongst the pixels that the kernel is applied to, so that outliers such as the sudden 
    occurrence of infrequent high and low values are removed."
   
    jump q7
return

label q7:
    scene bg hospital
    with fade
    show supervisor

    "You’re doing well answering these questions. However, working with these images also requires additional 
    preprocessing steps since all images do not have the same quality after being acquired."
    "In addition to denoising the artifacts, what other methods do you recommend for pre-processing of the MRI scan?"
    python:
        start_time = time()
    menu:
        "Maximize the spatial resolution of the scanned image":
            jump incorrect_7

        "Color normalization":
            jump incorrect_7

        "White matter intensity equalization in T1-weighted image":
            jump incorrect_7

        "Normalize the intensity":
            jump correct_7
    
    return

label incorrect_7:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "The right answer will be intensity normalization.To enhance the intensity of the acquired MRI image, normalization of the intensity is a relevant procedure. "
    "This will fix the range of each brain tissue  intensities with a considerable amount of variation resulting in a 
    well contrasted image. "
    " Typically the scanned MRI images will not be maximized to output high resolution images. "
    "This procedure is resource intensive as it will reconstruct each voxel back to higher resolution."
    " Color normalization is not required as the MRI scanned images are gray level intensity images. "
    scene bg hospital
    with fade
    show other_brain:
        xpos 500
        ypos 80
    "This would be the image obtained after denoising. As you see, the lesions are easier to spot. Especially those smallest ones usually can be seen fingers apart."
    jump q8
return

label correct_7:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "That's right. To enhance the intensity of the acquired MRI image, normalization of the intensity is a relevant procedure. "
    "This will fix the range of each brain tissue  intensities with a considerable amount of variation resulting in a 
    well contrasted image. "
    " Typically the scanned MRI images will not be maximized to output high resolution images. "
    "This procedure is resource intensive as it will reconstruct each voxel back to higher resolution."
    " Color normalization is not required as the MRI scanned images are gray level intensity images. "
    scene bg hospital
    with fade
    show other_brain:
        xpos 500
        ypos 80
    "This would be the image obtained after denoising. As you see, the lesions are easier to spot. Especially those smallest ones usually can be seen fingers apart."
    
    jump q8
return

label q8:
    scene bg hospital
    with fade
    show supervisor

    "We can clearly see the lesions in this slice from the sagittal view of the patient. But there’s something important in the image that isn’t often visible in the 
    sagittal view of the brain. "
    "When we see the transverse view of the patient scan, we can see there is a circular ring around the ventricles. "
    "These ring shaped structures are important landmarks for the detection of one specific type of MS. However, as you can see in the first image, they appear to be 
    fadings around the contours of the ring. "
    "Can you suggest a way to clearly see the ring around the left ventricle?"

    scene bg hospital
    with fade
    show saggital_brain
    python:
        start_time = time()
    menu:
        "Apply morphological gradient":
            jump incorrect_8

        "Use T2-flair image instead":
            jump incorrect_8

        "Apply gadolinium contrast agent ":
            jump correct_8

        "Use another slice of the image to better visualize the ring lesion":
            jump incorrect_8
    
    return
label incorrect_8:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "Hmmm actually to enhance  the ring effect gadolinium contrast agent is applied in T1-weighted image. "
    "This is usually the case for tumefactive multiple sclerosis where the tumor-like lesions appear like a ring shape around the ventricles."
    "Morphological gradients can also result in getting the contours around the tumor however there are other small insignificant structures that will be enhanced along the way."
    scene bg hospital
    with fade
    show saggital_brain_enhanced:
        xpos 500
        ypos 120
    "After applying the gadolinium contrast this is the result we will get. Now the rings can be clearly seen. "
    jump q9
return

label correct_8:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "That's correct indeed to enhance  the ring effect gadolinium contrast agent is applied in T1-weighted image. "
    "This is usually the case for tumefactive multiple sclerosis where the tumor-like lesions appear like a ring shape around the ventricles."
    "Morphological gradients can also result in getting the contours around the tumor however there are other small insignificant structures that will be enhanced along the way."
    scene bg hospital
    with fade
    show saggital_brain_enhanced:
        xpos 500
        ypos 120
    "After applying the gadolinium contrast this is the result we will get. Now the rings can be clearly seen. "
    jump q9
return

label q9:
    scene bg hospital
    with fade
    show supervisor

    "Now, since we have the denoised and preprocessed image, we can clearly see the locations of the lesions. "

    python:
        start_time = time()
    menu:
        "Dark matter":
            jump incorrect_9

        "Meninges":
            jump incorrect_9

        "CSF":
            jump incorrect_9

        "Periventricular region":
            jump correct_9
    
    return

label incorrect_9:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "That's  not correct.  Multiple sclerosis will most likely have lesions that could be found in proximity of the  ventricular region."
    "Commonly, these lesions have the shape of a finger and are therefore known as Dawson’s fingers. "
    "The lesions can be seen pointing away from the lateral ventricles. Usually MRI scanners don't display the lesions found around the dark matter"
    " instead the majority of the lesions can be depicted around the white matter and the bottom of the fourth ventricle."
    jump q10
return
label correct_9:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "You're correct. Multiple sclerosis will most likely have lesions that could be found in proximity of the  ventricular region."
    "Commonly, these lesions have the shape of a finger and are therefore known as Dawson’s fingers. "
    "The lesions can be seen pointing away from the lateral ventricles. Usually MRI scanners don't display the lesions found around the dark matter"
    " instead the majority of the lesions can be depicted around the white matter and the bottom of the fourth ventricle."
    
    jump q10
return

label q10:
    scene bg hospital
    with fade
    show supervisor

    "We’ve correctly identified the MS lesions from the MRI images. Now that we know where we can find the lesions in the MRI images"
   
    
    scene bg hospital
    with fade
    show t1t2:
        xpos 400
        ypos 100


    "we can choose which MRI sequence is the most adequate for working with in this case. "
    python:
        start_time = time()
    menu:
        "T1-weighted is mainly used for lesion detection and T2-weighted for segmentation of brain tissues.":
            jump incorrect_10

        "T1-weighted sequence is sufficient for segmentation and lesion detection.":
            jump incorrect_10

        "Instead of T1-weighted and T2-weighted sequences, the FLAIR sequence is used for segmentation and lesion detection.":
            jump incorrect_10

        "T2-weighted is commonly used for lesion detection and T1-weighted is suitable for brain tissue segmentation. ":
            jump correct_10
    
    return
label incorrect_10:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "Hmmmm that's not right as the T1-weighted sequence shows high contrast between gray matter and white matter regions"
    " it’s mainly applicable for segmentation tasks. In cases of multiple sclerosis, T2-weighted sequence is better at localizing lesion regions"
    "as it provides high lesion-to-brain contrast and lesions appear hyper-intense in these sequences."
    jump q11
return

label correct_10:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "Correct! as the T1-weighted sequence shows high contrast between gray matter and white matter regions"
    " it’s mainly applicable for segmentation tasks. In cases of multiple sclerosis, T2-weighted sequence is better at localizing lesion regions"
    "as it provides high lesion-to-brain contrast and lesions appear hyper-intense in these sequences."
    
    jump q11
return

label q11:
    scene bg hospital
    with fade
    show supervisor

    "There is still a lot of information in the MRI scans that we don’t need. One of these is the skull, and we only need brain tissue specifically for our purposes."
    "As you might already know skull stripping is a principal preprocessing step to differentiate brain and non-brain tissue."

    "Do you think the presence of a lesion will affect the accuracy of skull stripping?"
    python:
        start_time = time()
    menu:
        "Yes":
            jump correct_11

        "No":
            jump incorrect_11
    
    return
label incorrect_11:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "That's a tricky question, the answer is yes,the intensity distribution of tissues affected by lesion is different thus the skull stripping couldn’t be the same as that of the normal tissue."
    "See? This is why it’s very important to perform skull-stripping. Have you used any softwares before for skull stripping?"
    menu:
        "Yes, I have used SPM before":
            jump spm_comment
    return

label correct_11:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "Wonderful, That's that's excellent. The intensity distribution of tissues affected by lesion is different thus the skull stripping couldn’t be the same as that of the normal tissue."
    "See? This is why it’s very important to perform skull-stripping. Have you used any softwares before for skull stripping?"
   

    menu:
        "Yes, I have used SPM before":
            jump spm_comment
    return


label spm_comment:
    "That’s a great tool. FreeSurfer is another most widely used application as well. "

    jump q12
return

label q12:
    scene bg hospital
    with fade
    show supervisor

    "Knowing the volume of the lesions is actually important for us. This is because in the follow up treatments"

    "we would like to know if the lesions have decreased in size as a response to patient treatment."
    "We could segment the lesions to get their volume."
    "Yes! segmentation plays a key role in the detection and prognosis of MS. Your task during the internship period would be building deep learning models for accurate segmentation of MS lesions."
    "In order to do this we have to study important aspects to be taken into account and do a little bit of literature review. "
    "since we need the volumes of the segmentations, we need to use an evaluation metric to evaluate the quality of the segmented volume."
    "Which segmentation evaluation metric is volume-based only?"
    python:
        start_time = time()
    menu:
        "Hausdorff distance":
            jump incorrect_12

        "Dice Score":
            jump incorrect_12

        "Volumetric Similarity":
            jump correct_12

        "Jaccard Index":
            jump incorrect_12
    
    return
label incorrect_12:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "Hmmmm that's not right.There are many evaluation methods used to quantify the quality of the segmentation, and all the metrics mentioned can be used for this task. "
    "Hausdorff distance only takes spatial distance between points into account, and dice score and jaccard index are based on the degree of overlap the segmented images have with the ground truth."
    "Volumetric similarity considers the differences in volume only, and does not take the distance between points or overlap of segmented regions into consideration. "
    "In cases where the outer contour and degree of overlap are not of importance, but only the magnitude of the segmented volume is necessary, volumetric similarity is most appropriate. "
    jump q13
return

label correct_12:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "Awesome! That's indeed the correct answer. There are many evaluation methods used to quantify the quality of the segmentation, and all the metrics mentioned can be used for this task. "
    "Hausdorff distance only takes spatial distance between points into account, and dice score and jaccard index are based on the degree of overlap the segmented images have with the ground truth."
    "Volumetric similarity considers the differences in volume only, and does not take the distance between points or overlap of segmented regions into consideration. "
    "In cases where the outer contour and degree of overlap are not of importance, but only the magnitude of the segmented volume is necessary, volumetric similarity is most appropriate. "
    
    jump q13
return

label q13:
    scene bg hospital
    with fade
    show supervisor

    "So we know that volumetric similarity is more appropriate for this task. But when the shape of the lesion is of importance, do you know which metric should be used?"
    python:
        start_time = time()
    menu:
        "Hausdorff distance":
            jump correct_13

        "Dice Score":
            jump incorrect_13

        "Volumetric Similarity":
            jump incorrect_13

        "Mahalonobis distance":
            jump incorrect_13
    
    return

label incorrect_13:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "The correct answer is Hausdorff distance. "
    "Distance metrics that are spatial based, such as Hausdorff distance, provide information about the dissimilarity of the shape."
    "Other metrics only consider the percentage of overlap between the different segmentations. "
    "I think it's better to take some break here. You came to a busy day, I hope it's not overwhelmeing you."
    "Let's take some snacks here"
    jump break_time
return

label correct_13:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "As you said the correct answer is Hausdorff distance. "
    "Distance metrics that are spatial based, such as Hausdorff distance, provide information about the dissimilarity of the shape."
    "Other metrics only consider the percentage of overlap between the different segmentations. "
    "I think it's better to take some break here. You came to a busy day, I hope it's not overwhelmeing you."
    "Let's take some snacks here"
   
    jump break_time
return

label break_time:
    scene break_time
    with irisout
    show supervisor
        
    python:
        msg1 = renpy.input("How do you like your first day here?")

        msg1 = msg1.strip() or "it's going great"
    "It's funny you said [msg1]"
    "It could be a little overwelming at first but I am sure you will love it."
    "Ohhh I forgot my wallet, do you have some coins?"

    menu:
        "Yes,here you go":
            scene break_time
            with fade
            show happy_supervisor
            "Thanks... uh.. I owe you one"
            scene break_time
            with fade
            show insert_coin:
                alpha 1.0
                linear 1.0 alpha 0.0
                pause .150
                linear 1.0 alpha 1.0
                pause .150
                
            
 
 

        "No, sorry I only have for myself":
                scene break_time
                with fade
                show angry_supervisor
                "uh...ok.. I will go and get my wallet"
                scene break_time
                with fade

    
    jump q14

label q14:
    
    scene bg hospital
    with fade
    show supervisor

    "In MAIA clinic we have 25 cases of patients with Multiple sclerosis. We are studying these cases in our research and development department."
    "We want to register this particular patient MRI scan along with other patient MRI scans  in order to build a probabilistic atlas that will be used by you during the course of your thesis work."
    " In order to register the acquired image what registration techniques would you recommend?"
    "Which image registration method would you recommend?"
    python:
        start_time = time()
    menu:
        "Affine registration":
            jump incorrect_14

        "Non-rigid registration":
            jump incorrect_14

        "Affine registration followed by non-rigid registration":
            jump correct_14

        "Non-rigid registration followed by affine registration":
            jump incorrect_14
    
    return
label incorrect_14:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "Hmm it's actually prefered to perform affine registration followed by non-rigid registration "
    "To segment each brain tissue it is advised to register the intensity images beforehand. Linear transformation such as affine registration can be used initially to align the images. "
    "In some cases where the transformation is not linear, non-rigid registration techniques are used"
    jump q15
return  

label correct_14:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 
    "Well done! Ususally we perform affine registration followed by non-rigid registration "
    "To segment each brain tissue it is advised to register the intensity images beforehand. Linear transformation such as affine registration can be used initially to align the images. "
    "In some cases where the transformation is not linear, non-rigid registration techniques are used"
    
    jump q15
return  

label q15:
    scene bg hospital
    with fade
    show supervisor

    "Now we have most of the information that we need. Starting tomorrow, your work will be divided into two parts:"
    "MS lesion segmentation based on atlas and deep learning approaches! But before ending up with our day, let’s do some literature review. "
    "Multiple methods have been proposed in the literature, and they are mostly based in automatic segmentation by using Deep Learning approaches. "
    "One of the most common architectures used for this task is U-Net. Do you know about it?"
    python:
        start_time = time()
    menu:
        "yes, I worked with it during my second and third semester!":
            jump choice_q15
    return

label choice_q15:
    scene bg hospital
    with fade
    show supervisor

    "Perfect! As its name suggests, this network has the shape of U, and is composed of two important parts: encoder and decoder. Do you remember what is the role of the encoder part?"
    
    menu:
        "The role of the encoder is to reduce the spatial dimensions of the images and reduce the number of channels.":
            jump incorrect_15

        "The role of the encoder is to increase the spatial dimensions of the images and increase the number of channels.":
            jump incorrect_15

        "The role of the encoder is to reduce the spatial dimensions of the images and increase the number of channels. ":
            jump correct_15

        "The role of the encoder is to increase the spatial dimensions of the images reducing the number of channels.":
            jump incorrect_15
    return

label incorrect_15:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "Hmm well, the encoder’s goal is to compress the information of the images in terms of space but increasing the number of channels."
    "In each of the decoder steps there are skip connections placed so that the decoder is given enough context information for the generation of the segmentation masks. "

    jump q16
return  

label correct_15:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "That's right, the encoder’s goal is to compress the information of the images in terms of space but increasing the number of channels."
    "In each of the decoder steps there are skip connections placed so that the decoder is given enough context information for the generation of the segmentation masks. "
    
    jump q16
return  

label q16:
    scene bg hospital
    with fade
    show supervisor

    "Even though U-Net and several variations of it have been widely used for MS lesions segmentation, there have been some other recent approaches that use Convolutional Neural Networks. "
    "After revising some literature with the R&D team of the hospital, we have found a very interesting paper that tackles this problem using CNN. "
    "They achieved higher performance than 4 other state-of-the-art approaches in 2018. Their 2 major improvements are the adding of dropout to avoid overfitting,"
    "and also replacing common ReLu activation function for PReLu (Parametric ReLu), since ReLu cannot be trained by gradient descent method when the activation function values are zero."
    "Approaches such as leaky ReLu give a small value to the negative part. However, PReLu learns the slope from the negative part directly from the data. The authors of the paper conducted 
    several training experiments to prove the effect of DroupOut, and they show the following results: "

    scene bg hospital
    with fade
    show accuracy:
        xpos 350
        ypos 15
    
    "Which statement about the graphs is true?"
    python:
        start_time = time()
    menu:
        "Both images correspond to training with dropout at different rates. Dropout 1 > Dropout 2":
            jump incorrect_16

        "Image 1 corresponds to training with dropout (thus avoiding overfitting), and image 2 corresponds to training without dropout (thus overfitting)":
            jump incorrect_16

        "Image 1 corresponds to training without dropout (thus overfitting), and image 2 corresponds to training with dropout (thus avoiding overfitting)":
            jump correct_16

        "Both of the images correspond to training with dropout at different rates. Dropout 1 < Dropout2":
            jump incorrect_16
    
    return

label incorrect_16:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "The answer isn't correct. Image 1 corresponds to training without dropout (thus overfitting), and image 2 corresponds to training with dropout (thus avoiding overfitting)"
    "As you can see, in the first image the  accuracy of the test set reaches its maximum value from the 600th iteration, and then overfitting takes place since the test accuracy decreases."
    "On the other hand, in the second image the test accuracy increases steadily, which is the behavior of a non-overfitting training."
    jump q17
return  

label correct_16:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "The answer is correct. Well done! Image 1 corresponds to training without dropout (thus overfitting), and image 2 corresponds to training with dropout (thus avoiding overfitting)"
    "As you can see, in the first image the  accuracy of the test set reaches its maximum value from the 600th iteration, and then overfitting takes place since the test accuracy decreases."
    "On the other hand, in the second image the test accuracy increases steadily, which is the behavior of a non-overfitting training."
    
    jump q17
return 

label q17:
    scene bg hospital
    with fade
    show supervisor

    "It’s important to make sure that the model doesn’t overfit. The training of these deep learning models is controlled by the loss functions"
    "In general, there are a lot of loss functions that are well known and commonly used. Which of these is not a loss function?"
    python:
        start_time = time()
    menu:
        "Focal":
            jump incorrect_17

        "Binary Cross Entropy":
            jump incorrect_17

        "Mean Square Error":
            jump incorrect_17

        "Softmax":
            jump correct_17
    
    return
label incorrect_17:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "Hmmm that's not the right answer. Softmax is an activation function, while the others are loss functions. Activation functions control whether a neuron will be activated or not and add non-linearity to enable complex learning."
    "Loss functions such as Focal, Binary Cross Entropy, and Mean Square Error, calculate the error in the learning process of the model to help evaluate the updates"
    "that need to be made to improve the model performance."

    jump q18
return 
    
label correct_17:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 
    "Yes, that's right softmax is an activation function, while the others are loss functions. Activation functions control whether a neuron will be activated or not and add non-linearity to enable complex learning."
    "Loss functions such as Focal, Binary Cross Entropy, and Mean Square Error, calculate the error in the learning process of the model to help evaluate the updates"
    "that need to be made to improve the model performance."
    
    jump q18
return

label q18:
    scene bg hospital
    with fade
    show CNN:
        xpos 300
        ypos 160

    "The architecture of the network proposed in the paper is presented in the following table."
    "However, some of its parts are missing (the ones inside the red boxes)."
    "Based on your deep learning knowledge and by analyzing the remaining data provided, how would you fill the gaps so that the model is coherent"

    python:
        start_time = time()
    menu:
        "1. 32x16, 2. 64x128":
            jump incorrect_18

        "1. 16x48, 2. 128x64":
            jump incorrect_18

        "1. 16x32, 2. 64x128":
            jump incorrect_18

        "1. 48x16, 2. 128x64":
            jump correct_18
    
    return

label incorrect_18:
    scene bg hospital
    show angry_supervisor:
        xpos 400
        ypos 100
    "That's incorrect the right answer is 1. 48x16, 2. 128x64. "
    "Awesome! The paper reviewed is one of the state-of-the-art performers in terms of detection of MS lesions, and you were able to see how important it is to select an appropriate activation function"
    "depending on the application, but also understand which are the best techniques to handle overfitting."
    "Now,  I want to show you the software we use here in MAIA Clinic. In our radiology department we use 3D slicer application to segment the brain tissue regions."
    "Here you can see the segmented brain scan."

    scene bg hospital
    with fade
    # Add segmented image here

    jump end_of_case1
return

label correct_18:
    scene bg hospital
    show happy_supervisor:
        xpos 400
        ypos 100
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $ score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "Wonderful! that's the correct answer."
    "The paper reviewed is one of the state-of-the-art performers in terms of detection of MS lesions, and you were able to see how important it is to select an appropriate activation function"
    "depending on the application, but also understand which are the best techniques to handle overfitting."
    "Now,  I want to show you the software we use here in MAIA Clinic. In our radiology department we use 3D slicer application to segment the brain tissue regions."
    "Here you can see the segmented brain scan."
    scene bg hospital
    with fade
    # Add segmented image here

    jump end_of_case1
return

label end_of_case1:
    scene bg hospital
    with fade
    show supervisor

    "Now we have segmented brain tissues and the volumes are calculated, we will forward this information to the neurology department. "
    "Your goal during the following months would be to build an algorithm that can be as good as the software we use in the clinic!"
    "Thank you for assisting me today! I hope you learned how we deal with multiple sclerosis cases here in the radiology department."
    $score_round = "{:6.2f}".format(score)
    "Your overall point is [score_round]. Good Job!"
    jump case2_scene1
return
    

label case2_scene1:
    scene bg hospital
    with fade
    show happy_supervisor

    "Alright! Onto the next case!"
    
    "Are you ready to dive right into image processing today? It’s quite exciting, isn’t it?"
    menu:
        "Not really….":
            jump case2_scene1A

        "Yes, I look forward to it.":
            jump case2_scene1B

        "Yes, oh my god, I love image processing -can't wait to get started!":
            jump case2_scene1C

return

label case2_scene1A:
    scene bg hospital
    show supervisor
    "Aw, well that’s too bad."
    "Pace yourself and try to do as much as you can. It will help the doctors quite a lot."
    jump case2_q1
return

label case2_scene1B:
    scene bg hospital
    show supervisor
    "That’s good to hear. I hope you find what we'll be working with interesting."
    jump case2_q1
return

label case2_scene1C:
    scene bg hospital
    show happy_supervisor
    ".....That's....uh...wow....I was trying to motivate you more, but..."
    "uh...it's like you're the...personification of the motivation letter you submitted when applying here."
    "You might even be more motivated than me here, ahahahaaaa-"
    "Aaaaanyways, I'm really glad to hear that you're looking forward to it."
    jump case2_q1
return

label case2_q1:

    scene bg hospital
    with fade
    show supervisor

    "It appears that we'll be handling mammogram data."
    "The radiologist that is currently on call has sent some data for further analysis."
    "She has also sent us details about the case she is handling."

    "The patient received is a female, 38 years old of age. She claims to not have experienced any symptoms related to breast cancer, and was declared normal and healthy after physical examination."
    "However, she insists on having a screening due to her family history, and we have decided to take on her case despite screenings usually being done for women older than her."
    "She has an older sister, 45 years of age, who has recently been diagnosed with breast ductal carcinoma in situ (DCIS). A mammogram has already been performed for her as the primary screening method."

    "Now, do you know where DCIS originates?"
    python:
        start_time = time()
    menu:
        "Milk glands":
            jump case2_q1_incorrect

        "Milk ducts":
            jump case2_q1_correct

        "Lymph nodes":
            jump case2_q1_incorrect

        "Blood vessels":
            jump case2_q1_incorrect
return

label case2_q1_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, milk ducts is the correct answer."

    jump case2_q2
return

label case2_q1_incorrect:

    scene bg hospital
    show supervisor
    "Nope, that's incorrect. The right answer is milk ducts."

    jump case2_q2
return
    
label case2_q2:

    scene bg hospital
    with fade
    show breast1

    "DCIS is a type of breast cancer that originates in the milk ducts of the breast."
    "While the milk glands and ducts are closely related anatomical structures, as you can see in this image, the type of cancer that originates in the milk glands is a different one, called Lobular carcinoma in situ."
    "Lymph nodes and blood vessels can also be the origin of cancerous cells, and this is the case for another type of cancer termed angiosarcoma."
    
    scene bg hospital
    with fade
    show supervisor
    "The family history is important enough to be taken into consideration when it comes to DCIS."
    "Since she has an older sister who was diagnosed with it, her chances of having it are quite probable. "
    "It’s good that she has already had a mammogram performed. It will help us detect early signs of DCIS."

    "Keeping in mind that DCIS originates in the milk ducts, what do you think is the earliest sign of it?"
    
    python:
        start_time = time()
    menu:
        "Discharge from the nipples":
            jump case2_q2_incorrect

        "Inflammation of nipples":
            jump case2_q2_incorrect

        "Formation of solid breast masses":
            jump case2_q2_incorrect

        "Calcium deposits in milk ducts":
            jump case2_q2_correct
return

label case2_q2_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, you are right, it's calcium deposits in milk ducts."

    jump case2_q3
return

label case2_q2_incorrect:

    scene bg hospital
    show supervisor
    "No, that's not right, unfortunately. The right answer is calcium deposits in milk ducts."

    jump case2_q3
return

label case2_q3:

    scene bg hospital
    with fade
    show supervisor

    "Since mammograms are useful in detecting these calcifications, we can analyze the mammogram images."
    "But…oh dear, it seems the image is a little corrupt."
    show angry_supervisor
    "See for yourself by going to this {a=https://puzzel.org/es/slidingpuzzle/play?p=-NIXIrIuTw1QO3riamsn}link{/a}."
    "You’ll have to recover the complete image, it seems."
    "Don’t forget to save it by any means possible, since we’ll need it for further analysis."
    "Take a screenshot if you have to!"

    "Once you have recovered the image, shall we proceed?"
    python:
        start_time = time()
    menu:
        "Yes":
            jump case2_q4
    return

label case2_q4:
    
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    with fade
    show happy_supervisor

    "Well done, there."

    show angry_supervisor

    "Hmm...It seems that the doctor has given us only one mammogram image."

    show supervisor

    "Usually, 4 images are given."
    "Now that you've recovered the image, which view of the breast is this?"
    python:
        start_time = time()
    menu:
        "Mediolateral":
            jump case2_q4_incorrect
        "Craniocaudal":
            jump case2_q4_correct
        "Mediolateral Oblique":
            jump case2_q4_incorrect
    return    

label case2_q4_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, Craniocaudal is the right answer."

    jump case2_q5
return

label case2_q4_incorrect:

    scene bg hospital
    show supervisor
    "Hmm that's incorrect. The correct answer is Craniocaudal."

    jump case2_q5
return

label case2_q5:

    scene bg hospital
    with fade
    show supervisor

    "The craniocaudal view is taken from the top of the breast."
    "What differentiates it from the mediolateral or mediolateral oblique views is the pectoral muscle."
    "In the other two types of views, the pectoral muscle is usually clearly visible."
    "Since that’s not the case here, it is easy to determine from visual observations that this is the craniocaudal view."
    
    with fade
    show breast2

    "The mediolateral view, taken from the side, of the same breast has the pectoral muscle clearly visible, as you can see from another image that the doctor has just sent us."
    
    scene bg hospital
    with fade
    show supervisor

    "Ah, but the image doesn’t allow us to see many calcifications."
    "We need to be able to see more details in the image."
    "One obvious choice in order to be able to do that is contrast enhancement."
    "We might have to figure out which one works best, though."

    "Which of these contrast enhancement methods is local when applied to images?"
    python:
        start_time = time()
    menu:
        "Gamma Correction":
            jump case2_q5_incorrect
        "Histogram Equilization":
            jump case2_q5_incorrect
        "Adaptive Histogram Equilization":
            jump case2_q5_correct
        "Contrast Stretching":
            jump case2_q5_incorrect
    return



label case2_q5_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, Adaptive Histogram Equilization is correct."

    jump case2_q6
return

label case2_q5_incorrect:

    scene bg hospital
    show supervisor
    "That's incorrect. The correct answer is Adaptive Histogram Equilization."

    jump case2_q6
return

label case2_q6:

    scene bg hospital
    with fade
    show supervisor

    "All the methods mentioned are methods used to enhance contrast, but only adaptive histogram equilization is local."
    "Contrast stretching and histogram equilization are applied on the entire histogram of the image, and is not spatially selective and does not take local intensity differences into consideration."
    "Gamma correction is nonlinearly applied to histograms, making it selective to intensites in the intermediary range, but this is the case only for the intensities, and does not take spatial information into consideration either."
    "Adaptive histogram equilization, like CLAHE, on the other hand, takes histograms from small local neighbourhoods of the image only, and uses these local histograms to compute the new intensities."

    scene bg hospital
    with fade
    show happy_supervisor

    "Since we need the calcifications, the doctor has requested that we detect as many suspected calcifications in the image as possible."
    "We can do this by trying to make an algorithms to detect the highest number of true calcifications."
    
    scene bg hospital
    show supervisor
    
    "Usually, algorithms do not detect all the true positives, and sometimes end up mistaking other features as calcifications too, detecting false positives as a result."
    "So we need to measure both of these to evaluate the performance of the algorithm."

    "Which of these metrics do not take false positives into account?"
    python:
        start_time = time()
    menu:
        "Accuracy":
            jump case2_q6_incorrect
        "Precision":
            jump case2_q6_incorrect
        "Sensitivity":
            jump case2_q6_correct
        "Specificity":
            jump case2_q6_incorrect
    return

label case2_q6_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, Sensitivity is the right answer."

    jump case2_q7
return

label case2_q6_incorrect:

    scene bg hospital
    show supervisor
    "No, your answer is incorrect. The correct answer is Sensitivity."

    jump case2_q7
return

label case2_q7:

    scene bg hospital
    with fade
    show supervisor

    "All of these are metrics used to evaluate the performance of an algorithm designed for disease detection."
    scene bg hospital
    with fade
    show breast3:
        ypos 100
        xpos 200

    "Sensitivity is the only one of these that does not take false positives into account, as you can see from the formulas displayed."
    "It only considers the total number of positive samples correctly detected out of all the actual positive samples that exist, so it only takes true positives and false negatives into the formula."

    scene bg hospital
    with fade
    show supervisor

    "Okay, so now that you know what the metrics are for, let's do what the doctor has requested."
    "You’ll have to use the image that you previously recovered."
    "I'm going to give you the code that we used in a previous project for a similar task, so you just have to tinker around with it to learn what it does."
    "Go to this {a=https://colab.research.google.com/drive/1VLvQgcfA2p9Ar8CRsBMdw1uF90XjD0-w?usp=sharing}link{/a}, and edit the notebook to detect as many calcifications as possible."
    "Make sure to try different parameters by tuning them to increase the amount you detect."
    "You have to test the different parameters in order to get good results."
    "Get the number of possible candidates as the output, and make sure to save the notebook with the results loaded in order for me to be able to check later."
    scene bg hospital
    show happy_supervisor

    "There’s no rush, I’ll wait until you have as many possible candidates as possible in order for us to send our suspected findings to the doctor."
    "Though do keep in mind that we have other things to do today as well."
    "So if you spend too much time on this one, you won’t have time to complete the other things we have to do."

    "But feel free to go crazy with the number of candidates you detect. I’m serious."

    "Oh, but do you need further explanation about what to do in this task?"
    menu:
        "Yes":
            jump case2_q7_explain
        "No":
            jump case2_q7_continue

label case2_q7_explain:
    scene bg hospital
    with fade
    show supervisor
    "Alright, so candidate extraction in our case would be the detection of features that look like microcalcifications."
    "In order to do this, the code I have given you used blob detection using difference of gaussian."
    "So what blob detection does it that it extracts regions that are distinctly different from the rest of the image."
    "Laplacian of Gaussian, difference of gaussian, and determinant of gaussian are three common techniques used for this purpose."
    "Now, what the three techniques I mentioned does is enhance the regions we want to detect."
    "Since the calcifications appear very bright and dense in a black background, blob detection is able to capture them."
    "This is why it's a good starting point of our task of detecting calcifications."
    "It's worth mentioning that this detection task can be influenced by different preprocessing techniques."
    scene bg hospital
    with fade
    show breast5:
        ypos 120
        xpos 10
    "Now, for difference of gaussian, there are three main parameters."
    "For difference of gaussian to work, an image is first blurred with two gaussian kernels, with one gaussian kernel performing more smoothing than the other."
    "Next, the difference between the two smoothed images is taken."

    scene bg hospital
    with fade
    show breast6:
        ypos 100
        xpos 300
    "The blob detection then detects the distinct features from the difference of gaussian image."
    "Now, whether the blob detector detects only distinct features or whether is detects unnecessary features are controlled by the parameters of the sigmas and threshold."
    "The threshold controls whether blobs with high or low intensities will be detected, while the minimum and maximum sigma values control whether small or large blobs will be detected."
    "Therefore, tinker around with these parameters to complete the task given in order to see for yourself how the parameters effect the blob detection."

    jump case2_q7_continue
return

label case2_q7_continue:

    scene bg hospital
    with fade
    show supervisor

    "Okay, so if you're done, then tell me:"

    python:
        candidates = renpy.input(prompt="How many candidates did you find?", default="0", allow="0123456789")

    scene bg hospital
    with fade
    show supervisor
   
    $score = score + float(int(candidates)/1000)
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round)
    "So you detected [candidates] candidates? Alright."

    "Well done. We’ve sent your findings to the doctor. She says she’ll get back to us in a moment."
    "In the meantime, we’ve received data from another case she’s handling, and she’d like us to provide some statistics using the metrics we reviewed earlier."

    "This is the data she sent us."
    scene bg hospital
    with fade
    show breast4:
        ypos 250
        xpos 300
    "What are the calculated evaluations for the findings in the table?"
    python:
        start_time = time()
    menu:
        "Accuracy: 97.52\% Precision: 95.55\% Sensitivity: 94.50\% Specificity: 90.32\%":
            jump case2_q7_incorrect        
        "Accuracy: 94.50\% Precision: 97.52\% Sensitivity: 95.55\% Specificity: 90.32\%":
            jump case2_q7_correct
        "Accuracy: 90.32\% Precision: 94.50\% Sensitivity: 95.55\% Specificity: 97.52\%":
            jump case2_q7_incorrect
        "Accuracy: 94.50\% Precision: 97.52\% Sensitivity: 90.32\% Specificity: 95.55\%":
            jump case2_q7_incorrect
    return
       

label case2_q7_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, you are correct."

    jump case2_scene2
return

label case2_q7_incorrect:

    scene bg hospital
    show supervisor
    "No, your answer is incorrect."

    jump case2_scene2
return

label case2_scene2:
    scene bg hospital
    with fade
    show happy_supervisor
    
    "Since the number of true positives is 236, true negatives is 56, false positives is 6, and false negatives is 11, when you apply the respective formulas that we reviewed, the result you get is that the accuracy is 94.5\%, precision is 97.52\%, sensitivity is 95.55\%, and specificity is 90.32\%."

    "Those are certainly great results."
    "It’s expected, since she’s an expert who specializes in this field."
    "What do you think your findings with the image processing algorithm will like?"
    menu:
        "Not that great, I think.":
            jump case2_scene2A  
        "Probably as good as hers.":
            jump case2_scene2B
        "I think the CAD algorithm will be better.":
            jump case2_scene2C

    return

label case2_scene2A:
    scene bg hospital
    show supervisor

    "....Yeah, I agree. We'll have to do a lot more if we want our findings to be applicable."
    jump case2_scene3
return

label case2_scene2B:
    scene bg hospital
    show supervisor

    "...Probably not. It's not easy to get results on par with that of actual doctors using only some basic image processing."
    "Unfortunately, it's difficult for very simple and basic CAD algorithms to be applied to the medical domain."
    "But don't be discouraged, since there's a lot that we haven't tried, and the algorithms can always be improved."

    jump case2_scene3
return

label case2_scene2C:
    scene bg hospital
    show supervisor

    "...That's...uh....I admire your optimism, but let's be realistic."
    "The algorithm will have to be a lot more sophisticated if we want it to outperform doctors."
    "A LOT more. What we tried is a good start, however. But there's still a lot more that needs to be developed."

    jump case2_scene3
return

label case2_scene3:
    scene bg hospital
    with fade
    show supervisor

    "We have to strive to improve our algorithm as much as possible."
    "So far, when it comes to calcification detection, the best performances have been by deep learning algorithms."
    menu:
        "Wow, what a shocker.":
            jump case2_scene3A  
        "I didn’t know that.":
            jump case2_scene3B
        "Really? Deep learning again?":
            jump case2_scene3C
        "I know. I’m a huge fan of deep learning. It’s better than anything else at the moment.":
            jump case2_scene3D
    return

label case2_scene3A:

    scene bg hospital
    show happy_supervisor
    "Your sarcasm and apparent disdain for deep learning amuses me."
    jump case2_q8
return

label case2_scene3B:

    scene bg hospital
    show happy_supervisor
    "Well, now you do. Deep learning has been the basis of all the state-of-the art computer aided diagnosis systems that have been produced in the last decade or so, and a lot of research is being done on deep learning architectures to improve results even further."
    jump case2_q8
return

label case2_scene3C:

    scene bg hospital
    show happy_supervisor
    "...Clearly you're not a fan of it."
    "Unfortunately, until another state of the art appears, we're stuck with deep learning outperforming all traditional approaches."
    "And it's important for your algorithm, deep learning or not, to perform well in the medical field."
    jump case2_q8
return

label case2_scene3D:

    scene bg hospital
    show happy_supervisor
    "Ah yes, it has been outperforming other algorithms in every aspect so far."
    jump case2_q8
return

label case2_q8:

    scene bg hospital
    show supervisor
    "But of course, it's important to evaluate the deep learning algorithm."
    "Usually, for detection tasks such as the one we’re trying to perform, do you know which metric can be unreliable?"
    python:
        start_time = time()
    menu:
        "Accuracy":
            jump case2_q8_correct        
        "Precision":
            jump case2_q8_incorrect
        "Sensitivity":
            jump case2_q8_incorrect
        "Specificity":
            jump case2_q8_incorrect
    return 

label case2_q8_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, you are correct, accuracy is the correct answer."

    jump case2_q9
return

label case2_q8_incorrect:

    scene bg hospital
    show supervisor
    "No, your answer is incorrect. The right answer is accuracy."

    jump case2_q9
return

label case2_q9:

    scene bg hospital
    show supervisor    
    "Accuracy is not the most reliable because of many reasons. I'll explain why following my next question for you."

    "Do you know why accuracy is not reliable when measuring the performance of algorithms performing detection in the medical field?"
    python:
        start_time = time()
    menu:
        "It overfits":
            jump case2_q9_incorrect        
        "It causes biased results due to unbalanced data":
            jump case2_q9_correct
        "It gives results that are not explainable":
            jump case2_q9_incorrect
        "Medical data is different from data used in other data science fields":
            jump case2_q9_incorrect
    return 


label case2_q9_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "That's correct, it's due to the results being biased for unbalanced data."

    jump case2_q10
return

label case2_q9_incorrect:

    scene bg hospital
    show supervisor
    "No, your answer is incorrect. It's due to the results being biased for unbalanced data."

    jump case2_q10
return

label case2_q10:
    
    scene bg hospital
    with fade
    show supervisor

    "Accuracy is a metric that causes biased results for severely imbalanced data."
    "Unfortunately in the medical domain, most of the data is unbalanced."
    "or example, in a case of detecting benign versus malignant lesions in breast cancer, since most lesions are benign, the accuracy might be very high, but this would not be because the algorithm is performing well.0"
    "But it could be because the algorithm is detecting all the data from the majority class only, the benign class, and it’s classifying most lesions as benign."
    "So if 90 perfecnt of the lesions are benign, and the algorithm is only learning and detecting benign lesions, then it will give a training accuracy of 90\%."
    "However, it is not detecting the malignant lesions at all, so despite having a high accuracy- which will likely be the case for the validation set as well."
    "And since the data distribution will be the same, the high accuracy is misleading since the algorithms performs poorly when detecting malignant lesions."
    "It only APPEARS to be performing well because of the number of cases of malignant lesions being low."
    "This means that the results are completely biased towards one class only, since the algorithm is not performing well when detecting the malignant class."
    "The metric itself does not cause overfitting, since it’s not a trainable parameter, and the results given by it are explainable for balanced classes."
    " Medical data in the end is still data, and all data science approaches that are applicable to other kinds of data are applicable to medical data, hence why that’s also not the reason for accuracy not being applicable there."
    scene bg hospital
    with fade
    show happy_supervisor
   
    "Dealing with imbalanced data is indeed a huge problem."
    "We have to use other metrics to make sure the algorithm is actually performing well in detecting the presence of the disease."

    "For deep learning, the nice thing is that the model automatically trains to perform better."
    "But the reason it updates its parameters depends on one specific factor."

    "What causes the parameters of a neural network to be updated?"

    python:
        start_time = time()
    menu:
        "Activation function":
            jump case2_q10_incorrect        
        "Loss function":
            jump case2_q10_correct
        "Number of hidden layers":
            jump case2_q10_incorrect
        "Feature maps":
            jump case2_q10_incorrect
    return 

label case2_q10_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, loss function is the correct answer."

    jump case2_q11
return

label case2_q10_incorrect:

    scene bg hospital
    show supervisor
    "No, the correct answer is the loss function."

    jump case2_q11
return

label case2_q11:

    scene bg hospital
    with fade
    show supervisor
    "In order for the parameters of a neural network, meaning the weights, to be updated, the loss function must change."
    "The loss function in essence controls the way the network learns, and without a differentiable loss function, gradient descent cannot occur, and weights cannot be updated."
    "The activation function allows complex learning, and the number of hidden layers increase the complexity of the network, but these are not used to update the model."
    "Same with feature maps- these feature maps are used to extract data, but the model will still not be updated with just the feature maps."
    with fade
    show happy_supervisor
    "Alright, so with the case we were dealing with before, it seems that the doctor has given an assessment of BI-RADS class 3."
    "You've mentioned during your application that you know about this from one of the courses in the past semester, so that's great."
    "What is the likelihood of cancer and the next step for an assessment of BI-RADS 3?"
  
    python:
        start_time = time()
    menu:
        "Benign & continue routine screening":
            jump case2_q11_incorrect        
        "Benign & repeat mammogram in six months":
            jump case2_q11_incorrect
        "Probably benign & continue routine screening":
            jump case2_q11_incorrect
        "Probably benign & repeat mammogram in six months":
            jump case2_q11_correct        
        "Suspicion for malignancy & repeat mammogram in six months":
            jump case2_q11_incorrect
    return 
  

label case2_q11_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, your answer is correct."

    jump case2_q12
return

label case2_q11_incorrect:

    scene bg hospital
    show supervisor
    "No, that's incorrect."

    jump case2_q12
return

label case2_q12:
    scene bg hospital
    with fade
    show supervisor
    "A BI-RADS score of 3 is associated with an assessment of the suspected lesion probably being benign, and it is recommended that the patient undergo another mammogram after 6 months."
    "However, the patient has a family history of breast cancer. In this case, it is recommended that more tests be performed now."
    "By the way….. the doctor asked if we could reduce the number of false positives detected."
    "Usually, having a high sensitivity comes at the expense of having too many false positives."
    "So it’s understandable that she wants the false positives to be decreased."

    "That is why, in deep learning, the ROC curve is used to represent this."

    "What is in the x-axis and y-axis of the ROC curve?"
    python:
        start_time = time()
    menu:
        "True positive rate and false positive rate":
            jump case2_q12_incorrect        
        "average false positives and true positives":
            jump case2_q12_incorrect
        "sensitivity and specificity":
            jump case2_q12_incorrect
        "false positive rate and sensitivity":
            jump case2_q12_correct    
    return 


label case2_q12_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, your answer is correct. False positive rate and sensitivity is the right one."

    jump case2_q13
return

label case2_q12_incorrect:

    scene bg hospital
    show supervisor
    "No, that's incorrect. The correct answer is false positive rate and sensitivity."

    jump case2_q13
return
  
label case2_q13:
    scene bg hospital
    show supervisor

    "An ROC curve has the sensitivity (also known as the true positive rate) on the vertical y-axis."
    "The false positive rate, or 1-specificity goes into the horizontal x-axis."
    "I suggest that we try building a more sophisticated algorithm that will take the false positives into account and reduce them."
    show happy_supervisor
    "We can work more on it in the upcoming days."
    "The case of this particular patient is complete for now."
    "Well done!"
    jump case3_scene1
return

label case3_scene1:
    scene bg hospital
    with fade
    show happy_supervisor

    "Alright! Now we are heading to your last challenge... are you ready for it? "

    menu: 
        "Yes! I am looking forward to it":
            jump case3_scene1A
        
        "No, I am actually quite tired and would rather go home":
            jump case3_scene1B

label case3_scene1A:
    scene bg hospital
    with fade
    show happy_supervisor

    "Great! I am glad you are still very energetic after the past two cases. Just one more and you will be done with your first day of your internship."
    "After this first training and evaluation day, you will be officially part of our R&D team!"
    jump case3_scene2

return

label case3_scene1B:
    scene bg hospital
    with fade
    show angry_supervisor

    "Hmm.. that's a little bit sad to hear. However, your shift ends at 5 pm. 2 hours more to go!"
    jump case3_scene2

return


label case3_scene2:

    scene bg hospital
    with fade
    show supervisor

    "The emergency department has received the case of a female american patient aged 55 who has been feeling chest pain during the last week."
    "She indicates that the pain has been inconsistent (some days more than others), but it always comes in with different levels of intensity."
    "When reviewing her family tree it has been found that her grandparents had heart disease and some other members of her family had obesity. She got a physical examination and it was found that her BMI is normal."
    "However, she got some blood tests and high levels of triglycerides and cholesterol were found, and also a heart functioning test was conducted and some abnormalities were found."
    "Since this is an alarming symptom for patients having heart disease, she has been brought to the imaging department in order to do further evaluation of her medical condition."
    
    jump case3_q1
return

label case3_q1:

    scene bg hospital
    with fade
    show supervisor

    "Let's start revising your concepts. Which one is typically the first medical test performed to study the heart's functioning?"
    python:
        start_time = time()
    menu:
        "EEG":
            jump case3_q1_incorrect

        "ECG":
            jump case3_q1_correct

        "Holter monitor":
            jump case3_q1_incorrect

        "EMG":
            jump case3_q1_incorrect
return

label case3_q1_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, your answer is correct!"
    "ECG, which stands for Electrocardiogram, is the first medical test performed when doctors want to analyze the electrical activity of the heart (and thus its functioning) due to the fact that it’s quick and cheap."
    "Other studies such as Holter monitors are used when the patient has irregular arrhythmias that get masked by ECG machines."
    "EEG and EMG stand for encephalogram and electromyography, and these tests study the electrical activity of the brain and muscles, respectively."
    jump case3_q2
return

label case3_q1_incorrect:
    scene bg hospital
    show supervisor
    "No, that one is not the correct answer. The correct answer is ECG."
    "ECG, which stands for Electrocardiogram, is the first medical test performed when doctors want to analyze the electrical activity of the heart (and thus its functioning) due to the fact that it’s quick and cheap."
    "Other studies such as Holter monitors are used when the patient has irregular arrhythmias that get masked by ECG machines."
    "EEG and EMG stand for encephalogram and electromyography, and these tests study the electrical activity of the brain and muscles, respectively."
    jump case3_q2
return

label case3_q2:

    scene bg hospital
    with fade
    show supervisor

    "The first thing that should be done when analyzing the heart’s functioning is performing an ECG analysis."
    "We have received the result of the ECG exam from the patient, and the idea is to analyze it computationally."
    "The equipment used for acquiring the signal has an operating frequency of 125Hz." 
    "If we wanted to analyze the heart’s behavior for approximately one minute, what would be the number of samples we should take from the signal?."
    python:
        start_time = time()
    menu:
        "4000 samples":
            jump case3_q2_incorrect

        "6000 samples":
            jump case3_q2_incorrect

        "8000 samples":
            jump case3_q2_correct

        "3600 samples":
            jump case3_q2_incorrect
return

label case3_q2_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, your answer is correct!"
    
    scene bg hospital
    with fade
    show equation_frequency:
        xpos 400
        ypos 300
    "125Hz = 125 samples/second. Therefore, applying the equation above you get that the answer is 8000 samples."
    jump case3_scene3
return

label case3_q2_incorrect:
    scene bg hospital
    show supervisor
    "No, that one is not the correct answer. The correct answer is 8000 samples."
    scene bg hospital
    with fade
    show equation_frequency:
        xpos 400
        ypos 300
    "125Hz = 125 samples/second. Therefore, applying the equation above you get that the answer is 8000 samples."
    jump case3_scene3
return

label case3_scene3:

    scene bg hospital
    with fade
    show supervisor

    "Great! Now you know how to analyze 1 minute of signal. You’ll have to work on a small jupyter notebook activity where you are required to compute the following data:"
    "Patients heart rate (bpm)."
    "Number of R peaks in the signal for one minute."

    "For this, we will be working with BiosPPY, a python library designed for the analysis and processing of biomedical signals."

    "However, it won’t be that easy. The signal file of the notebook is encrypted with a password that you will have to discover solving the following sliding puzzle: {a=https://puzzel.org/es/slidingpuzzle/play?p=-NIXjdu287YO_05Jmth8} puzzle{/a} "

    python:
        while True: 
            password = renpy.input("What's the password of the file?") 
            if password=="15478563":
                renpy.say(None,"Great!, that's the correct password. You can now go to the python notebook activity.")
                break
            else: 
                renpy.say(None,"That's not the correct password. Try again.")
    
    "The notebook activity is available in the following link: {a=https://puzzel.org/es/slidingpuzzle/play?p=-NIXjdu287YO_05Jmth8} notebook{/a}. All instructions to run it are given there."
    "Based on the notebook activity, you will have to answer the following 3 questions."
    jump case3_q3

return

label case3_q3:

    scene bg hospital
    with fade
    show supervisor

    "What is the mean heart rate (bpm) of the patient during the first minute of the signal?"
    python:
        start_time = time()
    menu:
        "130.08 bpm":
            jump case3_q3_incorrect

        "131.08 bpm":
            jump case3_q3_correct

        "132.08 bpm":
            jump case3_q3_incorrect

        "133.08 bpm":
            jump case3_q3_incorrect
return

label case3_q3_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, your answer is correct!"
    jump case3_q4
return

label case3_q3_incorrect:
    scene bg hospital
    show supervisor
    "No, that one is not the correct answer. The correct answer is 131.08 bpm"
    jump case3_q4
return

label case3_q4:

    scene bg hospital
    with fade
    show supervisor

    "What is the standard deviation of the patient’s mean heart rate during the first minute of the signal?"
    python:
        start_time = time()
    menu:
        "20.91":
            jump case3_q4_correct

        "21.91":
            jump case3_q4_incorrect

        "22.91":
            jump case3_q4_incorrect

        "23.91":
            jump case3_q4_incorrect
return

label case3_q4_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, your answer is correct!" 
    jump case3_q5
return

label case3_q4_incorrect:
    scene bg hospital
    show supervisor
    "No, that one is not the correct answer. The correct answer is 20.91."
    jump case3_q5
return

label case3_q5:

    scene bg hospital
    with fade
    show supervisor

    "What is the number of R peaks in the signal during the first minute?"
    python:
        start_time = time()
    menu:
        "146":
            jump case3_q5_incorrect

        "147":
            jump case3_q5_incorrect

        "148":
            jump case3_q5_incorrect

        "149":
            jump case3_q5_correct
return

label case3_q5_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, your answer is correct!" 
    jump case3_scene4
return

label case3_q5_incorrect:
    scene bg hospital
    show supervisor
    "No, that one is not the correct answer. The correct answer is 149 R peaks."
    jump case3_scene4
return

label case3_scene4:
    scene bg hospital
    show happy_supervisor
    "Hey! important information"
    "Knowing the mean heart rate of a patient, as well as its standard deviation are useful features to consider when analyzing ECG signals."
    "Knowing the number of R peaks can help calculating some other meaningful features such as the duration of R-R interval."
    "BiosPPy library can be used for analyzing some other types of biomedical signals such as EEG, EDA, and EMG, so it might be useful for you in the future."
    jump case3_q6
return 

label case3_q6:
    scene bg hospital 
    show supervisor 
    "Based on the data previously calculated, what would you say about the current mean heart rate of the patient?"
    python:
        start_time = time()
    menu:
        "It is low, since the normal level is around 150-180 bpm":
            jump case3_q6_incorrect

        "It is low, since the normal level is around 140-160 bpm":
            jump case3_q6_incorrect

        "It is high, since the normal level is around 60-100 bpm":
            jump case3_q6_correct

        "It is high, since the normal level is around 50-100 bpm":
            jump case3_q6_incorrect
return 

label case3_q6_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, your answer is correct!" 
    "Normal levels for mean heart rate are around 60-100 bpm."
    jump case3_q7
return

label case3_q6_incorrect:
    scene bg hospital
    show supervisor
    "No, that one is not the correct answer. The correct answer is 60-100 bpm, as those are the normal levels for mean heart rate."
    jump case3_q7
return

label case3_q7:
    scene bg hospital 
    show supervisor 
    "As you see, the patient has all the clinical setup to be suspected of having heart disease. Therefore, some more in-depth studies should be performed."
    "You have the possibility to perform four different tests on the patient:"
    "1)	a non-invasive and quick test to look at the heart functioning"
    "2) a technique that allows you to look at the texture of the heart muscle and detect possible inflammations"
    "3) a non-invasive test able to capture fine-details images of the heart, specially the coronary arteries"
    "4) an invasive test test that is able to give the clearest pictures of blockages in the arteries."
    "Which imaging technique corresponds to each of the given situations?"
    python:
        start_time = time()
    menu:
        "Cardiac MRI, Cardiac CT, Echocardiography (ultrasound), invasive coronary angiography. ":
            jump case3_q7_incorrect

        "Cardiac MRI, Echocardiography (ultrasound), Cardiac CT, invasive coronary angiography.":
            jump case3_q7_incorrect

        "Echocardiography (ultrasound) , Cardiac MRI, Cardiac CT, invasive coronary angiography":
            jump case3_q7_correct

        "Echocardiography (ultrasound), Cardiac CT, cardiac MRI, invasive coronary angiography":
            jump case3_q7_incorrect
return 

label case3_q7_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, your answer is correct!" 
    "Echocardiography is the safest and least invasive test for checking at the heart’s functioning."
    "However, it might not be the most adequate technique as it might be difficult to look at finer details in an ultrasound."
    "Cardiac MRI is particularly useful to look at the texture of the heart muscle, and requires the injection of a contrast agent."
    "CT scans are particularly useful to have a detailed look of the coronary arteries (though it requires some radiation)."
    "Invasive coronary angiography gives the clearest picture regarding blockages in the arteries as it involves the passing of a thin tube from the wrist to the heart."
    jump case3_q8
return

label case3_q7_incorrect:
    scene bg hospital
    show supervisor
    "No, that one is not the correct answer. The correct answer is  Echocardiography (ultrasound) , Cardiac MRI, Cardiac CT, invasive coronary angiography" 
    "Echocardiography is the safest and least invasive test for checking at the heart’s functioning."
    "However, it might not be the most adequate technique as it might be difficult to look at finer details in an ultrasound."
    "Cardiac MRI is particularly useful to look at the texture of the heart muscle, and requires the injection of a contrast agent."
    "CT scans are particularly useful to have a detailed look of the coronary arteries (though it requires some radiation)."
    "Invasive coronary angiography gives the clearest picture regarding blockages in the arteries as it involves the passing of a thin tube from the wrist to the heart."
    jump case3_q8
return

label case3_q8:
    scene bg hospital 
    show supervisor 
    "Once knowing the scopes of each of the tests, and based on the symptoms referred by the patient and her clinical history, what would be the most adequate test to be done for further study in this case?"
    python:
        start_time = time()
    menu:
        "Cardiac CT":
            jump case3_q8_correct

        "Echocardiography":
            jump case3_q8_incorrect

        "Invasive coronary angiography":
            jump case3_q8_incorrect

return 

label case3_q8_correct:
    python:
        end_time = time()
        seconds_elapsed = end_time - start_time
    
    $score = score + float(1/seconds_elapsed)*10.0
    $score_round = "{:6.2f}".format(score)
    show screen stat_screen(score_round) 

    scene bg hospital
    show happy_supervisor
    "Yes, your answer is correct!" 
    "Since there are clinical symptoms and enough evidence that the patient might be having heart disease, the best imaging technique would be a cardiac CT to evaluate the current state of the patient’s arteries."
    "An echocardiography is performed as a first step and as a routinary check, but it is easy to notice that for this case it would not provide enough relevant/useful information."
    "If the situation of the patient is severe, she might require an invasive coronary angiography."

    jump case3_final_scene
return

label case3_q8_incorrect:
    scene bg hospital
    show supervisor
    "No, that one is not the correct answer. The correct answer is  Cardiac CT"
    "Since there are clinical symptoms and enough evidence that the patient might be having heart disease, the best imaging technique would be a cardiac CT to evaluate the current state of the patient’s arteries."
    "An echocardiography is performed as a first step and as a routinary check, but it is easy to notice that for this case it would not provide enough relevant/useful information, since arteries are not clearly visible in ultrasound."
    "If the situation of the patient is severe, she might require an invasive coronary angiography as a last resource." 
    jump case3_final_scene
return

label case3_final_scene:
    scene bg hospital
    call screen happy_supervisor

    "You are done on your first day of the internship, congratulations!"
    "Your final score was [score_round] points"
    call screen stat_screen(score_round) 







