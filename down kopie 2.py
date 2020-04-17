#os.rename(r'/Users/MWK/Desktop/OLE/tatiana/91018230_151840196296351_1894637158564459764_n%201.jpg',r'/Users/MWK/Desktop/OLE/tatiana/tatiana_art_1.jpg')
import wget
import os
import multiprocessing

def run_process(url, output_path):
    wget.download(url, out=output_path)
    # TODO: you can write your rename logic at here using os.rename


if __name__ == '__main__':
    cpus = multiprocessing.cpu_count()
    max_pool_size = 4
    pool = multiprocessing.Pool(cpus if cpus < max_pool_size else max_pool_size)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target = "tatiana_art"
    prefix_list = ["91018230_151840196296351_1894637158564459764_n"]
    download_list = []
    name_list = list(range(1, 14))
    #name_list.extend(["zoom_side", "zoom_sole", "zoom_side-thumb"])
    for prefix in prefix_list:
        path = os.path.join(base_dir, "tatiana")
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.isdir(path):
            exit()
        for name in name_list:
            download_list.append(['https://raw.githubusercontent.com/oliverwk/oliverwk.github.io/master/tatiana%20art/91018230_151840196296351_1894637158564459764_n{n}.jpg'.format(n=name, p=prefix), path])

    for url, path in download_list: # change here to download other files
        print('Beginning file download with wget module {n}'.format(n=url))
        pool.apply_async(run_process, args=(url, path, ))
        #print('{n}' .format(n=url))
        os.rename(r'/Users/MWK/Desktop/OLE/tatiana/91018230_151840196296351_1894637158564459764_n{n}.jpg',r'/Users/MWK/Desktop/OLE/tatiana/tatiana_art_{n}.jpg' .format(n=url))

    # add your code here to download other files
    pool.close()
    pool.join()
    print("finish")
