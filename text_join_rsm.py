import chardet
import os

root_dir = "C:\\nlp\\ancient_TV\\"
# sub_dir ="ancient_TV_en\\"
sub_dir = "ancient_TV_zh\\"
file_name = ''

def coding_detect(file_to_be_detect_char):
    with open(file_to_be_detect_char, mode='rb') as f:
        data = f.read()
        encoding_mode = chardet.detect(data)
        print("the encoding mode of file:{} is {}".format(file_to_be_detect_char, encoding_mode))
    return encoding_mode


def join_text(file_to_be_joined, target_file):
    detect_encode_mode = coding_detect(file_to_be_joined)
    with open(file_to_be_joined, mode="r", encoding= detect_encode_mode['encoding']) as encoded_file:
        text = encoded_file.read()
        with open(target_file, mode = "a+", encoding="utf8") as target_data:
            print("write in the:", target_file)
            target_data.write(text)
            target_data.flush()

# if __name__ == "__main__":
for root, dirs, files in os.walk(root_dir + sub_dir ):
    for file_name in files:
        print("start handle the file: ", root + file_name)
        join_text(root + file_name, root + "joined_file.zh")
    print(coding_detect(root + "joined_file.zh"))


