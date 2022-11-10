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


# The game starts here.

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

    "Good morning. We have a busy day ahead of us. Let's start it off with a simple question:"
    scene bg hospital
    show Laplacian_filter:
         xpos 300
         ypos 300

    "Which filter is this?"

    menu:
        
        "Which filter is this?"
        
        "Gaussian Filter":

            jump incorrect

        "Laplacian Filter":

            jump correct

    # This ends the game.

    return

label incorrect:

    "Your answer is incorrect, this is a Laplacian filter"

    jump scene2


return

label correct:

    "Your answer is correct! Well done!"

    jump scene2


return

label scene2:

 
    scene bg hospital
    with fade
    show supervisor

    
    "What is the correct label for the MRI sequences?"

    scene bg hospital
    show mri2:
         xpos 400
         ypos 350
    
    menu:
        
        "What is the correct label for the MRI sequences?"
        
        "A - T1 and B - T1 FLAIR":

            jump incorrect_mri

        "A - T1 and B - T2":

            
            jump correct_mri

        "A - T1 and B - T2 FLAIR":

            jump incorrect_mri
    return
   
    


return

label correct_mri:

    "Well done!"

    jump third

return

label incorrect_mri:

    "The correct answer is : A - T1 and B - T2"

    jump third


return

label incorrect_radiology:

    "The correct answer is : Longer training period"

    #jump third


return

label third:

    scene bg hospital
    with fade
    show supervisor

    "Let's get going, we have a lot to do today." 


    scene bg radiology
    with fade
    show supervisor

    "Let me ask you something from a different topic then."
    "I assume you've worked with deep learning before as you have mentioned it quite often in your cv. So, tell me then: "

    scene bg radiology

    menu:
        
        "Which of these cannot be used to prevent a model from overfitting?"
        
        "Adding more data":

            jump incorrect_radiology

        "Early stopping":

            jump incorrect_radiology

        "Longer training period":

            jump correct
    return
return



