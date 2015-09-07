START STREAM
ffmpeg -s 320x240  -i /dev/video0 -f rtp rtp://127.0.0.1:8874


CHECK FORMATS ON DEVICE
ffmpeg -f video4linux2 -list_formats all -i /dev/video0




