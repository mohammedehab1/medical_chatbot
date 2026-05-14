import soundfile as sf
import numpy as np
import librosa
import os

class AudioPreprocessor:

    @staticmethod
    def process(audio_path: str, output_path: str = None, target_sr: int = 16000):

        audio_array, sr = sf.read(audio_path)

        if isinstance(audio_array, np.ndarray) and len(audio_array.shape) > 1:
            audio_array = np.mean(audio_array, axis=1)

        if sr != target_sr:
            audio_array = librosa.resample(
                audio_array.astype(np.float32),
                orig_sr=sr,
                target_sr=target_sr
            )
            sr = target_sr

        if output_path is None:
            output_path = audio_path

        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

        sf.write(output_path, audio_array, sr)
        return output_path