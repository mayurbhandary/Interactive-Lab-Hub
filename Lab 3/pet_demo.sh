#arecord -f cd -r 16000 -d 5 -t wav recorded.wav && sox recorded.wav recorded_mono.wav remix 1,2

echo "how many pets do you have?"
arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
recorded=$(python3 pet_counter.py recorded_mono.wav)
echo $recorded