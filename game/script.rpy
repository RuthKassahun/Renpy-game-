define config.rollback_enabled = False

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
image bg hospital="hospital_1.jpg"
image Laplacian_filter=im.Scale("Laplacian_filter.jpg",621,308)
image bg white="bg_white_.jpg"
image supervisor="Supervisor_speaking_resi.png"
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


# The game starts here.

default score = 0

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg hospital_1

    scene bg hospital
    with fade
    show supervisor
         


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue. 

    "Dear Y, My name is X, and I will be your supervisor on your first day as an intern in the
    hospital."
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
    

    menu:
        
        #"Which filter is this?"
        
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
    show medical note:
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
    show medical note:
         xpos 400
         ypos 100


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

    
    $ score += 1
    
    screen text_example():
    frame:
        xalign 0.5 ypos 50
        text "Score: [score]."
            size 30
 
       
 

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
    show medical note:
         xpos 400
         ypos 100

    "Well, The correct answer is MRI."
    "The gold standard imaging modality to assess the presence of axional inflammation in
    multiple sclerosis is MRI."

    jump q3

return

label correct_2:

    scene bg hospital
    show medical note:
         xpos 400
         ypos 100

    "Awesome! As you saidThe gold standard imaging modality to assess the presence of axional inflammation in
    multiple sclerosis is MRI."
    $ score += 1
    jump q3

return

label q3:

    scene bg hospital
    with fade
    show supervisor

    "CT Scans are preferably used instead of MRI since they cost half the price and are much faster.
    However, why would you think MRI is preferred to be used when examining the brain for detecting
    diseases such as MS?" 

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
    show medical note:
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
    show medical note:
         xpos 400
         ypos 100

    "That's right. As compared to CT, MRI scans provide more pronounced image quality around white
    matter (where most of the lesions of MS are typically located), since they have excellent tissue contrast."
    "As the MS affects the myelin coats around the nerve, MRI can easily detect the regions
    where the myelin is missing. "
    "CT is mainly used for screening fractures, as it provides structural images
    of organs, tissues and bones. CSF spinal fluid tap testing is another important method to analyze a
    patient's auto immune around the brain and spinal cord."
    $ score += 1
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
    show medical note:
         xpos 400
         ypos 100
    "Well,as it can be observed, image one has some lesions around the area of white matter,
     so that one corresponds to MS. "

    jump q5
return

label correct_4:
    scene bg hospital
    show medical note:
         xpos 400
         ypos 100

    "Well done! as it can be observed, image one has some lesions around the area of white matter,
     so that one corresponds to MS. "
    $ score += 1
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
    show medical note:
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
    show medical note:
         xpos 400
         ypos 100

    "That's correct.Awesome! "
    $ score += 1
    jump q6
return

label q6:
    scene bg hospital
    with fade
    show supervisor

    "Since filtering is the correct method to get denoised images, which filter do you think would work best in 
    removing the type of noise that exists in these images?"

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
    show medical note:
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
    show medical note:
         xpos 400
         ypos 100

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
    $ score += 1
    jump q7
return

label q7:
    scene bg hospital
    with fade
    show supervisor

    "You’re doing well answering these questions. However, working with these images also requires additional 
    preprocessing steps since all images do not have the same quality after being acquired."
    "In addition to denoising the artifacts, what other methods do you recommend for pre-processing of the MRI scan?"

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
    show medical note:
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
        xpos 400
        ypos 100
    "This would be the image obtained after denoising. As you see, the lesions are easier to spot. Especially those smallest ones usually can be seen fingers apart."
    jump q8
return

label correct_7:
    scene bg hospital
    show medical note:
         xpos 400
         ypos 100
    "That's right. To enhance the intensity of the acquired MRI image, normalization of the intensity is a relevant procedure. "
    "This will fix the range of each brain tissue  intensities with a considerable amount of variation resulting in a 
    well contrasted image. "
    " Typically the scanned MRI images will not be maximized to output high resolution images. "
    "This procedure is resource intensive as it will reconstruct each voxel back to higher resolution."
    " Color normalization is not required as the MRI scanned images are gray level intensity images. "
    scene bg hospital
    with fade
    show other_brain
    "This would be the image obtained after denoising. As you see, the lesions are easier to spot. Especially those smallest ones usually can be seen fingers apart."
    $ score += 1
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
    show medical note:
         xpos 400
         ypos 100
    "Hmmm actually to enhance  the ring effect gadolinium contrast agent is applied in T1-weighted image. "
    "This is usually the case for tumefactive multiple sclerosis where the tumor-like lesions appear like a ring shape around the ventricles."
    "Morphological gradients can also result in getting the contours around the tumor however there are other small insignificant structures that will be enhanced along the way."
    scene bg hospital
    with fade
    show saggital_brain_enhanced:
        xpos 400
        ypos 100
    "After applying the gadolinium contrast this is the result we will get. Now the rings can be clearly seen. "
    jump q9
