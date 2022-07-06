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
    return YouTube(video_url).title


def get_resolutions(video_url):
    vid: StreamQuery = YouTube(url=video_url).streams.filter(progressive=True)
    v: Stream
    return [v.resolution for v in vid]


def download(res, path, video_url):
    video = YouTube(url=video_url).streams.filter(progressive=True, res=res).first()
    if video is None:
        return 'Video not found!', None
    path = video.download(output_path=path)
    return 'Video downloaded successfully!', path
