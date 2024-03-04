import fitz  # PyMuPDF
from PIL import Image
import os

def compress_pdf(input_pdf_path, output_pdf_path, max_size_mb, scale_decrease, image_quality=50):
    scale_factor = 1.0  # 初始缩放因子
    max_size = max_size_mb * 1024 * 1024  # 将MB转换为字节
    scale_decrease = 1 - (scale_decrease / 100)  # 转换为缩减比例

    while True:
        # 打开原始PDF文件
        pdf = fitz.open(input_pdf_path)
        compressed_images = []

        for page_number in range(len(pdf)):
            # 将PDF页面转换为图片
            page = pdf.load_page(page_number)
            pix = page.get_pixmap(matrix=fitz.Matrix(scale_factor, scale_factor))
            image_path = f"temp_page_{page_number}.png"
            pix.save(image_path)

            # 打开并保存图片
            compressed_image_path = f"compressed_page_{page_number}.jpg"
            Image.open(image_path).save(compressed_image_path, "JPEG", quality=image_quality)
            compressed_images.append(compressed_image_path)

            # 删除原始图片以节省空间
            os.remove(image_path)

        # 创建新的PDF并添加压缩后的图片
        compressed_pdf = fitz.open()
        for img_path in compressed_images:
            imgdoc = fitz.open(img_path)
            pdfbytes = imgdoc.convert_to_pdf()
            imgpdf = fitz.open("pdf", pdfbytes)
            compressed_pdf.insert_pdf(imgpdf)

            # 删除已使用的压缩图片
            os.remove(img_path)

        # 检查文件大小
        compressed_pdf.save(output_pdf_path)
        if os.path.getsize(output_pdf_path) <= max_size:
            break  # 如果大小符合要求，则结束循环

        compressed_pdf.close()
        scale_factor *= scale_decrease  # 逐渐减小缩放因子

    compressed_pdf.close()

# 接收用户输入
input_file_name = input("请输入要压缩的PDF文件名（包括.pdf扩展名）: ")
max_size_mb = float(input("请输入目标PDF文件大小（MB）: "))
scale_decrease_percentage = float(input("请输入每次减小图像分辨率时缩放因子的降低百分比（例如输入10表示每次减少10%）: "))
output_file_name = input_file_name.replace('.pdf', '_compressed.pdf')

# 使用示例
compress_pdf(input_file_name, output_file_name, max_size_mb, scale_decrease_percentage)
