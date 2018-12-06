ffmpeg -i dragon.mp4 -s 1280x720 \
    -vcodec libx264 -crf 25  -pix_fmt yuv420p \
    output.mp4
