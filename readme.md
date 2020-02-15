# slice-declicker
폴더 내의 wav파일에 타임 스트레치와 페이드 아웃을 적용시켜 음원 끝나는 지점에서 발생하는 클릭 노이즈를 제거합니다.

본 프로그램을 사용해서 발생하는 모든 문제에 대해서 책임지 않습니다.

Removes tail click noise by applying time-stretch and fade-out to the source.
Follow this guide and use at your own risk.

<b>
44100hz 16bit WAV만 지원합니다.<br/>
44100hz 16bit WAV ONLY!</b>

---

## Download & Installation
파이썬 사용법을 알고 있는 경우 slicke-declicker.py를 다운로드 하고 다음 Dependency를 설치합니다. 

If you are familiar with python, download slice-declicker.py and install the following dependencies
```
numpy<=1.17.0
librosa<=0.7.0
pySoundFile<=0.9.0
```
CLI Interface
```
python slice-declicker.py [directory-containing-wavs]
```
Example
```
python slice-declicker.py ./bgm
```
폴더 내의 모든 wav파일에 해당 처리가 적용되며 원본은 backup으로 시작하는 폴더 하에 저장됩니다.

All wav files will be processed and the originals will be moved to a new  folder starting with "backup". 

---

일반 사용자는 다음 링크에서 바이너리를 다운로드 합니다.

(For most users) Just download the binary from the following link.

```
```

다운로드 한 파일을 실행하면 실행 파일이 있는 폴더에 있는 모든 wav파일에 declick작업을 수행합니다. 원본은 backup으로 시작하는 폴더에 저장됩니다.

Execute the binary, then it will process all the wav files in the same folder, and the originals will be moved to a new folder starting with "backup".