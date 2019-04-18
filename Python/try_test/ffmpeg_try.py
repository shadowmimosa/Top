import os, json
import ffmpeg


def write_file(content):
    content_type = type(content)
    with open("./probe.json", 'a') as fn:
        if content_type != str:
            fn.write(json.dumps(content))
        else:
            fn.write(content)
        fn.write('\n')


def video_info(video_path):
    try:
        ff_info = ffmpeg.probe(video_path)
    except ffmpeg.Error as exc:
        print(exc)
    else:
        write_file(ff_info)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # video_info(
    #     r"C:/Users/ShadowMimosa/Documents/GitRepository/Top/Top/Python/reptile/down_mp4/5beb9dce9c68d1a465fe122b.mp4"
    # )
    # video_info(
    #     r"C:\Users\ShadowMimosa\Documents\GitRepository\Top\Top\Python\reptile\down_mp4\5beb9dce9c68d1a465fe122b\index0.ts"
    # )
    # video_info(
    #     r"C:\Users\ShadowMimosa\Documents\GitRepository\Top\Top\Python\reptile\down_mp4\5beb9dce9c68d1a465fe122b\index1.ts"
    # )    
    # video_info(
    #     r"C:\Users\ShadowMimosa\Documents\GitRepository\Top\Top\Python\reptile\down_mp4\5beb9dce9c68d1a465fe1243\m3u8.mp4"
    # )
    # ffmpeg.concat()

    path = "Python\reptile\down_mp4\5beb9dce9c68d1a465fe1243"

    with open(path,'r') as fn:
        
