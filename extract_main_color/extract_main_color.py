import numpy as np
import cv2

from pathlib import Path


def get_main_hsv_color(img):
    # img1 = cv2.resize(img, (round(img.shape[1] / 10), round(img.shape[0] / 10)))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # s = np.mean(np.reshape(img[:, :, 1], -1))
    # v = np.mean(np.reshape(img[:, :, 2], -1))
    harr = img[:, :, 0]
    h = np.argmax(np.bincount(np.reshape(img[:, :, 0], -1)))
    xy = np.where(harr == h)
    nimg = img[xy]
    s = np.mean(nimg[:, 1])
    v = np.mean(nimg[:, 2])

    tc = np.array([h, s, v], dtype=np.uint8)
    tc = tc.reshape(1, 1, 3)
    tc_bgr = cv2.cvtColor(tc, cv2.COLOR_HSV2BGR)
    tc_bgr = tc_bgr.reshape(-1)
    b, g, r = tc_bgr[0], tc_bgr[1], tc_bgr[2]
    return b, g, r
    # ret = hex(tc_bgr[2] * pow(16, 4) + tc_bgr[1] * 256 + tc_bgr[0])
    # ret = ret[2:]
    # if len(ret) < 6:
    #     ret = "0" * (6 - len(ret)) + ret
    # pass
    # return ret


if __name__ == "__main__":
    img_dir = Path("imgs")
    result_dir = Path("color_results")
    img_paths = img_dir.rglob("*.jpg")
    for img_path in img_paths:
        img = cv2.imread(str(img_path))
        b, g, r = get_main_hsv_color(img)
        save_img = np.zeros_like(img, dtype=np.uint8)
        save_img[:, :, 0] = b
        save_img[:, :, 1] = g
        save_img[:, :, 2] = r

        save_path = result_dir.joinpath(img_path.name)
        cv2.imwrite(str(save_path), save_img)
        pass
