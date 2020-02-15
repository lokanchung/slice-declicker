import librosa as rosa
import numpy as np
import soundfile as sf

def process(in_path, out_path):
    wav, sr = rosa.load(in_path, sr=44100, mono=False)

    left = wav[0]
    right = wav[1]

    samp = 441

    def smoothstep(x):
        return 3*x*x - 2*x*x*x

    def crossfade(x):
        return smoothstep(1-x), smoothstep(x)

    def append_with_crossfade(a, b, l):
        out = a.copy()

        for i in range(0, l):
            tail = len(a) - l + i
            

            x = i / l

            ca, cb = crossfade(x)

            out[tail] = out[tail] * ca + b[i] * cb
        
        return np.append(out, b[l:])

    st_left = rosa.effects.time_stretch(left[-samp * 2:], 0.5)
    out_left = append_with_crossfade(left, st_left, samp*2)
    st_right = rosa.effects.time_stretch(right[-samp*2:], 0.5)
    out_right = append_with_crossfade(right, st_right, samp*2)

    print(in_path, len(out_right))

    out = np.column_stack([out_left, out_right])
    for i in range(1, samp+1):
        j = len(out) - i
        a = i / samp
        out[j, 0] *= a
        out[j, 1] *= a

    sf.write(out_path, out , 44100, 'PCM_16')


if __name__ == "__main__":
    import itertools
    from pathlib import Path
    import sys

    if len(sys.argv) == 1:
        cwd = Path('.')
    else:
        cwd = Path(sys.argv[1])
        
        if not cwd.is_dir():
            print('directory not found!')
            exit()

    backup_dir = cwd / 'backup'

    for i in itertools.count():
        if not backup_dir.exists():
            break
        backup_dir = cwd / ('backup_' + str(i))
    
    backup_dir.mkdir()

    for p in cwd.glob("*.wav"):
        import shutil
        backup_path = backup_dir / p.name
        shutil.copy(p, backup_path)

        process(str(p), str(p))
