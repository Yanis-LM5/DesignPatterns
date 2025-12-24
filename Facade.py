"""
L'objectif du pattern facade est de cacher la complexité qu'il faut pour
réaliser un mécanisme logiciel particulier. Généralement, ce mécanisme complexe
est fourni par une ou plusieurs bibliothèques (en anglais "library") ou
un outil plus complexe (appelé "framework").
Ce pattern permet de proposer à un "client" une "interface" plus simple
(ici "interface" design un moyen d'interaction entre deux élements logiciels,
ce n'est pas interface avec polymorphisme) qui va
cacher la plupart des interactions avec la bibliothèque ou le framework.
"""

from abc import ABC, abstractmethod
from enum import StrEnum

# Dans cet exemple d'implémentation, pour faciliter la compréhension et
# la réalisation du pattern, on va prendre plusieurs raccourcis pour
# faciliter l'exercice proposé par
# `https://refactoring.guru/design-patterns/facade`.
#
# On a un mécanisme logiciel de conversion video d'un format 1
# (par exemple MPEG4) vers un format 2 (par exemple OGG).
# La réalisation de ce mécanisme passe par l'utilisation de plusieurs
# classes, avec méthodes et designs patterns associés.
#
# L'objectif de l'exercice est de montrer comment le pattern facade permet
# bien de proposer une interface plus simple à un "client" pour
# réaliser cette conversion. Le plus impportant est de comprendre
# l'intérêt et la structure du pattern, le "réalisme" de l'exercice en
# lui même n'est pas important. Le contexte de conversion video
# va être très simulé.


class VideoFormatEnum(StrEnum):
    OGG = "ogg"
    MP4 = "mp4"
    UNKNOWN = "unknown"


class CompressionCodecStrategy(ABC):
    """
    Represente une interface (avec polymorphisme) qui permettrait de
    coder un buffer d'image vers un format video ou de decoder un buffer d'image
    depuis un format video.

    Pour faciliter l'exercice, on considère que la réalisation du codec
    ne va faire que rajouter une "étiquette" en préfix du buffer image
    d'une video.

    Dans cet exercice, on ne gère pas les problèmes de cohérences entre
    le contenu du buffer image et le codec. On suppose que si
    une implémentation/ réalisation de codec est appelée, alors c'est bien
    le bon codec.
    """

    @abstractmethod
    def code(self, raw_image_buffer: str) -> str:
        """
        Retourne le buffer image transformé, avec l'étiquette du codec.

        :param raw_image_buffer: le buffer image "pur", c'est-à-dire sans le
        flag lié au codec.
        :type raw_image_buffer: str
        :return: le buffer image transformé, avec l'étiquette du codec.
        :rtype: str
        """
        pass

    @abstractmethod
    def decode(self, image_buffer_with_codec: str) -> str:
        """
        Retourne le buffer image "pur", c'est-à-dire sans le
        flag lié au codec.

        :param image_buffer_with_codec: le buffer image avec l'étiquette lié à un codec
        :type image_buffer_with_codec: str
        :return: buffer image "pur"
        :rtype: str
        """


class OggCompressionCodec(CompressionCodecStrategy):
    def __init__(self) -> None:
        self.flag = f"[{VideoFormatEnum.OGG.name}]"

    def code(self, raw_image_buffer) -> str:
        return f"{self.flag}{raw_image_buffer}"

    def decode(self, image_buffer_with_codec: str) -> str:
        return image_buffer_with_codec.removeprefix(
            self.flag,
        )


class MPEG4CompressionCodec(CompressionCodecStrategy):
    def __init__(self) -> None:
        self.flag = f"[{VideoFormatEnum.MP4.name}]"

    def code(self, raw_image_buffer) -> str:
        return f"{self.flag}{raw_image_buffer}"

    def decode(self, image_buffer_with_codec: str) -> str:
        return image_buffer_with_codec.removeprefix(
            self.flag,
        )


class CodecFactory:
    def __init__(self) -> None:
        self.codec_dict: dict[VideoFormatEnum, CompressionCodecStrategy] = {
            VideoFormatEnum.OGG: OggCompressionCodec(),
            VideoFormatEnum.MP4: MPEG4CompressionCodec(),
        }

    def getCodec(
        self, video_format: VideoFormatEnum
    ) -> CompressionCodecStrategy:
        return self.codec_dict.get(video_format, OggCompressionCodec())


class VideoFile:
    """
    Cette class represente la structure simplifiée d'un fichier video
    avec un format donné, et qui ne contiendrait que des images.
    """

    def __init__(
        self,
        filename: str,
        image_buffer_with_codec: str = "",
    ) -> None:
        """
        :param filename: le nom du fichier video
        :type filename: str
        :param image_buffer_with_codec: represente une simplification des données binaires
            du contenu image de la video.
        :type image_buffer_with_codec: str
        """
        self.filename = filename

        # Calcule le format de la video à partir de l'extension du fichier.
        tokens = self.filename.split(".")
        self.format: VideoFormatEnum = (
            VideoFormatEnum[tokens[-1].upper()]
            if len(tokens) > 0
            else VideoFormatEnum.UNKNOWN
        )

        self.image_buffer_with_codec = image_buffer_with_codec

    def __str__(self) -> str:
        """
        Permet de serialiser une instance de cette class sous forme de
        `string`.
        De sorte à pouvoir utiliser `print(object)` comme par exemple:
        ```
        input_video_file = VideoFile("name.mp4", "[MP4]buffer")
        print(input_video_file)
        ````

        :return: la serialisation sous forme de string
        :rtype: str
        """
        return f"{self.filename}, {self.format}, {self.image_buffer_with_codec}"


class BitRateReader:
    def read(
        self,
        input_video_file: VideoFile,
        source_codec: CompressionCodecStrategy,
    ) -> str:
        """
        Retourne le buffer image "pur" d'un fichier video passé en argument.
        """
        return source_codec.decode(input_video_file.image_buffer_with_codec)

    def convert(
        self, raw_image_buffer: str, destination_codec: CompressionCodecStrategy
    ) -> str:
        """
        Retourne le buffer image transformé dans le format video du codec passé
        en argument.
        """
        return destination_codec.code(raw_image_buffer)


class VideoConverterFacade:
    """
    Implémentation d'une façade pour cacher la complexité de transformer
    un fichier video d'un format en un autre.

    `convertVideo` retourne le resultat de la transformation dans un autre format.
    """

    def convertVideo(
        self, input_video_file: VideoFile, destination_format: VideoFormatEnum
    ) -> VideoFile:
        # Recupère les codecs grace au factory.
        codec_factory = CodecFactory()
        source_codec = codec_factory.getCodec(input_video_file.format)
        destination_codec = codec_factory.getCodec(destination_format)

        # Transforme le buffer image grâce au bit_rate_reader et aux codecs.
        bit_rate_reader = BitRateReader()
        real_image_buffer = bit_rate_reader.read(input_video_file, source_codec)
        destination_image_buffer = bit_rate_reader.convert(
            real_image_buffer, destination_codec
        )

        # Crée le fichier video avec le buffer image transformer à renvoyer.
        result_video_filename = input_video_file.filename.replace(
            input_video_file.format.value, destination_format.value
        )
        result_video = VideoFile(
            result_video_filename, destination_image_buffer
        )

        return result_video


if __name__ == "__main__":
    input_video_file = VideoFile("funny-cat-video.mp4", "[MP4]nyan-cat")
    print(input_video_file)

    video_converter_facade = VideoConverterFacade()
    result_video_file = video_converter_facade.convertVideo(
        input_video_file, VideoFormatEnum.OGG
    )

    print(result_video_file)
