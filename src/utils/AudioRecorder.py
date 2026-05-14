import sounddevice as sd
import soundfile as sf
import numpy as np

class AudioRecorder:

    def __init__(self, samplerate=16000):
        self.samplerate = samplerate
        self.recording = False
        self.frames = []
        self.stream = None

    def start(self):

        self.frames = []
        self.recording = True

        def callback(indata, frames, time, status):
            if self.recording:
                self.frames.append(indata.copy())

        self.stream = sd.InputStream(
            samplerate=self.samplerate,
            channels=1,
            dtype="float32",
            callback=callback
        )

        self.stream.start()

    def stop(self, filename="input.wav"):

        self.recording = False

        if self.stream:
            self.stream.stop()
            self.stream.close()

        audio = np.concatenate(self.frames, axis=0)
        sf.write(filename, audio, self.samplerate)

        return filename