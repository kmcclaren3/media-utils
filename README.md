These are some media editing CLI files to support some ofthe common editing requirements of the World Language assessment program. They support 3 common use cases for editiing media files, and attempt to deskill the work into a simple command line application. Currently these are run via Python, buit should be converted to standard .EXE files for stand-alone usage. 

**mergevideo2.py** - This app will merge all video clips in a given directory passed as an argument and place them into an output file called merged.mp4. If a directory is not specified, it will merge the .mp4 files in the current (.) directory. 
Usage: $ python mergedvideo2.py <directory> 

**slowvideo5.py** - This app will slow the audio and video dopwn by a percentage, so it is more appropirrate for language learners.
Usage: $ python slowvideo5.py <inputvideo.mp4> <slowdown_percentage>

**videoclip.py** - This app will take a clip of video from the source file and write it out to the destination file. The .mp4 extension is optional on the arguements.    
Usage: $ python videoclip.py <input_file> <begin_timeclip> <end_timeclip> <destination_filename> <BR/>
Example: $python videoclip.py spanish12.mp4 1:07 1:53 spanish12_clipped

