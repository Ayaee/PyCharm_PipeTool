import glob


def get_files():
    hard_coded_path = 'G:/Artfx/TD4/WS_MicroFilm/MOVIE/ASSETS'
    files = glob.glob(hard_coded_path + "/*/*/*/*.*")
    return files


if __name__ == '__main__':

    for f in get_files():
        print(f)
    # print(get_files())
