from pytube import YouTube, StreamQuery, Stream


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# path = 'C:Downloads'
# url = ''
# pytube.YouTube(url).streams.get_highest_resolution().download(path)

def title(video_url):
    """
    Gets the title for the video whose url is passed and returns it.
    :param video_url: The url of the video to be downloaded
    :return: The title of the video to be downloaded.
    """
    return YouTube(video_url).title


def get_resolutions(video_url):
    """
    Gets the available video resolutions to allow for user to download.
    :param video_url: the url whose resolutions are to be queried
    :return: a list of available resolutions e.g "720p"
    """
    vid: StreamQuery = YouTube(url=video_url).streams.filter(progressive=True)
    v: Stream
    return [v.resolution for v in vid]


def download(res, path, video_url):
    """
    Downloads a video from YouTube with the given video url, saves it in the given file path using the resolution
    specified.
    :param res: resolution of the video to be downloaded.
    :param path: relative file path the video is downloaded to.
    :param video_url: the YouTube url of the video to be downloaded.
    :return:
    """
    video = YouTube(url=video_url).streams.filter(progressive=True, res=res).first()
    if video is None:
        return 'Video not found!', False, None
    path = video.download(output_path=path)
    return 'Video downloaded successfully!', True, path
