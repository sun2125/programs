from PIL import Image
import wave
import numpy
import sys
import array

FRAME_RATE = 44100

def make_wave_file(data, channel):
    w = wave.open("out.wav","w")                                    #waveファイルを開く
    w.setframerate(FRAME_RATE)                                      #フレームレートの設定
    w.setnchannels(channel)                                         #チャンネル数の設定（1:モノラル 2:ステレオ)
    w.setsampwidth(2)                                               #サイズの設定(1:8bit 2:16bit 3:24bit)
    w.writeframes(data)                                             #データの書き込み
    w.close()                                                       #waveファイルを閉じる

def read_bmp(fname1):
    img1 = Image.open(fname1)                                       #画像ファイルを開く(1)
    size = img1.size                                                #画像のサイズの取得
    data = []
    img1_rgb = img1.convert("RGB")                                  #画像をRGBへ変換(1)
    for i in range(size[0]):
        for j in range(size[1]):
            r1,g1,b1 = img1_rgb.getpixel((i,j))                     #RGB情報の取得(1)
            if i==0 and j==0:
                continue
            elif i==1 and j==0:
                channel = r1                                        #チャンネルの設定
            else:
                
                #data[i][j] = r1*256+r2-32768
                data.append(r1*256-32768)                           #データの追加
    return data,channel

def main():
    args = sys.argv
    #fname1 = input("ファイル名１を入力してください ")
    if len(args)<3:
        print("コマンドライン引数として")
        print("ファイル名 チャンネル数")
        print("を入力してください")
    else:
        fname1 = args[1]
        channel = (int)(args[2])
    tmp_data = []
    tmp_data, ch = read_bmp(fname1)
    #data = array.array(tmp_data)
    make_wave_file(array.array('h',tmp_data), channel)


main()
print("success")