return

label correct_8:
    scene bg hospital
    show medical note:
         xpos 400
         ypos 100
    "That's correct indeed to enhance  the ring effect gadolinium contrast agent is applied in T1-weighted image. "
    "This is usually the case for tumefactive multiple sclerosis where the tumor-like lesions appear like a ring shape around the ventricles."
    "Morphological gradients can also result in getting the contours around the tumor however there are other small insignificant structures that will be enhanced along the way."
    scene bg hospital
    with fade
    show saggital_brain_enhanced:
        xpos 400
        ypos 100
    "After applying the gadolinium contrast this is the result we will get. Now the rings can be clearly seen. "
    $ score += 1
    jump q9
return

label q9:
    scene bg hospital
    with fade
    show supervisor

    "Now, since we have the denoised and preprocessed image, we can clearly see the locations of the lesions. "


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
    show medical note:
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
    show medical note:
         xpos 400
         ypos 100
    "You're correct. Multiple sclerosis will most likely have lesions that could be found in proximity of the  ventricular region."
    "Commonly, these lesions have the shape of a finger and are therefore known as Dawson’s fingers. "
    "The lesions can be seen pointing away from the lateral ventricles. Usually MRI scanners don't display the lesions found around the dark matter"
    " instead the majority of the lesions can be depicted around the white matter and the bottom of the fourth ventricle."
    $ score += 1
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
    show medical note:
         xpos 400
         ypos 100
    "Hmmmm that's not right as the T1-weighted sequence shows high contrast between gray matter and white matter regions"
    " it’s mainly applicable for segmentation tasks. In cases of multiple sclerosis, T2-weighted sequence is better at localizing lesion regions"
    "as it provides high lesion-to-brain contrast and lesions appear hyper-intense in these sequences."
    jump q11
return

label correct_10:
    scene bg hospital
    show medical note:
         xpos 400
         ypos 100
    "Correct! as the T1-weighted sequence shows high contrast between gray matter and white matter regions"
    " it’s mainly applicable for segmentation tasks. In cases of multiple sclerosis, T2-weighted sequence is better at localizing lesion regions"
    "as it provides high lesion-to-brain contrast and lesions appear hyper-intense in these sequences."
    $ score += 1
    jump q11
return

label q11:
    scene bg hospital
    with fade
    show supervisor

    "There is still a lot of information in the MRI scans that we don’t need. One of these is the skull, and we only need brain tissue specifically for our purposes."
    "As you might already know skull stripping is a principal preprocessing step to differentiate brain and non-brain tissue."

    "Do you think the presence of a lesion will affect the accuracy of skull stripping?"
    menu:
        "Yes":
            jump incorrect_11

        "No":
            jump incorrect_11
    
    return
label incorrect_11:
    scene bg hospital
    show medical note:
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
    show medical note:
         xpos 400
         ypos 100
    "Wonderful, That's that's excellent. The intensity distribution of tissues affected by lesion is different thus the skull stripping couldn’t be the same as that of the normal tissue."
    "See? This is why it’s very important to perform skull-stripping. Have you used any softwares before for skull stripping?"
    $ score += 1
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
    show medical note:
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
    show medical note:
         xpos 400
         ypos 100
    "Awesome! That's indeed the correct answer. There are many evaluation methods used to quantify the quality of the segmentation, and all the metrics mentioned can be used for this task. "
    "Hausdorff distance only takes spatial distance between points into account, and dice score and jaccard index are based on the degree of overlap the segmented images have with the ground truth."
    "Volumetric similarity considers the differences in volume only, and does not take the distance between points or overlap of segmented regions into consideration. "
    "In cases where the outer contour and degree of overlap are not of importance, but only the magnitude of the segmented volume is necessary, volumetric similarity is most appropriate. "
    $ score += 1
    jump q13
return

label q13:
    scene bg hospital
    with fade
    show supervisor

    "So we know that volumetric similarity is more appropriate for this task. But when the shape of the lesion is of importance, do you know which metric should be used?"

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
    show medical note:
         xpos 400
         ypos 100
    "The correct answer is Hausdorff distance. "
    "Distance metrics that are spatial based, such as Hausdorff distance, provide information about the dissimilarity of the shape."
    "Other metrics only consider the percentage of overlap between the different segmentations. "
    jump q14
return

label correct_13:
    scene bg hospital
    show medical note:
         xpos 400
         ypos 100
    "As you said the correct answer is Hausdorff distance. "
    "Distance metrics that are spatial based, such as Hausdorff distance, provide information about the dissimilarity of the shape."
    "Other metrics only consider the percentage of overlap between the different segmentations. "
    $ score += 1
    jump q14
return

