
# Image Processing Based Wood Defect Detection 

> <h3> [STEP 1] </h3>
> <h3> Cropping of original images taken from the field </h3>

Canny edge detection was preferred to perform cropping on the original images. Canny Edge Detection detects the edges of the lamella part and then cropping is performed according to the minimum maximum coordinate information returned from the algorithm.<br>
In the Crop_with_canny_edge_detection file, cropping was performed on the original images from the oak_fungal folder.


> <h3> [STEP 2] </h3>
> <h3> Determination of HSV lower and upper band values </h3>

The images cropped in step 1 were saved in the oak_fungal_cropped_canny folder. Then, HSV settings suitable for the dataset were determined in the hsv_space_for_fungal_detection file via trackbar. <br>
The HSV values determined for the images with the same brightness value in the dataset are lower=([23,70,170]), upper ([50,255,255]).

> <h3> [STEP 3] </h3>
> <h3> Calculation of the percentage of fungal </h3>

As a result of the lower and upper values determined from the hsv_space_for_fungal_detection code file, only the mask that will highlight the fungal region on the image is created. The cropped image and the mask obtained were subjected to bitwise_and operation. Thus, only the areas with fungal are present on the final image.
The image matrix was traversed pixel by pixel and the number of coloured pixels was calculated. The ratio of the number of coloured pixels to the total number of pixels was found and the percentage of fungal on the lamella was calculated.

> <h3> [BONUS ***] </h3>
> <h3> Dataset </h3>
Dataseet consists of lamellae of oak wood type with fungus from defect classes. It is a special data set collected during solid panel production. 1861 pieces in total.
The entire dataset can be shared for academic collaborations and partnerships.
<br>
<br>
<br>

> <h3> INFORMATION </h3>
The developed code was applied on the images with the same amount of illumination in the dataset. HSV lower and upper values should be re-tuned when the amount of light changes.
