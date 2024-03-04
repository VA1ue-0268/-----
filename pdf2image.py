import os

import fitz  # fitz就是pip install PyMuPDF

def pyMuPDF_fitz(filename, pdfPath, imagePath):  # PDF路径 保存图片路径 PDF编号
    # print("imagePath=" + imagePath)
    doc = fitz.open(pdfPath)
    for i, pg in enumerate(doc.pages()):
        trans = fitz.Matrix(5, 5)
        pix = pg.get_pixmap(matrix=trans)
        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建
        pix.pil_save(f"./{imagePath}/{filename}_{i}.png", compress=False)


if __name__ == "__main__":
    path = './' 
    for filename in os.listdir(path):
        # 1、PDF地址
        if '.pdf' not in filename and '.caj' not in filename:
            continue
        print('正在处理 {}'.format(filename))
        pdfPath = path+'/'+filename
        # 2、需要储存图片的目录
        imagePath = './imgs'
        pyMuPDF_fitz(filename, pdfPath, imagePath)
        print('已处理 {}'.format(filename))
    input("完成！按任意键退出。")