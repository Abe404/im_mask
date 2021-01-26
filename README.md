# im_mask
mask a folder of images with a folder of masks

Make sure you have python3 and pip installed (or conda etc)

## To install the dependencies (if you use pip)
> pip install -r requirements.txt

## how to run (example)
> python main.py --imagedir ./images --maskdir ./masks --outputdir ./masked

## Extra information
> 
> usage: main.py [-h] --imagedir IMAGEDIR --maskdir MASKDIR --outputdir
>                OUTPUTDIR
> 
> 
> optional arguments:
> 
> 
>   -h, --help            show this help message and exit
> 
> 
>   --imagedir IMAGEDIR   location of directory containing images to mask
> 
> 
>   --maskdir MASKDIR     location of directory where masks are located
> 
> 
>   --outputdir OUTPUTDIR
>                         location of directory where masked images will be
>                         saved
