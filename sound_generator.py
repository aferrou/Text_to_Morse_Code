import wave
import array

sample_width = 2  # 2  bytes for a 16-bit WAV file
frame_rate = 44100 # common sample rate
duration = 0.3 

beep_samples = array.array('h', [int(32767.0 * 0.5) for _ in range(int(duration * frame_rate))])

with wave.open('beep.wav', 'w') as wav_file:
    wav_file.setnchannels(1) 
    wav_file.setsampwidth(sample_width)
    wav_file.setframerate(frame_rate)
    wav_file.writeframes(beep_samples.tobytes())