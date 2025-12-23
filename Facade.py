
class VideoFile:

    def __init__(self, filename: str):
        self.name = filename


class OggCompressionCodec:

    def format(self) -> str:
        return ".ogg"


class MPEG4Compression:

     def format(self) -> str:
        return ".mp4"

class CodecFactory:

    def extract(self, file: VideoFile) -> None:
        print(f"extracting {file.name}")

class BitrateReader:

    def read(self, filename: str) -> None:
        print(f"reading {filename}")

    def convert_format(self, filename: str, format: str ) -> str:
        self.read(filename)
        print("audio not fixed, don't forget to fix it" )
        return filename.strip(".")+format


class AudioMixer:
    def fix(self, file: str) -> None:
        print ("audio fixed :)")
        pass


class VideoConverter:
    def conversion(self, filename: str, format: str ) -> VideoFile:
        file = VideoFile(filename)

        sourceCodec = CodecFactory().extract(file)

        if (format.lower()=="mp4"):
            destinationCodec = MPEG4Compression().format()

        else:
            destinationCodec = OggCompressionCodec().format()

        buffer = BitrateReader().read(filename)
        res = BitrateReader().convert_format(filename, destinationCodec)
        res_audio = AudioMixer()
        res_audio.fix(filename)
        print(f"here is your file '{res}'")
        return VideoFile(filename)





if __name__=="__main__":
    convertor = VideoConverter()
    mp4 = convertor.conversion("funny-cat-video.ogg","mp4")