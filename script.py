import os
import librosa
import soundfile as sf

def resample_wav_files(directory, target_sr=24000):
    # 遍历目录及其子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):
                # 获取当前文件的完整路径
                file_path = os.path.join(root, file)
                # 加载音频文件，sr=None 表示保持原始采样率
                y, sr = librosa.load(file_path, sr=None)
                if sr != target_sr:
                    print(f"Resampling {file_path} from {sr}Hz to {target_sr}Hz")
                    # 重采样音频
                    y_resampled = librosa.resample(y, orig_sr=sr, target_sr=target_sr)
                    # 保存重采样后的文件，覆盖原始文件
                    sf.write(file_path, y_resampled, target_sr)
                    print(f"Resampled file saved: {file_path}")

# 使用函数，替换为你的目标目录路径
directory_path = "./data/diversity"
resample_wav_files(directory_path)