label q14:
    
    scene bg hospital
    with fade
    show supervisor

    "In MAIA clinic we have 25 cases of patients with Multiple sclerosis. We are studying these cases in our research and development department."
    "We want to register this particular patient MRI scan along with other patient MRI scans  in order to build a probabilistic atlas that will be used by you during the course of your thesis work."
    " In order to register the acquired image what registration techniques would you recommend?"
    "Which image registration method would you recommend?"

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
    show medical note:
         xpos 400
         ypos 100
    "Hmm it's actually prefered to perform affine registration followed by non-rigid registration "
    "To segment each brain tissue it is advised to register the intensity images beforehand. Linear transformation such as affine registration can be used initially to align the images. "
    "In some cases where the transformation is not linear, non-rigid registration techniques are used"
    jump q15
return  

label correct_14:
    scene bg hospital
    show medical note:
         xpos 400
         ypos 100
    "Well done! Ususally we perform affine registration followed by non-rigid registration "
    "To segment each brain tissue it is advised to register the intensity images beforehand. Linear transformation such as affine registration can be used initially to align the images. "
    "In some cases where the transformation is not linear, non-rigid registration techniques are used"
    $ score += 1
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
    show medical note:
         xpos 400
         ypos 100
    "Hmm well, the encoder’s goal is to compress the information of the images in terms of space but increasing the number of channels."
    "In each of the decoder steps there are skip connections placed so that the decoder is given enough context information for the generation of the segmentation masks. "

    jump q16
return  

label correct_15:
    scene bg hospital
    show medical note:
         xpos 400
         ypos 100
    "That's right, the encoder’s goal is to compress the information of the images in terms of space but increasing the number of channels."
    "In each of the decoder steps there are skip connections placed so that the decoder is given enough context information for the generation of the segmentation masks. "
    $ score += 1
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
        xpos 400
        ypos 80
    
    "Which statement about the graphs is true?"

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
    show medical note:
         xpos 400
         ypos 100
    "The answer isn't correct. Image 1 corresponds to training without dropout (thus overfitting), and image 2 corresponds to training with dropout (thus avoiding overfitting)"
    "As you can see, in the first image the  accuracy of the test set reaches its maximum value from the 600th iteration, and then overfitting takes place since the test accuracy decreases."
    "On the other hand, in the second image the test accuracy increases steadily, which is the behavior of a non-overfitting training."
    jump q17
return  

label correct_16:
    scene bg hospital
    show medical note:
         xpos 400
         ypos 100
    "The answer is correct. Well done! Image 1 corresponds to training without dropout (thus overfitting), and image 2 corresponds to training with dropout (thus avoiding overfitting)"
    "As you can see, in the first image the  accuracy of the test set reaches its maximum value from the 600th iteration, and then overfitting takes place since the test accuracy decreases."
    "On the other hand, in the second image the test accuracy increases steadily, which is the behavior of a non-overfitting training."
    $ score += 1
    jump q17
return 

label q17:
    scene bg hospital
    with fade
    show supervisor

    "It’s important to make sure that the model doesn’t overfit. The training of these deep learning models is controlled by the loss functions"
    "In general, there are a lot of loss functions that are well known and commonly used. Which of these is not a loss function?"
    
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
    show medical note:
         xpos 400
         ypos 100
    "Hmmm that's not the right answer. Softmax is an activation function, while the others are loss functions. Activation functions control whether a neuron will be activated or not and add non-linearity to enable complex learning."
    "Loss functions such as Focal, Binary Cross Entropy, and Mean Square Error, calculate the error in the learning process of the model to help evaluate the updates"
    "that need to be made to improve the model performance."

    jump q18
return 
    
label correct_17:
    scene bg hospital
    show medical note:
         xpos 400
         ypos 100
    "Yes, that's right softmax is an activation function, while the others are loss functions. Activation functions control whether a neuron will be activated or not and add non-linearity to enable complex learning."
    "Loss functions such as Focal, Binary Cross Entropy, and Mean Square Error, calculate the error in the learning process of the model to help evaluate the updates"
    "that need to be made to improve the model performance."
    $ score += 1
    jump q18
return

label q18:
    scene bg hospital
    with fade
    show CNN:
        xpos 400
        ypos 100

    "The architecture of the network proposed in the paper is presented in the following table."
    "However, some of its parts are missing (the ones inside the red boxes)."
    "Based on your deep learning knowledge and by analyzing the remaining data provided, how would you fill the gaps so that the model is coherent"

    
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
    show medical note:
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
    show medical note:
         xpos 400
         ypos 100
    "Wonderful! that's the correct answer."
    "The paper reviewed is one of the state-of-the-art performers in terms of detection of MS lesions, and you were able to see how important it is to select an appropriate activation function"
    "depending on the application, but also understand which are the best techniques to handle overfitting."
    "Now,  I want to show you the software we use here in MAIA Clinic. In our radiology department we use 3D slicer application to segment the brain tissue regions."
    "Here you can see the segmented brain scan."
    $ score += 1
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
    
    "Your overall point is [score]. Good Job!"
    




